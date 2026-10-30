"""
    Handles the the dependcy injection of the dal
    (Data Access Layer) of the application.
"""

#
#   Imports
#

from typing import Annotated
from fastmcp.dependencies import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

# Perso

from dal.session import get_session, create_engine

#
#   Lifespan
#

@asynccontextmanager
async def dal_lifespan():
    engine = create_engine()
    
    try:
        yield
    finally:
        await engine.dispose()

#
#   Dependency Injection
#

def get_db_session(
    db_session: Annotated[AsyncSession, Depends(get_session)],
) -> AsyncSession:
    return db_session