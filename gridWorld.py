import numpy as np


class GridWorld(object):
    '''

    '''
    def __init__(self, m, n):
        '''

        '''
        self.grid = np.empty(shape=(m, n))
        self.goal = np.array([0, n-1])
        self.actions = {0: [0, 1],      # right
                        1: [0, -1],     # left
                        2: [-1, 0],     # up
                        3: [1, 0],      # down
                        4: [0, 0]}      # stay

    def reward(self, src, dst):
        '''

        :param src:
        :param dst:
        :return:
        '''
        if self.is_goal(src) and self.is_goal(dst):
            return 100
        if self.is_goal(src):
            return 0
        if self.is_goal(dst):
            return 100
        return 0

    def step(self, src, a):
        '''

        :param src:
        :param action:
        :return:
        '''
        dst = np.array(src) + self.actions[a]
        if dst[0] == -1 or dst[1] == -1 or dst[0] == self.grid.shape[0] or dst[1] == self.grid.shape[1]:
            return src, 0
        return dst, self.reward(src, dst)

    def is_goal(self, dst):
        '''

        :param dst:
        :return:
        '''
        return dst[0] == self.goal[0] and dst[1] == self.goal[1]
