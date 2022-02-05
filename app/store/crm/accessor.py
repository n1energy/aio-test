from typing import Optional
import typing

from app.crm.models import User

if typing.TYPE_CHECKING:
    from app.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Optional[Application] = None

    async def connect(self, app: "Application"):
        self.app = app
        try:
            self.app.database["users"]
        except KeyError:
            self.app.database["users"] = []
        print("connect to database")

    async def disconnect(self, _: "Application"):
        self.app = None
        print("disconnect to database")
    
    async def add_user(self, user: User):
        self.app.database['users'].append(user)
