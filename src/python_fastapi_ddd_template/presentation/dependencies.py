from ..application.user_service import UserService
from ..infrastructure.dynamodb_user_repository import DynamoDBUserRepository

def get_user_service() -> UserService:
    user_repository = DynamoDBUserRepository()
    return UserService(user_repository)
