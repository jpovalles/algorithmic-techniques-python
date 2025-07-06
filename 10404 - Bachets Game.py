'''
Tarea 2: Batchet's Game
Juan Pablo Ovalles Ceron
8971870

Bachet’s game is probably known to all but probably not by this name. Initially there
are n stones on the table. There are two players Stan and Ollie, who move alternately. 
Stan always starts. The legal moves consist in removing at least one but not more than 
k stones from the table. The winner is the one to take the last stone. Here we consider 
a variation of this game. The number of stones that can be removed in a single move must 
be a member of a certain set of m numbers. Among the m numbers there is always 1 and thus the game never stalls.

Input
The input consists of a number of lines. Each line describes one game by a sequence of positive numbers.
The first number is n ≤ 1000000 the number of stones on the table; the second number is m ≤ 10
giving the number of numbers that follow; the last m numbers on the line specify how many stones can
be removed from the table in a single move.

Output
For each line of input, output one line saying either ‘Stan wins’ or ‘Ollie wins’ assuming that both
of them play perfectly.
'''

from sys import stdin

rocks = list()

def main():
    global mov, rocks
    line = stdin.readline()
    while line != '':
        line = [int(i) for i in line.split()]
        r = line[0]
        rocks = [False for _ in range(r+1)]
        mov = line[2:]
        for m in mov: rocks[m] = True
        if process(r): print("Stan wins")
        else: print("Ollie wins")
        line = stdin.readline()
        


def process(r):
    for i in range(1, r+1):
        if i not in mov:
            for k in mov:
                if i-k>=0 and not rocks[i-k]:
                    rocks[i] = True
                    break
    return rocks[r]

main()
