Assumptions of Use
##################

.. aou_req:: Monotonic Semi-Dynamic Memory Allocation
   :id: aou_req__communication__1
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that enough memory is configured for shared memory instances,
   in order that LoLa can perform all necessary allocations (e.g. push-back on a Vector).

.. aou_req:: Correctly Configured Maximum Number of Subscribers
   :id: aou_req__communication__2
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that correct maximum number of subscriber is configured for each
   event for each service instance.

.. aou_req:: Correctly configured maximum number of maximum elements per subscriber
   :id: aou_req__communication__3
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

    It shall be ensured that correct maximum number of elements per subscriber is
    configured for each event for each service instance.

.. aou_req:: Correctly configured ASIL Level
   :id: aou_req__communication__4
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

    The ASIL-Level is used to ensure Freedom from Interference (e.g. by configuring access rights).
    Without a proper configured level, this cannot be ensured.

.. aou_req:: Only LoLa supported types
   :id: aou_req__communication__5
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured, that only types that are supported by LoLa are transmitted.

.. aou_req:: No APIs from Implementation Namespace
   :id: aou_req__communication__6
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that no API calls from the implementation namespace (e.g `impl`)
   are directly invoked or types from within are directly used.

.. aou_req:: No guarantees for notifications
   :id: aou_req__communication__7
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that a miss behavior of event notification, will not harm a safety goal.

.. aou_req:: Checking for possible message overflow
   :id: aou_req__communication__8
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that a message overflow, which results in message loss will not harm a safety goal.
   If this is not possible, a check for message overflow and necessary actions need to be performed.

.. aou_req:: Different user for ASIL and QM processes
   :id: aou_req__communication__9
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that processes with a different ASIL shall be executed within different user-ids.

.. aou_req:: Config on a safe filesystem
   :id: aou_req__communication__10
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that any configuration item that is read at runtime by LoLa is
   stored on a safety certified filesystem (according to the highest supported safety level).

.. aou_req:: No static context support
   :id: aou_req__communication__11
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that LoLa is not used within static context within C++.

.. aou_req:: No guarantee in availability of services
   :id: aou_req__communication__12
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that no safety goal is harmed, because a service instance is not found.

.. aou_req:: No notification on termination of producer
   :id: aou_req__communication__13
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensure that termination (either gracefully or due to a malfunction)
   of a producer will not lead to a violation of a safety goal.

.. aou_req:: Check for nullptr on Allocate()
   :id: aou_req__communication__14
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be checked if Allocate() on an event will return a nullptr. If a nullptr is returned,
   the system shall transition to safe state.


.. aou_req:: One producer only one AllocateePtr
   :id: aou_req__communication__15
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that at any time a producer instance per event only holds one AllocateePtr.

.. aou_req:: No Copy-Send() while holding AllocateePtr.
   :id: aou_req__communication__16
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that Send(const& value) is not invoked while an AllocateePtr is held.

.. aou_req:: None reentrant methods per event instance
   :id: aou_req__communication__17
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that any LoLa API that is bound to a specific event
    instance is not called in a reentrant manner.

.. aou_req:: Skeleton alive while its AllocateePtr being used
   :id: aou_req__communication__18
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that a Skeleton instance is still alive while any AllocateePtr returned by it is used.

.. aou_req:: Event Subscription active while holding SamplePtr
   :id: aou_req__communication__19
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that Unsubscribe() isn't called on a proxy eventinstance as long as
   any SamplePtr provided by it, is still held.

.. aou_req:: Non-Terminating callbacks
   :id: aou_req__communication__20
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that any callback passed to LoLa for invocation is not throwing.

.. aou_req:: Valid callbacks while proxy alive
   :id: aou_req__communication__21
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that all callbacks passed towards LoLa are valid as long as the associated proxy is alive.

.. aou_req:: Quality of data is dependent on producer
   :id: aou_req__communication__22
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that the necessary quality of data is produced by the respective skeleton process.

.. aou_req:: Validity of pointer on LoLa pointer
   :id: aou_req__communication__23
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that no pointer, pointing to the memory of a SamplePtr
   or AllocateePtr is used once the SamplePtr or AllocateePtr are invalid.

.. aou_req:: LoLa Memory only accessed through LoLa
   :id: aou_req__communication__24
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that no other code accesses the mapped memory managed by LoLa.

.. aou_req:: No shared memory allocation in namespace lola
   :id: aou_req__communication__25
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that no other code creates shared memory segments beginning with "lola".

.. aou_req:: LoLa specific QNX Messaging End-Points only accessed through LoLa
   :id: aou_req__communication__26
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that the LoLa specific QNX Message Passing end-points are only accessed through LoLa APIs.

.. aou_req:: aragen not safe
   :id: aou_req__communication__27
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   If aragen is being used to generate LoLa interfaces, any output produced by aragen
   shall be manually reviewed for its correctness.

.. aou_req:: unsupported data-types
   :id: aou_req__communication__28
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that neither variants nor maps are sent via LoLa.

.. aou_req:: No guarantee on execution time
   :id: aou_req__communication__29
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   There is no guarantee on the execution time of any function call provided by LoLa.

.. aou_req:: Usage of configuration "oversubscription"
   :id: aou_req__communication__30
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   If event instance "oversubscription" is enabled. LoLa makes no warranty, that proxies/consumers
   can't suffer from data loss! It is the responsibility of the user to adapt scheduling/event-data
   access in a way, that no data-loss happens.
   However, we can give the guarantee that if only QM consumers misbehave,ASIL consumers are not
   affected by these actions.

.. aou_req:: Same compiler settings for provider and consumer side
   :id: aou_req__communication__31
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   All compiler settings having influence on the binary representation of data exchanged via
   mw::com/LoLa (event, field, service-method payloads) have to be identical for compilation of
   code containing mw::com proxies and skeletons, which communicate.

.. aou_req:: Event or Field reception via GenericProxy needs specific care
   :id: aou_req__communication__32
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   When receiving event or field data via untyped GenericProxyEvent or GenericProxyField, care has to
   be taken, when accessing the corresponding SamplePtr<void> delivered by calls to GetNewSamples():
   When casting it to the expected type, it needs to be checked, that no access behind the size returned
   by GetSampleSize() will happen.

.. aou_req:: Correctly configured events/fields per service type
   :id: aou_req__communication__34
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid

   It shall be ensured that all safety relevant events/fields in the service type,
   are the same in all configurations.
