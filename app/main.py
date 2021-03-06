from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db.session import engine
from app.core.models import Base


from app.core.config import settings
from v1.api import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(api_router)
create_tables()
