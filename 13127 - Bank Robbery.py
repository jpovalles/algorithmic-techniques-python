'''
Tarea 3: Bank robbery
Juan Pablo Ovalles Ceron
8971870
'''

from sys import stdin
from heapq import heappush,heappop
from collections import deque

INF = float("inf")

def main():
    global G
    line = stdin.readline()
    while line != "":
        n, m, b, p = [int(x) for x in line.split()]
        G = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = [int(x) for x in stdin.readline().split()]
            G[u].append((v, w))
            G[v].append((u, w))
        banks = [int(x) for x in stdin.readline().split()]

        if p == 0:
            ans = banks; dist = "*"
        else:
            stations = [int(x) for x in stdin.readline().split()]
            rsp = dijkstraMod(G, stations)

            # banksDist extrae las distancias minimas para llegar de una estacion a cada banco
            banksDist = list()
            for b in banks:
                banksDist.append(rsp[b])
            dist = max(banksDist)   # la maxima distancia para llegar a un banco

            ans = list()
            # Cada banco que cumpla esa distancia va a estar en la solucion
            for b in banks:
                if rsp[b] == dist: ans.append(b)

            if dist == float("inf"): dist = "*"
        ans.sort()
        print(len(ans), dist)
        print(*ans)
        line = stdin.readline()


def dijkstraMod(G, s):
  dist = [ INF ]*len(G)
  pqueue = list()
  for station in s:
      dist[station] = 0
      heappush(pqueue, (dist[station], station))
  pred = [-1] * len(G)
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    if dist[u] == du:
      for v,duv in G[u]:
        if du+duv<dist[v]:
          dist[v] = du+duv
          pred[v] = u
          heappush(pqueue, (dist[v], v))
  return dist

main()
        
