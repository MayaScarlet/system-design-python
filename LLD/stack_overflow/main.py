from typing import List
from question import Question, Tag
from users import Member
from abc import ABC


class StackOverflow(ABC):
    questions: List[Question] = []
    tags: List[Tag] = []
    users: List[Member] = []

    def search_question(self) -> List[Question]:
        ...

    def search_tag(self) -> List[Tag]:
        ...

    def search_user(self) -> List[Member]:
        ...
