
#src/seo_art_auto/main.py
import sys
import warnings

from datetime import datetime

from seo_art_auto.crew import SeoArtAuto

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'website': 'https://www.fast-resume-ai.com/',
        'current_year': str(datetime.now().year)
    }
    
    try:
        SeoArtAuto().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

