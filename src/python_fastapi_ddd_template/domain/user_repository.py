from abc import ABC, abstractmethod
from typing import Optional
from .user_entity import User

class IUserRepository(ABC):

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        pass
