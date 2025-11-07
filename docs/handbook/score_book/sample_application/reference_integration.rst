Reference integration
=======================
After we've build a scrample binary for qnx x86 image, as described in the previous chapter,
let us now give it a try in the reference qnx image for the x86 platform.

Reference integration repository already provides a
`reference qnx image  <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_.

The reference QNX image is currently really rudimentary, providing minimal set of tooling in the IFS image (TODO: link to QNX IFS image desc).
If you interested in the more detailed description of the qnx reference image in Eclipse S-CORE, you should check following file: (TODO: Link to QNX description).
Its content is defined in the qnx build file (TODO: link to file) as following:

.. code-block:: python
    
    qnx_ifs(
        name = "init",
        build_file = "init.build",
        srcs = [
            "system.build",
            ":scripts",
            ":configs",
        ],
        visibility = [
            "//:__pkg__"
        ],
    )

    

