#src/seo_art_auto/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from .tools.google_trends_tool import GoogleTrendsTool
from .tools.brave_search import BraveSearchTool
from crewai_tools import DallETool

@CrewBase
class SeoArtAuto():
	"""SeoArtAuto crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	scrape_website_tool = ScrapeWebsiteTool()
	google_trends_tool = GoogleTrendsTool()
	dall_e_tool = DallETool()

	@agent
	def website_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['website_analyzer'],
			verbose=True,
			tools=[self.scrape_website_tool]
		)

	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			verbose=True
		)

	@agent
	def seo_trend_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_trend_researcher'],
			verbose=True,
			tools=[self.google_trends_tool]
		)

	@agent
	def seo_image_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_image_generator'],
			verbose=True,
			tools=[self.dall_e_tool]
		)
	@agent
	def seo_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_writer'],
			verbose=True
		)

	@task
	def website_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_analysis_task'],
		)

	@task
	def content_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_strategy_task'],
		)

	@task
	def seo_trend_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_trend_task'],
		)
	
	@task
	def seo_image_generator_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_image_generator_task'],
		)

	@task
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
			output_file='output/article.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SeoArtAuto crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
