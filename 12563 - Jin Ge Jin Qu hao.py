'''
Tarea 2: Jin Ge Jin Qu Hao
Juan Pablo Ovalles Ceron
8971870

There is one very popular song called Jin Ge Jin Qu(). It is a mix of 37 songs, and is extremely
long (11 minutes and 18 seconds) — I know that there are Jin Ge Jin Qu II and III, and some other
unofficial versions. But in this problem please forget about them.
Why is it popular? Suppose you have only 15 seconds left (until your time is up), then you should
select another song as soon as possible, because the KTV will not crudely stop a song before it ends
(people will get frustrated if it does so!). If you select a 2-minute song, you actually get 105 extra
seconds! ....and if you select Jin Ge Jin Qu, you’ll get 663 extra seconds!!!
Now that you still have some time, but you’d like to make a plan now. You should stick to the
following rules:
• Don’t sing a song more than once (including Jin Ge Jin Qu).
• For each song of length t, either sing it for exactly t seconds, or don’t sing it at all.
• When a song is finished, always immediately start a new song.
Your goal is simple: sing as many songs as possible, and leave KTV as late as possible (since we
have rule 3, this also maximizes the total lengths of all songs we sing) when there are ties.
Input
The first line contains the number of test cases T (T ≤ 100). Each test case begins with two positive
integers n, t (1 ≤ n ≤ 50, 1 ≤ t ≤ 109
), the number of candidate songs (BESIDES Jin Ge Jin Qu)
and the time left (in seconds). The next line contains n positive integers, the lengths of each song, in
seconds. Each length will be less than 3 minutes — I know that most songs are longer than 3 minutes.
But don’t forget that we could manually “cut” the song after we feel satisfied, before the song ends.
So here “length” actually means “length of the part that we want to sing”.
It is guaranteed that the sum of lengths of all songs (including Jin Ge Jin Qu) will be strictly larger
than t.
Output
For each test case, print the maximum number of songs (including Jin Ge Jin Qu), and the total lengths
of songs that you’ll sing.
'''
from sys import stdin

JIN = 678


def main():
    global c, R
    cases = int(stdin.readline())
    for i in range(cases):
        n, c = [int(x) for x in stdin.readline().split()]
        R = [int(x) for x in stdin.readline().split()]
        memo = dict()
        ans = phi_mem(len(R), c, memo)
        print("Case %d: %d %d" %(i+1, ans[1]+1, ans[0]+JIN))

def phi_mem(n, c, memo):
    dur, cant, k = None, None, (n,c)
    if k in memo:
        dur, cant = memo[k]
    else:
        if n == 0:
            dur = 0; cant = 0
        elif n != 0 and R[n-1] > c-1:
            dur, cant = phi_mem(n-1, c, memo)
        else:
            dur1, cant1 = phi_mem(n-1, c, memo)
            dur2, cant2 = phi_mem(n-1, c-R[n-1], memo)
            dur2 += R[n-1]
            cant2 += 1
            
            if cant1!=cant2:
                if cant1>cant2: dur, cant = dur1, cant1
                else: dur, cant = dur2, cant2
            else:
                if dur1>dur2: dur, cant = dur1, cant1
                else: dur, cant = dur2, cant2
            
        memo[(n,c)] = (dur, cant)
    return dur, cant
main()
