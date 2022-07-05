from sqlalchemy import Column, Integer, String, Boolean, Date, Enum

from app.core.models import Base
from app.core.schemas import JobType


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, nullable=False)
    site = Column(String, nullable=False)
    due_date = Column(Date)
    completed_at = Column(Date)
    job_type = Column(Enum(JobType))
    late = Column(Boolean)
    flagged = Column(Boolean)
    num_of_items = Column(Integer)
