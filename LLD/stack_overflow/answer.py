import datetime
from users import Member


class Answer:
    def __init__(self, content, member: Member):
        self.content = content
        self.member = member
        self.accepted = False
        self.created_at = datetime.datetime.now()
        self.votes = 0
