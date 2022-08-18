# Member can add comment to question or answer
# Member can upvote a question, answer or comment
# Member can flag a question, comment or answer


class Votes:
	def __init__(self):
		self.__votes = set()
		self.vote_count = 0

	def upvote(self, member_id: int) -> None:
		if member_id not in self.__votes:
			self.__votes.add(member_id)
			self.vote_count += 1

	def downvote(self, member_id: int) -> None:
		if member_id in self.__votes:
			self.__votes.remove(member_id)
			self.vote_count -= 1


class Flag:
	def __init__(self):
		self.__flagged_by = set()
		self.flag_count = 0

	def flag(self, member_id: int) -> None:
		if member_id not in self.__flagged_by:
			self.__flagged_by.add(member_id)
			self.flag_count += 1

	def unflag(self, member_id: int) -> None:
		if member_id in self.__flagged_by:
			self.__flagged_by.remove(member_id)
			self.flag_count -= 1
