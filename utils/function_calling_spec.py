from utils.database_functions import database_schema_string

# Specify function descriptions for OpenAI function calling 
functions = [
    {
        "name": "ask_postgres_database",
        "description": "Use this function to answer user questions about the database. Output should be a fully formed SQL query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": f""" The SQL query that extracts the information that answers the user's question from the Postgres database. Write the SQL in the following schema structure:
                            {database_schema_string}. Write the query in SQL format only, not in JSON. Do not include any line breaks or characters that cannot be executed in Postgres.  
                            """,
                }
            },
            "required": ["query"],
        },
    }
]
