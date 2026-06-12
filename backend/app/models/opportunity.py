import enum
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Enum, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OpportunityStatus(str, enum.Enum):
    NEW = "new"
    ACTIVE = "active"
    CLOSED = "closed"


class Opportunity(Base):
    __tablename__ = "opportunities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    asking_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    estimated_value: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    opportunity_score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    status: Mapped[OpportunityStatus] = mapped_column(
        Enum(OpportunityStatus, native_enum=False, length=20),
        nullable=False,
        default=OpportunityStatus.NEW,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
