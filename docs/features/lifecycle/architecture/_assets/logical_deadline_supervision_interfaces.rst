Deadline and Logical Supervision Interfaces
==========================================

This document describes the logical interfaces for the Deadline and Logical Supervision components, using abstracted and non-matching names for clarity and generality.

Deadline Supervision Interface
-----------------------------

.. code-block:: text

    Interface: TimeConstraintMonitor

    Methods:
        - configure_minimum_time(min_time):
            Set the minimum allowed time for the monitoring window.
        - configure_maximum_time(max_time):
            Set the maximum allowed time for the monitoring window.
        - link_condition(condition):
            Add a reference to a related condition for monitoring.
        - mark_start():
            Mark the start of the timing window (e.g., source event).
        - mark_end():
            Mark the end of the timing window (e.g., target event).
        - on_timer_expiry():
            Handle the event when the timer expires.
        - enable_monitoring():
            Activate the time constraint monitoring.
        - disable_monitoring():
            Deactivate the time constraint monitoring.
        - check_configuration():
            Validate the configuration of the monitor.

Logical Supervision Interface
----------------------------

.. code-block:: text

    Interface: LogicalSupervisionManager

    Methods:
        - add_entry_point(checkpoint_id):
            Add a node as an entry point in the flow graph.
        - add_exit_point(checkpoint_id):
            Add a node as an exit point in the flow graph.
        - add_allowed_transition(transition):
            Add an allowed transition (edge) between checkpoints.
        - link_condition(condition):
            Add a reference to a related condition for flow.
        - record_checkpoint(checkpoint_id):
            Record a checkpoint and check if the transition is allowed.
        - enable():
            Enable the process flow supervision.
        - disable():
            Disable the process flow supervision.
        - verify():
            Verify the flow graph.
