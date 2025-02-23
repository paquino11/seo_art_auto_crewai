from crewai.tools import BaseTool
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()

# Define the Google Trends Tool
class GoogleTrendsTool(BaseTool):
    name: str = "Google Trends"
    description: str = "Fetches trending search data from Google Trends."
    api_wrapper: GoogleTrendsAPIWrapper = Field(default_factory=GoogleTrendsAPIWrapper)

    def _run(self, query: str) -> str:
        """Execute the Google Trends query and return results."""
        try:
            tool = GoogleTrendsQueryRun(api_wrapper=self.api_wrapper)
            result = tool.run(query)
            if not result or result == "":
                # If no results, try with more specific parameters
                trends = self.api_wrapper.build_payload(
                    [query], 
                    timeframe='today 12-m',  # Last 12 months
                    geo='',  # Worldwide
                )
                return str(trends)
            return result
        except Exception as e:
            return f"Error fetching Google Trends data: {str(e)}"

if __name__ == "__main__":
    # Create an instance of the tool
    trends_tool = GoogleTrendsTool()
    
    # Test with a single, simple query first
    test_query = "bitcoin"
    print(f"\nSearching for: {test_query}")
    result = trends_tool.run(test_query)
    print(f"Results:\n{result}")
