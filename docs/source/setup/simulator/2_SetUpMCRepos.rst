***********************
2. Set Up the M&C Repos
***********************

Checkout Source
===============

For checking out the trunk:

If you followed the sparrow steps then do the below
---------------------------------------------------

.. code:: bash

    cd /home/sandboxes/${USER}/mc
    for d in ygor gb gbt; do git clone /home/gbt2/git/integration-bare/$d $d; done;

If you did NOT do the sparrow steps do the below
------------------------------------------------

.. code:: bash

    cd /home/sandboxes/${USER}
    mkdir mc
    cd mc
    for d in ygor gb gbt; do git clone /home/gbt2/git/integration-bare/$d $d; done;

Set-up your build environment
=============================

Exports that you may need later:

.. code:: bash

    export YGOR_ROOT=/home/sandboxes/${USER}/mc/ygor
    export YGOR_INSTALL=/home/sandboxes/${USER}/mc/ygor/install
    export GB_ROOT=/home/sandboxes/${USER}/mc/gb
    source $YGOR_ROOT/ygor.bash

.. warning::

    * Edit `PYTHONINCLUDES` and `PYTHONLIBS` in ``ygor/include/CommonRules.mk`` if necessary for the correct McPython path.
    * Also edit `SWIGCMD` and `SWIGLIB` in ``gbt/user/python/lib/wrappers/Makefile`` if necessary for the correct path to swig (possibly a McPython path).

Build the new source tree
=========================

.. warning::

    IMPORTANT: You may execute all the steps, save the last one, with your login. To successfully execute the  `mkTelescopeDirs`  script, you must be logged in as  monctrl .

.. note::

    The ``make depend`` command is intended to build a dependency tree so that future compilations don't result in a full recompile. If organizational changes are made to the repo, or branches are changed, etc., then  $ make depend  should be run again.

Make the repos
--------------

.. code:: bash

    cd /home/sandboxes/${USER}/mc
    for d in ygor gb gbt; do cd $d; touch .depend; make 2>&1 | tee make.out ;
    make depend; cd ..; done;


Make the telescope dirs
-----------------------

.. code:: bash

    ssh monctrl@galileo
    cd /home/sandboxes/${USER}/mc/ygor/utilities/host/installScripts
    export YGOR_ROOT=/home/sandboxes/${USER}/mc/ygor
    export YGOR_INSTALL=/home/sandboxes/${USER}/mc/ygor/install
    export GB_ROOT=/home/sandboxes/${USER}/mc/gb
    source $YGOR_ROOT/ygor.bash
    ./mkTelescopeDirs
    
    cd /home/sandboxes/${USER}/mc
    for d in ygor gb gbt; do cd $d; make install; cd ..; done;

Inspect the output of the builds
--------------------------------

Inspect the output of the builds to guarantee the release is clean and complete. Errors must be resolved before continuing. Warnings should be forwarded to the responsible programmer.

TIP: In order to guarantee that there are no errors or warnings during any of the steps in the build and install process you would have to either stare at the output during the entire procedure, or pipe stdout & stderr to a file and look for errors there. When piping, however, the output disappears from your shell and you can't see what is going on. You can have it both ways by combining stdout and stderr and using the 'tee' utility:

.. code:: bash
    
    make 2>&1 | tee make.out