"""pytest-faker plugin."""
import pytest

from faker import Factory


@pytest.fixture
def faker_locale():
    """Faker locale.

    None by default which means faker's default locale.
    """
    return None


@pytest.fixture
def faker(faker_locale):
    return Factory.create(faker_locale)
