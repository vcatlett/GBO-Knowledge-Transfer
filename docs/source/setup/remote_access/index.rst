********************************
Remote Access to the GBO Network
********************************

To ensure good performance on our gateway login machines (ssh.gb.nrao.edu & stargate.gb.nrao.edu), please follow the following guidelines from CIS.

First we would like to remind you not to run data reduction jobs on either of these machines. Please use one of the machines intended for that purpose (euclid, thales, fourier, planck, newton).

Observing sessions should not be run from ssh or stargate either. Please use one of the dedicated machines for that (ariel, titania) and ensure that you terminate your session on those machines entirely once you have finished observing.

Firefox and thunderbird both suffer from memory leaks and it helps if you avoid running them on the gateway machines altogether but if you must please terminate them when you are done and don't leave them running for days on end. (GB staff should run these on their own desktop machines) Unless you are accessing internal only web resources you are better served by running a browser on the computer you are sat in front of.

For data reduction sessions that may run for hours users should consider using the screen command (type "man screen" for more info) This can help you avoid the frustration of losing your connection and having to start over.

.. toctree::
    :maxdepth: 1
    :titlesonly:

    fastx
    xfreerdp
    vnc