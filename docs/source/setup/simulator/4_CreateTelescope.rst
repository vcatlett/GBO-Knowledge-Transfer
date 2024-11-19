***********************
4. Creating a Telescope
***********************

This process is outlined in `ToyTelescope <https://safe.nrao.edu/wiki/bin/view/GB/Software/YgorManagerToyExample#Development_Environment>`_. However, Thomas has implemented most of it via a script.

.. code:: bash

    export YGOR_ROOT=/home/sandboxes/${USER}/mc/ygor
    export GB_ROOT=/home/sandboxes/${USER}/mc/gb
    export YGOR_INSTALL=/home/sandboxes/${USER}/mc/ygor/install
    source $YGOR_ROOT/ygor.bash
    source /home/sim/gbt.bash
    source /home/sandboxes/${USER}/mc/sparrow/sparrow.bash

1. Run  ``make_telescope``  and follow the instructions
2. ...that's it

Your environment should look like this:

.. code:: bash

    YGOR_INSTALL_ROOT=/home/sandboxes/${USER}/mc/ygor/install
    YGOR_INSTALL=/home/sandboxes/${USER}/mc/ygor/install
    YGOR_TELESCOPE=/home/sandboxes/${USER}/THE_SIM
    YGOR_ROOT=/home/sandboxes/${USER}/mc/ygor
    YGOR_INSTALL_FOLDER=/home/sandboxes/${USER}/mc/ygor/install

After sourcing the provided gbt.bash you will be "in" the new simulator.  ``$ cdtele``  will now take you to your `$YGOR_TELESCOPE`. As  monctrl , you should now be able to start up the simulator on the host you indicated during setup.

.. code:: bash

    cdtele
    ./ygor_system start

.. note::

    Error for kpurcell:

    .. code:: bash
        
        ERROR 1045 (28000): Access denied for user 'monctrl'@'localhost' (using password: YES)
        --- Executing: "mysql" ---
        ERROR 1045 (28000): Access denied for user 'kpurcell'@'localhost' (using password: YES)
        --- ERROR: mysql failed! ---
        /home/sandboxes/kpurcell/kasey_simulator/mnc_repos/mc_utils/bash_functions: line 59: exit: --defaults-file=/users/monctrl/.my.cnf: numeric argument required