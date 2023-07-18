import gym
from agent import Agent 


if __name__ == '__main__':

    # create an env
    env = gym.make("Blackjack-v1")
    agent = Agent(gamma=0.99)
    n_episodes = 500000

    # run the episodes 
    for i in range(n_episodes):
        # for debugging
        if i % 50000 == 0:
            print(f"Starting epsiode {i}")
        # reset the env
        observation = env.reset()
        # print(observation)
        total, _, _ = observation
        done = False
        # run the episode
        if not done:
            action = agent.policy(observation)
            observation_, reward, done, info = env.step(action)
            agent.memory.append((observation_, reward))
            observation = observation_
        # update the state value once the episode terminates 
        agent.update_V()

    # check the state-value function 
    print(agent.V[(21,3,True)])
    print(agent.V[(4,1,False)])


