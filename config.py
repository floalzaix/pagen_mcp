"""
    Basic config parameters for the application.
"""

CONFIG = {
    "name": "Pagen",
    "version": "0.1",
    "description": """
        Pagen is a tool for managing html templates for llms.

        It uses a database to store the templates their sections
        and their activation. It then offers a way to export the
        completed template as a pdf file.

        For the llm it is a way to generate the html template
        following some specific rules. Then saved to the database
        and modified by the other tools.
    """,
    "database_url": "sqlite+aiosqlite:///data/database.db",
}