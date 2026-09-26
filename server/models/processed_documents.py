from uuid import uuid4

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class ProcessedDocument(Base):
    __tablename__ = "processed_documents"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    document_id: Mapped[str] = mapped_column(
        ForeignKey("documents.id"),
        nullable=False,
        unique=True
    )

    document_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    keywords: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )