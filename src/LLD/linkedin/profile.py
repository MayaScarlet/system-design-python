from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Experience:
	title: str
	employment_type: str
	company_name: str
	currently_working: bool = False
	location: str = None
	start_date: str = None
	end_date: Optional[str] = None
	description: str = None
	profile_headline: str = None
	skills: list = field(default_factory=list, repr=True)
	media: list = field(default_factory=list, repr=True)


@dataclass
class Education:
	school: str
	degree: str
	field_of_study: str
	grade: str = None
	description: str = None
	start_date: str = None
	end_date: Optional[str] = None


@dataclass
class Stats:
	views: int
	search_count: int
	connections: int


@dataclass
class Profile:
	stats: Stats
	tagline: str = None
	cover: str = None
	views: int = field(default_factory=int)
	skills: list[str] = field(default_factory=list, repr=True)
	interests: defaultdict[list] = field(default_factory=list, repr=True)
	education: List[Education] = field(default_factory=list, repr=True)
	experience: List[Experience] = field(default_factory=list, repr=True)

	def add_experience(self, experience: Experience) -> None:
		self.experience.append(experience)

	def remove_experience(self, experience: Experience) -> None:
		self.experience.remove(experience)

	def add_education(self, education: Education) -> None:
		self.education.append(education)

	def remove_education(self, education: Education) -> None:
		self.education.remove(education)

	def add_skill(self, skill: str) -> None:
		self.skills.append(skill)

	def add_interests(self, interest_type: str, interest) -> None:
		self.interests[interest_type].append(interest)


def main():
	profile = Profile("Some tagline here", "Image here")
	experience = Experience("Developer", "Full time", "UNI")
	profile.add_experience(experience)
	print(profile)


if __name__ == '__main__':
	main()
