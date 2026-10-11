from dataclasses import dataclass


@dataclass
class Ticket:
    id: int
    title: str
    description: str
    category: str
    urgency: str
    affected_users: int
    priority: str
    status: str = "open"
    assigned_to: str | None = None
