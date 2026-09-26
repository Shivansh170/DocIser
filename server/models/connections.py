from enum import Enum
from uuid import uuid4

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class ProviderEnum(str, Enum):
    OUTLOOK = "OUTLOOK"
    GMAIL = "GMAIL"
    TELEGRAM = "TELEGRAM"
    WHATSAPP = "WHATSAPP"


class Connection(Base):
    __tablename__ = "connections"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    provider: Mapped[ProviderEnum] = mapped_column(
        SQLEnum(ProviderEnum),
        nullable=False
    )

    access_token: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    refresh_token: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )