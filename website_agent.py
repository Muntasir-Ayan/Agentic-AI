from phi.agent import Agent
from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
# import openai

import os
from dotenv import load_dotenv
load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")

## web search agent
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

multi_ai_agent.print_response("Search the web page and generate an overview: 'https://thecatapi.com/'", markdown=True)
