'''
Tarea 4: Triple-Free Binary Strings
Juan Pablo Ovalles Ceron
8971870

A binary string consists of ones and zeros. Given a binary string T, if there is no binary string S such that S S S (concatenate
three copies of S together) is a substring of T, we say T is triple-free.
A pattern consists of ones, zeros and asterisks, where an asterisk (∗) can be replaced by either one or zero. For example, the
pattern 0 ∗ ∗1 contains strings 0001, 0011, 0101, 0111, but not 1001 or 0000.
Given a pattern P, how many triple-free binary strings does it contain?

Input
Each line of the input represents a test case, which contains the length of pattern, n (0 < n < 31), and the pattern P. There
can be maximum 35 test cases.
The input terminates when n = 0.
The input must be read from standard input.

Output
For each test case, print the case number and the answer, shown below.
The output must be written to standard output.
'''

from sys import stdin

def main():
    global n, p, count
    line = stdin.readline().strip()
    cases = 1
    while line != '0':
        n, p = line.split()
        n = int(n)

        count = 0
        solve(0, [])
        print("Case %d: %d" %(cases, count))
        cases += 1
        
        line = stdin.readline().strip()


def solve(i, sol):
    global count
    if i == n:
        count += 1
    else:
        if len(sol) < 2:
            if p[i] != '*':
                sol.append(p[i])
                solve(i+1, sol)
                sol.pop()
            else:
                for c in ['0', '1']:
                    sol.append(c)
                    solve(i+1, sol)
                    sol.pop()
        else:
            if p[i] != '*':
                if check(sol, p[i]):
                    sol.append(p[i])
                    solve(i+1, sol)
                    sol.pop()
            else:
                for c in ['0', '1']:
                    if check(sol, c):
                        sol.append(c)
                        solve(i+1, sol)
                        sol.pop()

def check(sol, car):
    sol.append(car)
    revs = len(sol)//3
    
    i = 1
    flag = False
    cad = ''.join(sol[len(sol)-revs*3:len(sol)])
    while i <= revs and not flag:
        base = len(cad) - 3 *i
        a, b, c = base+i, base+i*2, base+i*3
        
        flag = cad[base:a] == cad[a:b] and cad[base:a] == cad[b:c] and cad[a:b] == cad[b:c]
        i+=1
    sol.pop()
    return not flag


main()