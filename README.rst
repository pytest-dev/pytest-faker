faker_ integration the pytest_ test runner
==========================================

.. image:: http://img.shields.io/travis/pytest-dev/pytest-faker.svg
   :target: https://travis-ci.org/pytest-dev/pytest-faker
.. image:: https://img.shields.io/pypi/pyversions/pytest-qt.svg
  :target: https://pypi.python.org/pypi/pytest-qt/   
.. image:: http://img.shields.io/pypi/v/pytest-faker.svg
   :target: https://pypi.python.org/pypi/pytest-faker
.. image:: http://img.shields.io/coveralls/pytest-dev/pytest-faker.svg
   :target: https://coveralls.io/r/pytest-dev/pytest-faker
.. image:: https://readthedocs.org/projects/pytest-faker/badge/?version=latest
    :target: https://readthedocs.org/projects/pytest-faker/?badge=latest
    :alt: Documentation Status

pytest-faker adds faker fixtures_ for easy use of faker_ for your tests under pytest_ runner.

.. _faker: http://www.joke2k.net/faker/
.. _pytest: http://pytest.org
.. _fixtures: https://pytest.org/latest/fixture.html

Install pytest-faker
-------------------------

::

    pip install pytest-faker

Example
-------

An example of faker_ and pytest_ integration.


tests/test_faker.py:

.. code-block:: python

    from faker.generator import Generator

    def test_faker(faker):
        """Faker factory is a fixture."""
        assert isinstance(faker, Generator)
        assert isinstance(faker.name(), str)


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_.

© 2015 Anatoly Bubenkov, Oleg Pidsadnyi and others
