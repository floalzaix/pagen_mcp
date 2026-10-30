"""
    Dependency injection for the business logic layer.
"""

#
#   Imports
#

from contextlib import asynccontextmanager

# Perso

from dal.di import dal_lifespan

#
#   Lifespan
#

@asynccontextmanager
async def bll_lifespan():
    async with dal_lifespan() as dal_ls:
        yield dal_ls

#
#   Dependency Injection
#
