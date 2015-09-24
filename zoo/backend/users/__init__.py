from ..wrappers import BaseService

from .models import UserDb


class UserService(BaseService):

    def __init__(self, *args, **kwargs):
        super(UserService, self).__init__(*args, **kwargs)

    def me(self):
        rv = UserDb(name='kanat', email='abc@abc', password='42')
        return rv

    def create(self, name=None, email=None, password=None):
        return UserDb(name=name, email=email, password=password)
