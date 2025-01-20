from phi.agent import Agent
# from phi.model.openai import OpenAIChat
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.postgres import PgAgentStorage
import os
from dotenv import load_dotenv
load_dotenv()
agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    storage=PgAgentStorage(table_name="agent_sessions", db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
agent.print_response("Which country are we speaking about?")
