import uuid
@dataclass
class User:
    _id: uuid.UUID
    email: str