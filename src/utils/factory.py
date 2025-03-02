import factory
from src.model.db_schemas import UserModel


class UserFactory(factory.Factory):
    class Meta:
        model = UserModel
    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'@{obj.password}123')
