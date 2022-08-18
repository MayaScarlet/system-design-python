from constants import AccountStatus


class Account:
    def __init__(
            self, account_id: int, first_name: str, last_name: str,
            email: str, password: str, status=AccountStatus.ACTIVE
    ) -> None:
        self.id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.account_status = status
        self.reputation = 0
        self.location = None

    def reset_password(self) -> None:
        ...

    def update_location(self, location) -> None:
        ...

    def deactivate(self) -> None:
        ...

    def delete_account(self) -> None:
        ...


class Member:
    def __init__(self, account: Account):
        self.__account = account
        self.badges = []
        self.questions_asked = []
        self.bookmarks = []
        self.followed_posts = []

    def get_reputation(self) -> int:
        return self.__account.reputation

    def add_question(self, question) -> None:
        self.questions_asked.append(question)

    def bookmark_question(self, question) -> None:
        self.bookmarks.append(question)

    def follow_post(self, post) -> None:
        self.followed_posts.append(post)


class Admin(Member):
    def __init__(self, account: Account):
        super().__init__(account)

    def block_member(self, member):
        ...

    def unblock_member(self, member):
        ...


class Moderator(Member):
    def __init__(self, account: Account):
        super().__init__(account)

    def close_question(self, question):
        ...

    def reopen_question(self, question):
        ...
