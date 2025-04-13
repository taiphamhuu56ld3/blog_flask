from enum import Enum
from typing import List


class Status(Enum):
    ACTIVE = "active"  # Account is active
    INACTIVE = "inactive"  # Account is disabled
    BANNED = "banned"  # Account is permanently banned
    PENDING = "pending"  # Account is pending confirmation
    ADMIN = "admin"  # Admin can access all pages
    USER = "user"  # Regular user
    GUEST = "guest"  # Guest (not registered)

# Check access rights


def has_access(user_status: Status, required_status: List[Status]):
    return user_status in required_status
