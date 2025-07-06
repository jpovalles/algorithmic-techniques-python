'''
Tarea 4: Maze
Juan Pablo Ovalles Ceron
8971870

The maze has only one entry which is at (0, 0) and only one exit which is at (N − 1, N − 1). From each block you can move
in four directions (N, E, W, S) and the cost is 1 for each movement among the maze but collecting treasure does not require
any cost. Some blocks contain treasures that you will have to collect. Suppose there are T treasures in the maze and you
have to collect at least S (S ≤ T) treasures from them. In this problem, you are requested to find an optimal way from
starting location to ending location and take at least S treasures from the maze. Remember that, you can visit a block more
than once if you want.

Input
The first line of the input contains three integers N (N ≤ 30), T (T ≤ 30) and S (S ≤ 10 and S ≤ T) describing the
dimension of the maze, number of treasures in the maze and number of treasures that you can take. After that, there are T
lines. Each line contains two numbers representing the position of the treasure in the maze. The input may contain multiple
test cases and ends with three zeros for N, T and S .
The input must be read from standard input.

Output
Each test case produces one line of output. This line should contain the output serial no as shown in the sample output and
a number representing the minimum cost which is required to collect the treasures.
The output must be written to standard output.
'''

from sys import stdin

import time

def main():
    line = stdin.readline().strip()
    cases = 1
    while line != '0 0 0':
        global T, N, S, tre, mini
        N, T, S = [int(x) for x in line.split()]
        tre = [(0,0)]
        for i in range(T):
            r, c = [int(x) for x in stdin.readline().split()]
            tre.append((r,c))
        tre.sort()
        vis = [False for _ in range(T+1)]
        
        mini = float("inf")
        solve(0, 0, 0, vis)
        print("Case %d: %d" %(cases, mini))
        cases += 1
        line = stdin.readline().strip()


def solve(curr, acc, count, vis):
    global mini
    row = tre[curr][0]; col = tre[curr][1]
    if count == S:
        acc += abs(N-1-row) + abs(N-1-col)
        mini = min(mini, acc)
    else:
        for i in range(1, len(tre)):
            rowN = tre[i][0]; colN = tre[i][1]
            distCurr = acc + abs(rowN-row) + abs(colN-col)
            distGoal = distCurr + abs(N-1-rowN) + abs(N-1-colN)
            if not vis[i] and distGoal < mini and distCurr < mini:
                acc = distCurr; count += 1; vis[i] = True
                solve(i, acc, count, vis)
                acc -= abs(rowN-row) + abs(colN-col); count -= 1; vis[i] = False

main()

