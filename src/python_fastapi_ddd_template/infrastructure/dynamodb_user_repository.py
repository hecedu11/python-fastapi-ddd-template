import boto3
from typing import Optional
from ..domain.user_entity import User
from ..domain.user_repository import IUserRepository
from .config import settings

class DynamoDBUserRepository(IUserRepository):

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name=settings.aws_region)
        self.table = self.dynamodb.Table(settings.dynamodb_table_name)

    def get_by_id(self, user_id: str) -> Optional[User]:
        response = self.table.get_item(Key={'user_id': user_id})
        item = response.get('Item')
        return User(**item) if item else None

    def get_by_email(self, email: str) -> Optional[User]:
        # This requires a Global Secondary Index (GSI) on the 'email' attribute
        response = self.table.query(
            IndexName='email-index',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={':email': email}
        )
        items = response.get('Items')
        return User(**items[0]) if items else None

    def save(self, user: User) -> User:
        self.table.put_item(Item=user.model_dump())
        return user

    def delete(self, user_id: str) -> bool:
        self.table.delete_item(Key={'user_id': user_id})
        return True
