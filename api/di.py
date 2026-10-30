"""
    Dependency injection for the API layer.
"""

#
#   Imports
#

from fastmcp.server.lifespan import lifespan
from fastmcp import FastMCP

# Person

from bll.di import bll_lifespan

#
#   Lifespan
#

@lifespan
async def api_lifespan(server: FastMCP):
    async with bll_lifespan() as bll_ls:
        yield bll_ls

#
#   Dependency Injection
#