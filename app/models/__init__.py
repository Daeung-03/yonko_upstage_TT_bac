from app.models.enums import (
    TermDomain, TermStatus, ClauseType,
    EventType, NotificationStatus, MessageRole
)
from app.models.user import User
from app.models.term import Term, TermVersion, TermChunk, TermClause
from app.models.calendar import CalendarEvent, Notification
from app.models.chat import ChatSession, ChatMessage