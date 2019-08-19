import gym
from gym import spaces
import numpy as np


class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    symbols = ['O', ' ', 'X'];

    def __init__(self):
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Dict({"observation": spaces.Box(low=0.0,high=1.0,shape=(9,)), "on_move": spaces.Box(low=-1,high=1.0,shape=(1,))})
    def step(self, action):
        done = False
        reward = 0

        square = action
        
        # check move legality
        board = self.state['board']
        om = self.state['on_move']
        proposed = board[square]

        print('Board', board)
        print('Player Move', om)
        print('Action', square)
        
        if (proposed != 0):  # wrong player, not empty
            print("illegal move ", action, ". (square occupied): ", square)
            done = True
            reward = -100 
        else:
            board[square] = om 
            self.state['on_move'] = -om

        # check game over
        for i in range(3):
            # horizontals and verticals
            if ((board[i * 3] == om and board[i * 3 + 1] == om and board[i * 3 + 2] ==om)
                or (board[i + 0] == om and board[i + 3] == om and board[i + 6] == om)):
                reward = 100
                done = True
                break
        # diagonals
        if((board[0] == om and board[4] == om and board[8] == om)
            or (board[2] == om and board[4] == om and board[6] == om)):
                reward = 100
                done = True
        
        print('New State', self.state)
        print('Reward', reward)
        print('Done', done)
        return self.state, reward, done, {}
    def reset(self):
        self.state = {}
        self.state['board'] = np.zeros(shape = (9,), dtype=float)
        self.state['on_move'] = 1.0
        return self.state
    def render(self, mode='human', close=False):
        if close:
            return
        print("on move: " , self.symbols[self.state['on_move']+1])
        for i in range (9):
            print (self.symbols[self.state['board'][i]+1], end=" ");
            if ((i % 3) == 2):
                print();
