from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
import csv

# from sqlalchemy.orm import Session

from app.core.schemas import Job, JobType

router = APIRouter()

all_jobs: List[Job] = []
# Create in-memory version of data
with open("pod-data.csv") as f:
    for row in csv.DictReader(f):
        # TODO: create proper parsing here
        # Manual parsing
        job_vals = [v for k, v in row.items()]
        job_keys = [
            "customer",
            "site",
            "due_date",
            "completed_at",
            "job_type",
            "late",
            "flagged",
            "num_of_items",
        ]
        job_dict = dict(zip(job_keys, job_vals))
        job_dict["job_type"] = JobType.DELIVERY  # hardcoded
        job = Job.parse_obj(job_dict)
        all_jobs.append(job)


@router.get("/", response_model=List[Job])
def read_items() -> Any:
    """
    Retrieve items.
    """
    return all_jobs
