Faker_ integration with the pytest_ test runner
===============================================

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

pytest-faker adds Faker fixtures_ for easy use of Faker_ for your tests under pytest_ runner.

.. _Faker: https://faker.readthedocs.io/
.. _pytest: http://pytest.org/
.. _fixtures: https://pytest.org/latest/fixture.html

Install pytest-faker
--------------------

::

    pip install pytest-faker

Example
-------

An example of Faker_ and pytest_ integration.


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
