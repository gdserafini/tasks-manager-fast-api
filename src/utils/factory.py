import factory
from src.model.db_schemas import UserModel, TaskModel 
from src.model.task import TaskStateEnum
import factory.fuzzy


class UserFactory(factory.Factory):
    class Meta:
        model = UserModel
    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'@{obj.password}123')


class TaskFactory(factory.Factory):
    class Meta:
        model = TaskModel
    title = factory.Faker('text')
    description = factory.Faker('text')
    state = factory.fuzzy.FuzzyChoice(TaskStateEnum)
    user_id = 1
