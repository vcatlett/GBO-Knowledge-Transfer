***********************
1. Create a Sparrow Env
***********************

This is largely taken from sparrow's JenkinsFile. Please cross-reference that to make sure you are using the most up to date conventions

Setting up your sandbox
=======================

Development should take place in the developer's `/home/sandboxes/${USER}` area. The process for checking out, and building the M&C source code can be adapted from the steps included in `GB.Knowledge.CreatingNewMCVersion <https://safe.nrao.edu/wiki/bin/view/GB/Knowledge/CreatingNewMCVersion>`_.

Get the repo from git
=====================

.. code:: bash

    cd /home/sandboxes/${USER}
    mkdir mc
    cd mc
    git clone /home/gbt2/git/integration-bare/sparrow

Make the repo following the JenkinsFile
=======================================

.. code:: bash

    cd sparrow
    mkdir sparrow
    shopt -s dotglob nullglob extglob
    mv !(sparrow|jenkins-sparrow-env) sparrow
    cd sparrow
    ln -s admin/linux-gcc.mak config.mak
    cp sparrow.venv.bash.do_not_source ../sparrow.bash
    mkdir ../bin ../app ../daemon ../include ../i386-linux ../i386-linux/lib ../x86_64-linux ../x86_64-linux/lib

Make the venv
=============

.. code:: bash

    cd ..
    ./sparrow/createSparrowEnv jenkins-sparrow-env
    ln -s jenkins-sparrow-env sparrow_venv

Run a make on the repo
======================

.. code:: bash

    export YGOR_ROOT='/home/gbt1/integration/ygor'
    export GB_ROOT='/home/gbt1/integration/gb'
    source $YGOR_ROOT/ygor.bash
    source sparrow.bash
    source sparrow_venv/bin/activate
    cd sparrow
    make -j8

Install the repo as monctrl
===========================
.. code:: bash

    ssh monctrl@galileo
    cd /home/sandboxes/${USER}/mc/sparrow
    export YGOR_ROOT='/home/gbt1/integration/ygor'
    export GB_ROOT='/home/gbt1/integration/gb'
    source $YGOR_ROOT/ygor.bash
    source sparrow.bash
    source sparrow_venv/bin/activate
    cd sparrow
    make install -j8

Check that it all works via unit tests, back in your own user account
=====================================================================

.. code:: bash
    
    ssh ${USER}@galileo
    cd /home/sandboxes/${USER}/mc/sparrow
    export YGOR_ROOT='/home/gbt1/integration/ygor'
    export GB_ROOT='/home/gbt1/integration/gb'