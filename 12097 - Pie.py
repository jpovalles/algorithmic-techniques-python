'''
Tarea 1: Pie
Juan Pablo Ovalles Ceron
8971870

My friends are very annoying and if one of them gets a bigger piece than the others, they start complaining. Therefore all
of them should get equally sized (but not necessarily equally shaped) pieces, even if this leads to some pie getting spoiled
(which is better than spoiling the party). Of course, I want a piece of pie for myself too, and that piece should also be of the
same size.
What is the largest possible piece size all of us can get? All the pies are cylindrical in shape and they all have the same
height 1, but the radii of the pies can be different.

Input
The first line contains a positive integer indicating the number of test cases. Each testcase comprises two lines. The first
line contains integers N and F (1 ≤ N, F ≤ 10 000) indicating the number of pies and the number of friends. The second
line contains N integers ri (1 ≤ ri ≤ 10 000) defining the radii of the pies.
The input must be read from standard input.

Output
For each test case, output one line with the largest possible volume V such that me and my friends can all get a pie piece of
size V. The answer should be given as a floating point number with exactly 4 decimal places and absolute error of at most
10−6
.
The output must be written to standard output.
'''
from sys import stdin
from math import pi

E = 10e-7

def isOkay(mid):
    cont = 0; i = 0
    while cont<F and i < N:
        cont += V[i]//mid
        i+=1
    return cont >= F

def main():
    global N, F, V
    cases = int(stdin.readline())
    for i in range(cases):
        N, F = map(int, stdin.readline().split())
        F += 1
        V = [int(radius)**2*pi for radius in stdin.readline().split()]
        V.sort()
        print("{:.4f}".format(bisection()))

def bisection():
    lo = 0
    hi = V[-1]+2*E
    while hi-lo >= E:
        mid = (lo + hi) / 2
        if isOkay(mid): lo = mid
        else: hi = mid
    return lo
main()
