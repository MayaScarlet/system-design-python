from dataclasses import dataclass, field


@dataclass
class Player:
	name: str
	is_white: bool = False
	pieces_killed: list = field(default_factory=list, repr=False)
