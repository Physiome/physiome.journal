physiome.journal
================

The Physiome Journal support package.

Installation and usage
----------------------

For the mean time, install the package inside a Python virtualenv with
the following commands:

.. code:: console

    $ git clone https://github.com/journal/physiome.journal.git
    $ cd physiome.journal
    $ pip install -e .
    $ python setup.py build  # to build the artifacts

Start the demo server simply by

.. code:: console

    $ python -m repodono.model.demo.flask_standalone journal.toml
