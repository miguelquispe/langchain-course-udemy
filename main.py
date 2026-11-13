import os
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openrouter import ChatOpenRouter
from langchain_tavily import TavilySearch
# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool
# def search(query:str) -> str:
#     """
#     Tool that searches over internetb
#     Args:
#         query (str): The search query
#     Returns:
#         str: The search results
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)



llm = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    openrouter_api_key=os.environ.get("OPENROUTER_API_KEY")
)
tools = [TavilySearch()] #[search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course-udemy!")
    result = agent.invoke({
        "messages": HumanMessage(content="Search for 3 job postings for an frontend developer in Lima, Perú as remote work on linkedin and list their details")
    })
    print(result)


if __name__ == "__main__":
    main()

# PROMPTS
"""
Search for 3 job postings for an full stack developer in Lima, Perú as remote work on linkedin and list their details
"""

