from pytest_factoryboy import register

from tests.factories import AdFactory, CategoryFactory, UserFactory

pytest_plugins = "tests.fixtures"

# Factories
register(AdFactory)
register(CategoryFactory)
register(UserFactory)
