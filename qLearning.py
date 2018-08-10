import numpy as np

from gridWorld import GridWorld


class QLearning(object):
    '''

    '''
    def __init__(self, m, n):
        '''

        '''
        self.env = GridWorld(m, n)
        self.q = self.init_q()
        self.current = [1, 0]
        self.gamma = 0.9

    def init_q(self):
        '''

        :return:
        '''
        q = dict()
        for i in range(self.env.grid.shape[0]):
            q[i] = {}
            for j in range(self.env.grid.shape[1]):
                q[i][j] = {}
                for a in self.env.actions:
                    q[i][j][a] = 0
        return q

    def learn(self):
        '''

        :return:
        '''
        for i in range(500):
            a = np.random.choice(self.env.actions.__len__(), 1)[0]
            next, reward = self.env.step(self.current, a)
            self.q[self.current[0]][self.current[1]][a] = reward + self.gamma*max(self.q[next[0]][next[1]].values())
            self.current = next


ql = QLearning(2, 3)
ql.learn()
for row in ql.q:
    for col in ql.q[row]:
        x = ql.q[row][col]
        a = max(x, key=x.get)
        print(row, col, ' : ', a)
