from abc import ABC
from dataclasses import dataclass, field
from typing import List, Union
from constants import EmploymentType, InvitationStatus
from users import Member

import datetime
import uuid


@dataclass
class Message:
	sent_to: Member
	message_body: str
	media: list = None


@dataclass
class Comment:
	content: str
	author: Member
	comment_id: str = uuid.uuid1()
	created_at: str = datetime.datetime.today()
	votes: int = 0

	def upvote(self):
		self.votes += 1


@dataclass
class Post:
	author: Member
	shares: int = 0
	total_likes: int = 0
	caption: str = None
	comments: List[Comment] = field(default_factory=list, repr=False)

	def add_comment(self, comment: Comment):
		self.comments.append(comment)

	def like(self):
		self.total_likes += 1

	def share(self):
		...


@dataclass
class Group:
	group_id = uuid.uuid4()
	name: str
	description: str
	listed_group: bool
	members: list = field(default_factory=list, repr=None)
	admins: list = field(default_factory=list, repr=None)

	def add_member(self, member: Member):
		self.members.append(member)

	def update_description(self, description: str) -> None:
		self.description = description

	def toggle_group_status(self):
		self.listed_group = not self.listed_group

	def remove_members(self, member: Member) -> None:
		self.members.remove(member)


@dataclass
class Invitation:
	owner: Member
	invitee: Member
	invitation_status: InvitationStatus
	invitation_id: str = uuid.uuid4()
	created_at: str = datetime.datetime.today()


@dataclass
class Page:
	name: str
	tagline: str
	industry: str
	website: str
	logo: str
	location: str
	linkedin_address: str = None
	organization_size: int = None
	followers: int = None


@dataclass()
class OrganizationPage(Page):
	organization_type: str = None
	products: list = field(default_factory=list)
	jobs: list = field(default_factory=list)
	people: list = field(default_factory=list)
	events: list = field(default_factory=list)
	videos: list = field(default_factory=list)
	photos: list = field(default_factory=list)

	def __post_init__(self):
		super().__init__(
			self.name,
			self.tagline,
			self.industry,
			self.website,
			self.logo,
			self.location,
		)

	def update_logo(self, logo):
		...

	def add_photos(self, image):
		...

	def add_event(self, event):
		...

	def add_people(self, people: Member):
		...

	def add_product(self, product):
		...

	def add_job_post(self, post):
		...


@dataclass
class InstitutionalPage(Page):
	employees: int = 0
	jobs: list = None
	alumni: list = None

	def __post_init__(self):
		super().__init__(
			self.name,
			self.tagline,
			self.industry,
			self.website,
			self.logo,
			self.location
		)


@dataclass
class JobPosting:
	position = str
	description: str
	location: str
	employment_type: EmploymentType
	created_on: str
	active_until: str
	applicants: int = 0
	date_of_posting: str = datetime.datetime.today()

	def save_job(self, member: Member):
		...


@dataclass
class Notification:
	message: int
	timestamp: str
	entity: Union[Page, Member] = None

	def send_notifications(self):
		...


class Search(ABC):
	def search_member(self, member):
		...

	def search_organization(self, query):
		...

	def search_group(self, group):
		...

	def search_title(self, query):
		...


def main():
	...


if __name__ == '__main__':
	main()
