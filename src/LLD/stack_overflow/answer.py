import datetime
from users import Member
from meta import Votes, Flag


class Answer:
    def __init__(self, content, member: Member):
        self.content = content
        self.member = member
        self.accepted = False
        self.created_at = datetime.datetime.now()
        self.votes = Votes()
        self.flag = Flag()
