import datetime
from abc import ABC


class Comment(ABC):
    def __init__(self, content: str, user_id: int):
        self.content = content
        self.user_id = user_id
        self.created_at = datetime.datetime.now()
        self.__votes = set()
        self.__flagged_by = set()
        self.votes = 0
        self.flag = 0

    def upvote(self, member_id: int):
        if member_id not in self.__votes:
            self.__votes.add(member_id)
            self.votes += 1

    def flag(self, member_id: int):
        if member_id not in self.__flagged_by:
            self.__flagged_by.add(member_id)
            self.flag += 1


class QuestionComment(Comment):
    ...


class AnswerComment(Comment):
    ...


def main():
    q = QuestionComment("Question comment", 1)
    for i in range(2, 10):
        q.upvote(i)
    print(q.votes)


if __name__ == '__main__':
    main()
