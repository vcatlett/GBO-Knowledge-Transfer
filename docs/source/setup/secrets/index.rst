.. _secrets:

*******
Secrets
*******

General
=======

We rely heavily on file-based secrets. That means that we also heavily rely on Linux file permissions in order to protect secrets. When creating a secrets file, you should first set your umask to ``umask u=rwx,go=`` (``077``). This prevents anyone else from reading your secrets file. For certain groups (``monctrl``, ``gbosdd``, ``dss``, etc. -- any of the GBOSDD group accounts), group-readable files are also permissible. But you should *never* allow "broad" groups like ``gbstaff`` to read secrets!.

``umask`` can be confusing at first. See https://wintelguy.com/umask-calc.pl for a simple calculator if you are unsure. And of course you should check the actual permissions of the files you create before writing to them.

Application Development
=======================

When developing applications, we often need to store secrets. However, you should **never** put secrets into a file that is tracked in a repository! This exposes it to anyone who clones the repo.

If you have *committed* but not *pushed* a secret, things can still be salvaged: just amend the commit before you push. If you have accidentally pushed a secret, or you discover a secret that has already been pushed, **contact your division head**! The affected secrets will need to be changed, and then removed from version control to prevent it from happening again.

For Python projects we are commonly using `env files <https://pypi.org/project/python-dotenv/>`_


.. warning:: You should **never** put secrets into a file that is tracked in a repository!

Password Vault
==============

Currently GBOSDD maintains a KeePass vault at ``~gbosdd/gbosdd.kdbx``. It can be opened by anyone in the ``gbosdd`` group via: ``keepassx2  ~gbosdd/gbosdd.kdbx  --keyfile ~gbosdd/.gbosdd.key``. Note that ``~gbosdd/gbosdd.kdbx.lock`` will also need to be kept group-writeable, or you won't be able to save (unless you're the ``gbosdd`` user)

This stores a variety of passwords: databases, mailing lists, etc. that everyone in the group should have access to.

PostreSQL
=========

The best place to keep your Postgres passwords is in ``~/.pgpass`` (https://www.postgresql.org/docs/9.6/libpq-pgpass.html).

For many Python projects we are now use `env files <https://pypi.org/project/python-dotenv/>`_; these are also an appropriate place to store passwords.

.. note:: Remember to set your umask before creating this file!

MySQL/MariaDB
=============

There is no equivalent to ``~/.pgpass`` in (our ancient version of) MariaDB. However, you can create per-database config files that look like this:

.. code-block:: ini

    [client]
    user=<username>
    password=<password>

Then use this via ``$ mysql --defaults-file=~/.something.cnf -h some_host some_db``

This will supply a default user and password (which can be overriden at the command-line), without leaking into the process name or your shell history.

.. note:: Remember to set your umask before creating these files!

In the future, hopefully we can use more modern password management features, e.g. https://dev.mysql.com/doc/refman/8.0/en/password-security-user.html

