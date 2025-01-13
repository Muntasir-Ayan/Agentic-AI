
from phi.agent import Agent
import phi.api

from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.tools.website import WebsiteTools

import os
import phi
from phi.playground import Playground, serve_playground_app
# Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## WebSite agent
website_agent = Agent(
    name="Website AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[WebsiteTools()], 
    show_tool_calls=True)

multi_ai_agent=Agent(
    team=[web_search_agent,website_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[website_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)