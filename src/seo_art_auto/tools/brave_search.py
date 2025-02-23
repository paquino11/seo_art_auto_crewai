from crewai.tools import BaseTool
from langchain_community.tools import BraveSearch
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()

class BraveSearchTool(BaseTool):
    name: str = "Brave Search"
    description: str = "Searches the web using Brave Search API."
    api_key: str = Field(default_factory=lambda: os.getenv("BRAVE_API_KEY"))
    
    def _run(self, query: str) -> str:
        """Execute the Brave Search query and return results."""
        try:
            tool = BraveSearch.from_api_key(
                api_key=self.api_key, 
                search_kwargs={"count": 3}
            )
            result = tool.run(query)
            return result
        except Exception as e:
            return f"Error fetching Brave Search results: {str(e)}"

if __name__ == "__main__":
    # Create an instance of the tool
    search_tool = BraveSearchTool()
    
    # Test with a single, simple query
    test_query = "bitcoin"
    print(f"\nSearching for: {test_query}")
    result = search_tool.run(test_query)
    print(f"Results:\n{result}")
