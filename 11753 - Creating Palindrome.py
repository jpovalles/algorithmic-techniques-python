'''
Parcial 2: Creating Palindrome
Juan Pablo Ovalles Ceron
8971870

Input
Input will start with an integer T (1 ≤ T ≤ 100), number of test cases. Each test case starts with
two integers N (1 ≤ N ≤ 10000) and K (0 ≤ K ≤ 20), the length of integer sequence and maximum
allowed difficulty.
Output
For each test case, output a single line of the form ‘Case X: D’. Here X is the case number. If the
given sequence is already a palindromic sequence D will be ‘Too easy’ without quotes, if the difficulty
of the given sequence is greater than K, D will be ‘Too difficult’, other wise D will be the difficulty
of the given sequence. See the sample input and output for exact format.

'''

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)


def main():
    global nums, mini, N, K
    cases = int(stdin.readline())
    i = 0
    while i < cases:
        
        N, K = [int(x) for x in stdin.readline().split()]
        nums = stdin.readline().split()

        mini = float("inf")


        solve(0, len(nums)-1, 0)
        

        i += 1

        if mini > K: print("Case %d: Too difficult" %(i))
        elif mini == 0: print("Case %d: Too easy" %(i))
        else: print("Case %d: %d" %(i, mini))
        
        


def solve(i, j, count):
    global mini
    if i > j:
        mini = min(mini, count)
    else:
        if count <= K and count < mini:            
            if nums[i] == nums[j]:
                solve(i+1,j-1, count)
            else:
                if nums[i] == nums[j-1] and nums[i+1] != nums[j]:
                    solve(i,j-1, count+1)
                elif nums[i+1] == nums[j] and nums[i] != nums[j-1]:
                    solve(i+1,j, count+1)
                else:
                    solve(i+1,j, count+1)
                    solve(i,j-1, count+1)
            
main()
