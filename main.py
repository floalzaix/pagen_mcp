"""
    Main script of the MCP server of Pagen.
"""

#
#   Imports
#

from mcp.server import MCPServer

# Perso



#
#   Main
#

def main():
    mcp = MCPServer()

    #
    #   Routes registration
    #

    
    
    #
    #   Run
    #
    
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()