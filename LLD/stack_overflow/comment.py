import datetime
from users import Member


class Comment:
    def __init__(self, content: str, user: Member):
        self.content = content
        self.user = user
        self.created_at = datetime.datetime.now()
        self.votes = 0

    def update_comment(self, content: str, user_id: int) -> None:
        ...

    def delete_comment(self, user_id: int) -> None:
        ...
