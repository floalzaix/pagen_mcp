"""
    Creates the database if needed and provide a session
    to interact with the database.

    If the database is sqlite then it creates the file
    if needed.
"""

#
#   Imports
#

from pathlib import Path
from typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
    create_async_engine
)

# Perso

from config import CONFIG

#
#   DatabaseSession
#

_session_factory: Optional[async_sessionmaker[AsyncSession]] = None

def create_engine() -> AsyncEngine:
    global _session_factory

    database_url = CONFIG["database_url"]

    # If the database is sqlite, create the file if needed.
    if database_url.startswith("sqlite"):
        database_path = Path(database_url.split(":///")[1])
        database_path.parent.mkdir(parents=True, exist_ok=True)

    engine = create_async_engine(database_url)
    _session_factory = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    return engine

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    global _session_factory

    if _session_factory is None:
        raise RuntimeError("Session factory not initialized")

    async with _session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise