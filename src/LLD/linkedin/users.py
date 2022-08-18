import datetime
from dataclasses import dataclass, field
from typing import List

from constants import AccountStatus
from profile import Profile
from main import Group, Invitation, Message


@dataclass
class Account:
	id: int
	password: str
	email: str
	created_at = datetime.datetime.today()
	status: str = AccountStatus.ACTIVE


@dataclass
class Member(Profile):
	first_name: str
	last_name: str
	phone: str = None
	summary: str = None
	posts: list = None
	pending_invites: List['Invitation'] = field(default_factory=list, repr=False)
	connected_members: List['Member'] = field(default_factory=list, repr=False)
	connected_groups: List['Group'] = field(default_factory=list, repr=False)
	saved_jobs: list = field(default_factory=list, repr=False)

	def send_message(self, message: 'Message'):
		...

	def create_post(self, post):
		...

	def send_connection_invite(self, invitation):
		...

	def recommend(self, member_id, page):
		...
