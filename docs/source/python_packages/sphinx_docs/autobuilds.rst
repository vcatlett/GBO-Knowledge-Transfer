.. _autobuilds:

*****************
Sphinx Autobuilds
*****************

Package Version
===============

I've encountered issues with the current latest version of `sphinx-autobuild` (2024.10.3) where it does not detect new changes. Freezing the version to 2021.3.14 does the trick. To install it within an existing environment, do the following:

.. code:: bash

    $ pip install sphinx-autobuild==2023.14


Setting Up Sphinx Autobuilds
============================

Here are the steps to set up Sphinx autobuilds so that you can check your documentation edits live.

1. First, activate your environment

.. code-block:: bash

    $ source $VENV_HOME/{{VENV_NAME}}/bin/activate

2. Now, run the autobuild command. The docs will be published at `http://127.0.0.1:8000/`.

.. code-block:: bash

    (venv) $ sphinx-autobuild docs/source docs/_build

3. If you would like the docs to publish at a specific host and port, such as `http://thales:9876`, then add the appropriate flags:

.. code-block:: bash

    (venv) $ sphinx-autobuild docs/source docs/_build --host thales --port 9876

4. You may now make changes in the `docs/` directory and see the live changes at the appropriate URL in your browser. 

5. To shut down the server, simply `CTRL+C`.