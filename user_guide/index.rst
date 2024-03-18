User Guide
----------

MDI uses a driver/engine paradigm in which drivers orchestrate complex simulations by controlling engines through the use of an API-like command set that is defined by the MDI Standard. 
A driver will typically implement one or more high-level methods, such as advanced sampling or QM/MM, while relying on one or more engines to perform lower-level operations, such as energy and force evaluation.

In total, MDI consists of the following components:

* Drivers, which are codes that control the high-level program flow of one or more other codes.
* Engines, which are codes capable of responding to commands from an external driver.
* The MDI Standard, which is an API-like definition of a set of commands that can be sent from a driver to an engine, and that cause the engine to respond in a clearly defined way.
* The MDI Library, which is a library that enables inter-code communication in compliance with the MDI Standard.


.. toctree::
   :maxdepth: 1

   installation
   mdi_standard
