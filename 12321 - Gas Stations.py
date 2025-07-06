'''
Tarea 3: Gas station
Juan Pablo Ovalles Ceron
8971870

Input
The input consists of several test cases. The first line of each test case contains two integer numbers L and G (separated by
a blank), representing the length of the road and the number of gas stations, respectively (1 ≤ L ≤ 108

, 1 ≤ G ≤ 104
). Each

one of the next G lines contains two integer numbers xi and ri (separated by a blank) where xi

is the location and ri
is the
radius of coverage of the i-th gas station (0 ≤ xi ≤ L, 0 < ri ≤ L). The last test case is followed by a line containing two
zeros.
The input must be read from standard input.
Output
For each test case, print a line with the maximum number of gas stations that can be eliminated, so that every point on the
road belongs to the area of influence of some not closed station. If some point on the road is not covered by any of the
initial G gas stations, print ‘-1’ as the answer for such a case
The output must be written to standard output.
'''

from sys import stdin

def main():
    line = stdin.readline().strip()
    while line != "0 0":
        L, S = [int(x) for x in line.split()]
        A = []
        for _ in range(S):
            x, r = [int(x) for x in stdin.readline().split()]
            limL = x-r; limR = x+r
            if limL < 0: limL = 0
            if limR > L: limR = L
            A.append((limL, limR))

        ans = solve(A, 0, L)
        if ans != -1: print(S-ans)
        else: print(ans)
            
        line = stdin.readline().strip()

def solve(A, L, H):
    A.sort()
    ans, ok, = 0, True
    n, N, l = 0, len(A), L

    while n<N and l<H and ok:
        if A[n][0] > l: ok = False

        best, n = n, n+1
        while ok and n<N and A[n][0] <= l:
            if A[n][1] > A[best][1]: best = n
            n+=1
        l = A[best][1]
        ans +=1
    if not ok or l<H: ans = -1
    return ans
main()
