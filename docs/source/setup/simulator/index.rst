****************************
How to Make an M&C Simulator
****************************

What is a Simulator?
====================

A "Simulator" in this context is a specific type of M&C System installation. As far as I can tell, there are three types of M&C installation:

#. GBT M&C System. This lives at /home/gbt, and is used to control real hardware and do real things

#. Simulated GBT M&C System. This lives at /home/sim, and is used to control some real hardware, but not production hardware. It is not used to perform real observations

#. Sandbox GBT M&C System. These live in the various developer sandboxes, and are typically not used to interact with real hardware (although they certainly can).

This document traces the problems I faced in trying to set up type (3), and how I resolved them.

Creating a Release
==================
This process is copied, but updated, from `DevelopingMC <https://safe.nrao.edu/wiki/bin/view/GB/Software/DevelopingMC>`_.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   1_CreateSparrowEnv
   2_SetUpMCRepos
   3_UnitTests
   4_CreateTelescope