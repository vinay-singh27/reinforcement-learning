import numpy as np

class Agent():
    
    def __init__(self, eps=0.1, gamma=0.99):

        self.Q = {}
        