"""
    Main script of the MCP server of Pagen.
"""

#
#   Imports
#

from fastmcp import FastMCP

# Perso

from config import CONFIG
from api.di import api_lifespan

#
#   Main
#

def main():
    mcp = FastMCP(
        name=CONFIG["name"],
        version=CONFIG["version"],
        instructions=CONFIG["description"],
        lifespan=api_lifespan,
    )

    #
    #   Routes registration
    #


    
    #
    #   Run
    #
    
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()