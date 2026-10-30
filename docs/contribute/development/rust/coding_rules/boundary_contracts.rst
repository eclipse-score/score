..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

.. _rust_boundary_contracts:

Panic and Foreign Boundary Contracts
####################################

.. document:: Rust Panic and Foreign Boundary Contracts
   :id: doc__rust_coding_rules_boundary_contracts
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]

This page holds the detailed conditions behind :ref:`SCR-RUST-036 <scr-rust-036>` and
:ref:`SCR-RUST-042 <scr-rust-042>`. The rule entries state what to do; this page states
the exact conditions a reviewer checks at a panic or foreign-language boundary. Each
condition is paired with the hazard it prevents.

.. _rust_boundary_contracts_panic:

Panic boundaries
================

**Choosing the level.** Every boundary where a panic could matter, such as a public
library API, a callback passed to foreign code or a destructor, declares one level:

* *Panic-free*: the path never initiates a panic. This includes implicit panics from
  indexing, slicing, integer arithmetic with overflow checks, ``unwrap``/``expect``, and
  allocation failure. Use checked operations and return ``Result``.
* *Panic-contained*: a panic may occur inside but shall not escape the boundary.

**Destructors are panic-free.** A custom ``Drop`` and the field destructors it relies on
shall not panic. A panic inside a destructor that runs during unwinding aborts the
process, and under ``panic=abort`` any destructor panic aborts.

**Catching panics.** Converting a panic into an error with ``std::panic::catch_unwind``
is acceptable only on a panic-contained boundary, only when the delivered panic strategy
is ``unwind``, and only when the code after the catch is itself panic-free. That includes
dropping the caught payload and any guards still alive outside the catch. Under
``panic=abort`` the catch never runs. ``catch_unwind`` shall not be relied on to recover
a foreign exception or an abort.

.. code-block:: rust

   // Compliant: panic-contained boundary, panic=unwind, panic-free after the catch.
   pub fn run(job: impl FnOnce() + std::panic::UnwindSafe) -> Result<(), JobError> {
       match std::panic::catch_unwind(job) {
           Ok(()) => Ok(()),
           Err(_payload) => Err(JobError::Panicked), // dropping the payload cannot panic here
       }
   }

.. code-block:: rust

   // Non-compliant: the payload is handled after the catch in a way that can panic again.
   pub fn run(job: impl FnOnce() + std::panic::UnwindSafe) -> Result<(), JobError> {
       match std::panic::catch_unwind(job) {
           Ok(()) => Ok(()),
           Err(payload) => {
               let msg = payload.downcast::<String>().unwrap(); // panics for a &str payload
               Err(JobError::Message(*msg))
           }
       }
   }

**Payload contents.** A payload passed to ``std::panic::panic_any`` shall carry only owned
data or ``'static`` references. The ``'static + Any + Send`` bound already rejects a bare
raw pointer and a non-``'static`` borrow, but an integer address, a handle or a wrapper
can still smuggle access to borrowed storage that is gone by the time the payload is
inspected. Those are prohibited.

**Termination.** Libraries shall not call ``std::process::exit``, ``std::process::abort``
or equivalents, nor take or store their addresses, nor reach them through foreign code.
``clippy::exit`` sees only direct calls, so stored function pointers need an inventory.
The only accepted fail-stop is the abort produced by a failed assertion or by the
delivered panic strategy. A component that needs another fail-stop path documents the
system response, including cleanup or external recovery, as an adaptation.

**Strategy.** Record the delivered panic strategy per target. A rule stated for
``panic=unwind`` does not transfer to ``panic=abort``: catching is impossible, and the
panic-contained level collapses into panic-free.

.. _rust_boundary_contracts_ffi:

Foreign-language boundaries
===========================

