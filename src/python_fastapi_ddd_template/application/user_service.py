from ..domain.user_entity import User
from ..domain.user_repository import IUserRepository

class UserService:

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str) -> User:
        existing_user = self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists.")
        
        new_user = User(name=name, email=email)
        return self.user_repository.save(new_user)
