from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.postgres import PostgresTools

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="localhost",
    port=5532,
    db_name="ai",
    user="ai", 
    password="ai",

)

# Initialize Agent with Gemini model
agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    tools=[postgres_tools]
)

agent.print_response("""
Please run a SQL query to get all users from the users table 
who signed up in the last 30 days
""")