**Unwinding.** Functions exported or imported through ``extern "C"`` are panic-contained
on the Rust side: a Rust panic reaching a non-unwinding ``extern "C"`` frame aborts, and a
foreign exception entering Rust through it is undefined behavior. ``extern "C-unwind"``
may be used only when both sides support unwinding and the delivered panic strategy is
``unwind``. The whole Rust wrapper around a foreign call or callback, including its
cleanup, follows the panic rules above.

**Nonlocal transfers.** ``setjmp``/``longjmp`` and similar transfers shall not cross a
Rust frame; skipping Rust frames skips their destructors and leaves the program in a
state the compiler assumed impossible. Foreign-only use stays inside the foreign region
under that code's own policy.

**Signals.** Signal handling is limited to the platform APIs the component documents.
Installing a handler requires an async-signal-safety assessment of everything the
handler calls. Disabling a signal is permitted where the component documents it.

**Error state.** Handle ``errno`` and equivalents per the API contract: read it only when
the return value says it is meaningful, clear it before the call where the API requires,
and capture it immediately, before logging or any other call can overwrite it.
Application code shall not write ``errno`` except to set it to zero, written as the
literal ``0`` or as a Rust ``const`` or macro whose value is that literal; a runtime
variable that happens to hold zero is not permitted. ``std::io::Error::last_os_error``
reads ``GetLastError`` on Windows and is not a portable substitute for reading ``errno``.

.. code-block:: rust

   // Compliant: errno captured immediately, only when the return value makes it meaningful.
   let rc = unsafe { libc::close(fd) };
   if rc == -1 {
       let err = std::io::Error::last_os_error(); // captured before any other call
       log::warn!("close failed: {err}");
       return Err(err);
   }

.. code-block:: rust

   // Non-compliant: the log call may overwrite errno before it is read.
   let rc = unsafe { libc::close(fd) };
   if rc == -1 {
       log::warn!("close failed");
       return Err(std::io::Error::last_os_error());
   }

**Locale.** Rust code shall not change the process-wide locale. A component that must do
so documents initialization ordering and concurrency conditions for all affected foreign
code as an explicit adaptation.

**Returned storage.** Storage returned by ``localeconv``, ``getenv``, ``setlocale`` and
``strerror``, including the strings nested in ``lconv``, is read-only. A shared reference
created from it, including through ``CStr::from_ptr``, is valid only while no foreign
code can mutate the storage. An owned snapshot shall be taken by a valid, race-free read
of the whole data, including nested strings. The addresses of these four functions shall
not be taken or stored for indirect calls.

**Invalidation by later calls.** Pointers returned by ``asctime``, ``ctime``, ``gmtime``,
``localtime``, ``localeconv``, ``getenv``, ``setlocale`` and ``strerror`` shall not be used
after a later call, on any thread, to the same function or to one that invalidates the
same storage. Known pairs are ``setlocale`` after ``localeconv``, ``asctime`` with
``ctime``, and ``gmtime`` with ``localtime``. Copy the data while the read is valid and
protected.

.. code-block:: rust

   // Compliant: snapshot taken while the read is valid, before any other call.
   let value: Option<String> = unsafe {
       let p = libc::getenv(c"HOME".as_ptr());
       if p.is_null() { None } else { Some(std::ffi::CStr::from_ptr(p).to_string_lossy().into_owned()) }
   };

.. code-block:: rust

   // Non-compliant: the borrowed CStr is used after a call that may invalidate it.
   let home = unsafe { std::ffi::CStr::from_ptr(libc::getenv(c"HOME".as_ptr())) };
   let _ = unsafe { libc::setlocale(libc::LC_ALL, c"".as_ptr()) };
   println!("{}", home.to_string_lossy()); // may read invalidated storage

**Remaining work.** MISRA C:2025 Addendum 6 assesses 223 MISRA C guidelines for Rust.
S-CORE has not yet derived and checked an obligation for every entry it marks applicable
at a boundary. This page covers the concerns of the MISRA C++ sources linked from
SCR-RUST-042 and the addendum comments on R.8.3, R.8.5, R.8.6 and R.8.15; completing the
derivation is open work for a later rulebook revision.
