Launch manager
==============

.. logic_arc_int:: Alive Interface
   :id: logic_arc_int__lifecycle__alive_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

.. comp_arc_sta:: Launch Manager
   :id: comp_arc_sta__lifecycle__launch_manager
   :status: valid
   :safety: ASIL_B
   :implements: logic_arc_int__lifecycle__controlif, logic_arc_int__lifecycle__alive_if
   :uses: logic_arc_int__logging__logging
   :security: NO
   :includes: 
   :fulfils:

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


