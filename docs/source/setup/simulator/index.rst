********************
Telescope Simulators
********************

What is a Simulator?
====================

A "Simulator" in this context is a specific type of :term:`M&C` System installation. As far as I can tell, there are three types of :term:`M&C` installation:

#. GBT M&C System. This lives at /home/gbt, and is used to control real hardware and do real things

#. Simulated GBT M&C System. This lives at /home/sim, and is used to control some real hardware, but not production hardware. It is not used to perform real observations

#. Sandbox GBT M&C System. These live in the various developer sandboxes, and are typically not used to interact with real hardware (although they certainly can).


Creating a Simulator
====================

This process is copied, but updated, from `DevelopingMC <https://safe.nrao.edu/wiki/bin/view/GB/Software/DevelopingMC>`_.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   1_CreateSparrowEnv
   2_SetUpMCRepos
   3_UnitTests
   4_CreateTelescope