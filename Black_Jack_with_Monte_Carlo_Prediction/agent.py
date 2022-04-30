import numpy as np


class Agent:

    def __init__(self, gamma=0.99):

        self.V = {}
        self.sum_space = [i for i in range(4, 22)]
        self.dealer_show_card = [i+1 for i in range(10)]
        self.ace_space = [True, False]
        self.action_space = [0, 1]  # hit or stick

        self.state_space = []
        self.returns = {}
        self.state_visited = {}  # first visit or not
        self.memory = []
        self.gamma = gamma

        self.init_vals()

    def init_vals(self):

        for total in self.sum_space:
            for card in self.dealer_show_card:
                for ace in self.ace_space:
                    self.V[(total, card, ace)] = 0
                    self.returns[(total, card, ace)] = []
                    self.state_visited[(total, card, ace)] = 0
                    self.state_space.append((total, card, ace))

    @staticmethod
    def policy(state):

        total, _, _ = state
        action = 0 if total >= 20 else 1

        return action

    def update_V(self):

        for idt, (state, _) in enumerate(self.memory):
            G = 0
            if self.state_visited[state] == 0:
                self.state_visited[state] += 1
                discount = 1
                for t, (_, reward) in enumerate(self.memory[idt:]):
                    G += reward * discount
                    discount *= self.gamma
                    self.returns[state].append(G)

        for state, _ in self.memory:
            self.V[state] = np.mean(self.returns[state])

        for state in self.state_space:
            self.state_visited[state] = 0

        self.memory = []




