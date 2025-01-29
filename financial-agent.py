from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()
Groq.api_key = os.getenv("GROQ_API_KEY")

web_search_agent = Agent(
    name="web_search_agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    teams= [web_search_agent, financial_agent],
    instructions=["always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendations which share i should buy, openai or NVDA", stream=True)



