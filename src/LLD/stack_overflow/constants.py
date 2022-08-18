from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 1
    DEACTIVATED = 2
    CLOSED = 3
    BLOCKED = 4
    BLACKLISTED = 5


class QuestionStatus(Enum):
    OPEN = 1
    CLOSE = 2
    ON_HOLD = 3
    DELETED = 4
    FLAGGED = 5
    HAS_BOUNTY = 6


class QuestionClosingRemark(Enum):
    DUPLICATE = 1
    OFF_TOPIC = 2
    TOO_BROAD = 3
    NOT_CONSTRUCTIVE = 4
    NOT_A_REAL_QUESTION = 5
    OPINION_BASED = 6
