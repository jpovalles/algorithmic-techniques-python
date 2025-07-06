'''
Tarea 4: Y2K Accounting bug
Juan Pablo Ovalles Ceron
8971870

Accounting for Computer Machinists (ACM) has sufferred from the Y2K bug and lost some vital data for preparing annual
report for MS Inc.
All what they remember is that MS Inc. posted a surplus or a deficit each month of 1999 and each month when MS Inc.
posted surplus, the amount of surplus was s and each month when MS Inc. posted deficit, the deficit was d. They do not
remember which or how many months posted surplus or deficit. MS Inc., unlike other companies, posts their earnings for
each consecutive 5 months during a year. ACM knows that each of these 8 postings reported a deficit but they do not know
how much. The chief accountant is almost sure that MS Inc. was about to post surplus for the entire year of 1999. Almost
but not quite.
Write a program, which decides whether MS Inc. suffered a deficit during 1999, or if a surplus for 1999 was possible, what
is the maximum amount of surplus that they can post.

Input
Input is a sequence of lines, each containing two positive integers s and d.
The input must be read from standard input.

Output
For each line of input, output one line containing either a single integer giving the amount of surplus for the entire year, or
output ‘Deficit’ if it is impossible.
The output must be written to standard output.
'''

from sys import stdin

def main():
    global s, d, sol, opc, maxi
    line = stdin.readline()
    while line != "":
        opc = [int(x) for x in line.split()]
        opc[1] *= -1
        sol = [None for _ in range(12)]
        maxi = float("-inf")
        phi(sol, 0)
        if maxi < 0: print("Deficit")
        else: print(maxi)
        line = stdin.readline()

def phi(sol, n):
    global maxi
    if n == len(sol):
        ans = list(sol)
        maxi = max(maxi, sum(ans))
    else:
        for op in opc:
            if n < 4 or (sum(sol[n-4:n])+op < 0 and sum(sol[n-4:n])+op >= opc[1]):
                sol[n] = op
                phi(sol, n+1)
                sol[n] = None
    
main()
