import gym
from agent import Agent

if __name__ == '__main__':

    # instantiate the environment
    env = gym.make("Blackjack-v1")
    agent = Agent()
    n_episodes = 500000
    for i in range(n_episodes):
        if i % 50000 == 0:
            print(f"starting episode: {i}")
        observations = env.reset()
        done = False
        while not done:
            action = agent.policy(observations)
            observations_, reward, done, info = env.step(action)
            agent.memory.append((observations, reward))
            observations = observations_
        agent.update_V()
    print(agent.V[(21, 3, True)])
    print(agent.V[(4, 1, False)])
