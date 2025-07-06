'''
Tarea 3: Antimonotonicity
Juan Pablo Ovalles Ceron
8971870

I have a sequence Fred of length n comprised of integers between 1 and n inclusive. The elements of Fred are pairwise
distinct. I want to find a subsequence Mary of Fred that is as long as possible and has the property that:
Mary[0] > Mary[1] < Mary[2] > Mary[3] < . . .

Input
The first line of input will contain a single integer T expressed in decimal with no leading zeroes. T test cases will follow.
Each test case is contained on a single line. A line describing a test case is formatted as follows:
n Fred[0] Fred[1] Fred[2] . . . Fred[n − 1]
where n and each element of Fred is an integer expressed in decimal with no leading zeroes. No line will have leading
or trailing whitespace, and two adjacent integers on the same line will be separated by a single space. n will be at most
50000.
The input must be read from standard input.

Output
For each test case, output a single integer followed by a newline — the length of the longest subsequence Mary of Fred
with the desired properties.
The output must be written to standard output.
'''

from sys import stdin

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        nums = [int(x) for x in stdin.readline().split()]
        nums = nums[1:]
        print(solve(nums))

def solve(nums):
    it = 0
    for i in range(len(nums)-1):
        if it%2==0 and nums[i] > nums[i+1]: it+=1
        elif it%2==1 and nums[i] < nums[i+1]: it+=1
    return it+1

main()

