'''
Tarea 1: Starting school
Juan Pablo Ovalles Ceron
8971870

The idea is very simple. Roll number should be unique and a student should get the smallest roll number that has not been
assigned yet to any of the students. For example if K = 4, total number of students are 10 and the first K students roll
numbers are 1, 3, 5, 10 then the next 6 roll numbers should be 2, 4, 6, 7, 8 and 9.
Though this is a very good idea, the teacher got mad at Po. So she starts asking the roll number for various students. As
there are many students, Po is feeling helpless. Can you help Po?

Input
First line will contain an integer T (T ≥ 0), the number of test cases. Each case will start with three integers N (0 < N ≤ 109),
K (0 < K ≤ 50 000, and K ≤ N), and Q (0 < Q ≤ 50 000): N is the total number of students, K is described earlier, and Q
is the number of queries of the crazy teacher. Next line will contain K distinct integers, the first K roll number assigned
by the teacher. These values will be between 1 and 109

(inclusive). Next will be Q integers, each indicating a position of

students. These values will be between 1 and N (inclusive).
The input must be read from standard input.

Output
For each case print one line ‘Case T:’ where T is the case number. Then for each query print one line with the roll number
of the student standing on the queried position. See sample I/O for clarity.
The output must be written to standard output.
'''
import time
from sys import stdin

def main():
    global numbers
    cases = int(stdin.readline())
    it = 1
    for i in range(cases):
        N, K, Q = list(map(int, stdin.readline().split()))
        numbers = [int(num) for num in stdin.readline().split()]
        numbersCopy = [num for num in numbers]
        numbers.sort()

        print("Case %d:" %it); it += 1
        queries = [int(num) for num in stdin.readline().split()]
        for querie in queries:
            # Si el querie esta dentro de los primeros K's asignados basta con consultarlo en la lista
            if querie <= len(numbers): print(numbersCopy[querie-1])
            # Si el querie es mayor que el maximo de la lista K, el valor estara fuera de la mezcla de los numeros
            # entonces basta con entregar el querie
            elif querie > numbers[-1]: print(querie)
            else: print(binarySearch(querie))


def binarySearch(querie):
    lo = 0
    hi = len(numbers)
    mid = (hi+lo)//2
    gap = querie-len(numbers)-1
    # si el primer numero es 1 o la cantidad de numeros sin asignar
    # menores al primero es menor a los asignados antes del querie hay que hacer busqueda
    if numbers[0] == 1 or numbers[0]-1 <= gap:
        while hi-lo > 1:
            mid = (hi+lo)//2
            # Operacion para saber cuantos numeros sin asignar hay antes
            # de numbers[mid]
            disp = numbers[mid]-mid-1
            if gap < disp: hi = mid
            else: lo = mid
        return numbers[lo]+(gap+1-(numbers[lo]-lo-1))
    # si la cantidad de numeros sin asignadar antes del primer numero K
    # cubre al querie simplemente se asigna el gap+1 (pensando que el 1 no es el primero en los K)
    else: return gap+1
main()
