from typing import List, Text


class NoAgentFoundException(Exception):

    def __str__(self):
        return 'no agent found'


class Agent(object):

    def __init__(self, name, skills, load):
        self._name = name
        self._skills = skills
        self._load = load

    @property
    def name(self) -> str:
        return self._name

    @property
    def skills(self) -> list:
        return self._skills

    @property
    def load(self) -> int:
        return self._load

    @property
    def skill_set(self) -> set:
        return set(self._skills)

    def __str__(self):
        return f"<Agent: {self._name}>"


class Ticket(object):

    def __init__(self, id, restrictions):
        self._id = id
        self._restrictions = restrictions

    @property
    def restrictions(self):
        return self._restrictions

    @property
    def restrictions_set(self) -> set:
        return set(self._restrictions)


class FinderPolicy(object):

    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        '''
        one agent can handle maximum of three tickets
        '''
        return list(filter(lambda x: x.load < 3, agents))

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        filtered_agents = self._filter_loaded_agents(agents)
        if not filtered_agents:
            raise NoAgentFoundException()
        return sorted(filtered_agents, key=lambda x: x.load)[0]


class LeastFlexibleAgent(FinderPolicy):

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        '''
        sort agents by (len(x.skills), len(x.load))
        '''
        filtered_agents = sorted(self._filter_loaded_agents(agents), key=lambda x: (len(x.skills), x.load))
        for agent in filtered_agents:
            if ticket.restrictions_set.issubset(agent.skill_set):
                return agent
        else:
            raise NoAgentFoundException()


# Default Test Case

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2])) # B

least_flexible_policy = LeastFlexibleAgent()
print(least_flexible_policy.find(ticket, [agent1, agent2])) # A


# Empty Restrictions

print('restrictions 가 비어 있음')
ticket = Ticket(id="1", restrictions=[])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2])) # B

least_flexible_policy = LeastFlexibleAgent()
print(least_flexible_policy.find(ticket, [agent1, agent2])) # A


# skills 가 전부 비어 있는 경우

print('skills 전부 비어 있음')
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=[], load=2)
agent2 = Agent(name="B", skills=[], load=0)

try:
    least_loaded_policy = LeastLoadedAgent()
    print(least_loaded_policy.find(ticket, [agent1, agent2])) # B
except NoAgentFoundException as e:
    print(f'least loaded policy error: {e}')


try:
    least_flexible_policy = LeastFlexibleAgent()
    print(least_flexible_policy.find(ticket, [agent1, agent2])) # No Agents Found
except NoAgentFoundException as e:
    print(f'least flexible policy error: {e}')


# load 가 모두 꽉찬 경우

print('load 모두 꽉 참')
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=[], load=3)
agent2 = Agent(name="B", skills=[], load=3)

try:
    least_loaded_policy = LeastLoadedAgent()
    print(least_loaded_policy.find(ticket, [agent1, agent2])) # No Agents Found
except NoAgentFoundException as e:
    print(f'least loaded policy error: {e}')


try:
    least_flexible_policy = LeastFlexibleAgent()
    print(least_flexible_policy.find(ticket, [agent1, agent2])) # No Agents Found
except NoAgentFoundException as e:
    print(f'least flexible policy error: {e}')
