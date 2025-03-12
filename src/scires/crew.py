from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Scires():
    """Scires crew"""

    # YAML configuration files for agents and tasks
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Define agents
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst'],
            verbose=True
        )

    @agent
    def hypothesis_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['hypothesis_generator'],
            verbose=True
        )

    @agent
    def collaboration_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['collaboration_advisor'],
            verbose=True
        )

    # Define tasks
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            agent=self.research_analyst(),
            output_file='analysis_report.md'
        )

    @task
    def hypothesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['hypothesis_task'],
            agent=self.hypothesis_generator(),
            output_file='hypotheses.md'
        )

    @task
    def collaboration_task(self) -> Task:
        return Task(
            config=self.tasks_config['collaboration_task'],
            agent=self.collaboration_advisor(),
            output_file='collaboration_opportunities.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Scires crew"""
        return Crew(
            agents=[self.researcher(), self.research_analyst(), self.hypothesis_generator(), self.collaboration_advisor()],
            tasks=[self.research_task(), self.analysis_task(), self.hypothesis_task(), self.collaboration_task()],
            process=Process.sequential,
            verbose=True
        )