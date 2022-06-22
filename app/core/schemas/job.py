from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class JobType(str, Enum):
    DELIVERY = "delivery"
    COLLECTION = "collection"


class Job(BaseModel):
    customer: str
    site: str
    due_date: datetime
    completed_at: datetime
    job_type: JobType
    late: bool
    flagged: bool
    num_of_items: int
