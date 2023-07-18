from typing import List
import random

class Environment:

    def __init__(self) -> None:
        self.steps_left = 10

    def get_observation(self) -> List[float]:
        """
        This function returns the environment observation
        state
        """

        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> List[int]:
        """
        List of possible actions in the env
        """
        return [0, 1]
    
    def is_done(self) -> bool: 
        """
        Returns if the envionment has reached
        to the terminal state
        """
        return self.steps_left == 0
    
    def action(self, action : int) -> float:
        """
        Performs the agent's action and returns
        the reward
        """
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random() 
        

class Agent:

    def __init__(self) -> None:
        self.total_reward = 0.0

    def step(self, env : Environment) :
       current_obs = env.get_observation()
       actions = env.get_actions()
       reward = env.action(random.choice(actions))
       self.total_reward += reward  


if __name__ == "__main__":
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)
        
    print(f"Total Reward : {agent.total_reward}")

