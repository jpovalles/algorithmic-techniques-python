'''
Tarea 3: Painting tool
Juan Pablo Ovalles

Maybe you wonder what an annoying painting tool is? First of all, the painting tool we speak of supports only black and
white. Therefore, a picture consists of a rectangular area of pixels, which are either black or white. Second, there is only
one operation how to change the colour of pixels:
Select a rectangular area of r rows and c columns of pixels, which is completely inside the picture. As a result of the
operation, each pixel inside the selected rectangle changes its colour (from black to white, or from white to black).
Initially, all pixels are white. To create a picture, the operation described above can be applied several times. Can you paint
a certain picture which you have in mind?

Input
The input contains several test cases. Each test case starts with one line containing four integers n, m, r and c. (1 ≤ r ≤ n ≤
100, 1 ≤ c ≤ m ≤ 100), The following n lines each describe one row of pixels of the painting you want to create. The i-th
line consists of m characters describing the desired pixel values of the i-th row in the finished painting (’0’ indicates white,
’1’ indicates black).
The last test case is followed by a line containing four zeros.
The input must be read from standard input.

Output
For each test case, print the minimum number of operations needed to create the painting, or ’-1’ if it is impossible.
The output must be written to standard output.
'''

from sys import stdin

def main():
    global canva, ref
    init = stdin.readline()
    while init != "0 0 0 0":
        n, m, r, c = [int(x) for x in init.split()]
        canva = [[0 for _ in range(m)] for _ in range(n)]
        ref = list()
        for i in range(n):
            ref.append(stdin.readline().strip())
        print(solve(n, m, r, c))
        init = stdin.readline().strip()


def solve(n,m, r, c):
    flag = True
    i = 0
    ans = 0
    while i < n and flag:
        j = 0
        while j < m and flag:
            if canva[i][j] != int(ref[i][j]):
                if n-i >= r and m-j >= c: change(i, j, r, c); ans+=1;
                else: flag = False; ans = -1
            j+=1
        i+=1
    return ans

def prove():
    for line in canva: print(line)
    for line in ref: print(line)
    print()

def change(i, j, r, c):
    for x in range(r):
        for y in range(c):
            canva[i+x][j+y] = 1-canva[i+x][j+y]
main()
