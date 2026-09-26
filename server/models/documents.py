from enum import Enum
from uuid import uuid4

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class SourceEnum(str, Enum):
    MANUAL = "MANUAL"
    OUTLOOK = "OUTLOOK"
    GMAIL = "GMAIL"
    TELEGRAM = "TELEGRAM"
    WHATSAPP = "WHATSAPP"


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    connection_id: Mapped[str | None] = mapped_column(
        ForeignKey("connections.id"),
        nullable=True
    )

    source: Mapped[SourceEnum] = mapped_column(
        SQLEnum(SourceEnum),
        nullable=False
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )