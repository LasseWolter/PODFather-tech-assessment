from fastapi import Depends
from app.core.db import get_db
from sqlalchemy.orm import Session
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
import csv

# from sqlalchemy.orm import Session

from app.core.schemas import JobCreate, JobType
from app.core.models import Job

router = APIRouter()

all_jobs: List[JobCreate] = []
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
        job = JobCreate.parse_obj(job_dict)
        all_jobs.append(job)


@router.get("/", response_model=List[JobCreate])
def get_all(job_id: str) -> Any:
    """
    Retrieve items.
    """
    return all_jobs


@router.post("/")
def create_job(job: JobCreate, db: Session = Depends(get_db)) -> Any:
    """
    Create new job items.
    """
    print(job)
    new_job: Job = Job(customer=job.customer, site=job.site, due_date=job.due_date,
                       completed_at=job.completed_at, late=job.late, flagged=job.flagged, num_of_items=job.num_of_items)
    db.create_all()
    print(new_job)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return job
