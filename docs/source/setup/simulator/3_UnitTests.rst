*****************
3. M&C Unit Tests
*****************

Set up the tests
================

Unit Tests are run from the source directories. Running the unit tests for the M&C modules requires some preparation. This is due to the fact that some of the unit tests need a) a configuration file, or b) to run against a daemon. For this reason, the unit tests need to run against a simulation. Because of the dependencies of some unit tests on M&C simulator components, the developer should pay special attention to whether or not the simulator is in use by checking the simulator calendar prior to running unit tests. If it is in use, results of the unit tests may not be consistent or reliable. Thus in the below instructions (from the comments in the gbtunit_test script), the ``/home/sim/gbt.bash_`` and ``sparrow.bash`` files are sourced:

.. code:: bash

    export YGOR_ROOT=/home/sandboxes/${USER}/mc/ygor
    export GB_ROOT=/home/sandboxes/${USER}/mc/gb
    source $YGOR_ROOT/ygor.bash
    source /home/sim/gbt.bash
    source /home/sandboxes/${USER}/mc/sparrow/sparrow.bash

Run the tests
=============

`Ygor`
------

.. code:: bash

    cd /home/sandboxes/${USER}/mc/ygor/unit_test
    ./ygor_unit_test

`Gb`
----

Running the unit tests for the `gb` module is even easier: there are none.

`Gbt`
-----

.. warning::

    There is a hard-coded path for `sparrow` in ``gbt/devices/misc/AntennaCharacterization/unit_test/etc/config/AntennaCharacterization.conf``, used for AntennaCharacterization unit test. Make sure this path points to a compatible version of `sparrow`!

.. code:: bash
    
    cd /home/sandboxes/${USER}/mc/gbt/unit_test
    ./gbt_unit_test