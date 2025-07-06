'''
Tarea 4: The boggle game
Juan Pablo Ovalles Ceron
8971870

Input
The input file will include a few data sets. Each data set will be a pair of boards as shown in the sample input. All entries
will be upper case letters. Two consecutive entries on same board will be separated by one blank. The first row in the first
board will be on the same line as the first row of the second board. They will be separated by four spaces, the same will
hold for the remaining 3 rows. Board pairs will be separated by a blank line. The file will be terminated by ‘#’.
The input must be read from standard input.
Output
For each pair of boggle boards, output an alphabetically-sorted list of all common words, each word on a separate line; or
the statement ‘There are no common words for this pair of boggle boards.’.
Separate the output for each pair of boggle boards with a blank line.
The output must be written to standard output.
'''

from sys import stdin

def main():
    global board1, board2, commonLetters, words1, words2
    line = stdin.readline().strip()
    board1 = [[None for _ in range(4)] for _ in range(4)]
    board2 = [[None for _ in range(4)] for _ in range(4)]
    while line != '#':
        board1set = set(); board2set = set()    # conjuntos que guardan las letras de cada tablero
        words1 = set(); words2 = set()          # words1 guarda las palabras encontradas en la primera busqueda
        
        for i in range(4):
            line = line.split()
            j = 0
            for l in line[0:4]: board1[i][j] = l; j+=1; board1set.add(l)
            j = 0
            for l in line[4:8]: board2[i][j] = l; j+=1; board2set.add(l)
            if i != 3: line = stdin.readline().strip()
        
        commonLetters = board1set.intersection(board2set)   # contiene las letras en comun de los tableros
        
        # Se busca en el primer tablero todas las palabras validas formadas por las letras en comun entre los tableros
        for i in range(4):
            for j in range(4):
                vis = [[False for _ in range(4)] for _ in range(4)]
                solveBoard(i,j,[], vis, 0, 1, board1)

        # si se encontraron palabras habrá que buscarlas en el segundo tablero, sino se puede responder no hay palabras en comun
        if len(words1) != 0:
            # se hace la busqueda de palabras en comun en el tablero 2
            for i in range(4):
                for j in range(4):
                    vis = [[False for _ in range(4)] for _ in range(4)]
                    solveBoard(i,j,[], vis, 0, 2, board2)
            if len(words2) != 0:
                ans = list(words2)
                ans.sort()
                for w in ans: print(w)
            else: print("There are no common words for this pair of boggle boards.")
        else:
            print("There are no common words for this pair of boggle boards.")
        
        line = stdin.readline().strip()
        line = stdin.readline().strip()
        if line != "#": print()

movX = [0,1,0,-1,1,-1,-1,1]
movY = [1,0,-1,0,1,-1,1,-1]

# el parametro mode ayuda a saber si se esta haciendo la primera o segunda busqueda
# ya que en el caso inductivo hacen lo mismo pero en el caso base no.
# Los valores para este parametro son 1 y 2, para indicar la respectiva busqueda
def solveBoard(i,j, word, vis, vowels, mode, b):
    global words1, words2
    if len(word) == 4:
        opc = ''.join(word)
        if mode == 1: words1.add(opc)
        else:
            if opc in words1: words2.add(opc)
    else:
        for k in range(8):
            if check(word, i, j, vis, vowels, b):
                vowel = isVowel(b[i][j])
                if vowel: vowels+=1
                newX = j+movX[k]; newY = i+movY[k]
                word.append(b[i][j]); vis[i][j] = True
                
                solveBoard(newY, newX, word, vis, vowels,mode,b)
                
                if vowel: vowels-=1
                word.pop(); vis[i][j] = False
                
                
def check(word, i, j, vis, vowels, b):
    if i >= 0 and j >= 0 and i < 4 and j < 4 and not vis[i][j] and b[i][j] in commonLetters:
        vowel = isVowel(b[i][j])
        if (vowels == 2 and vowel) or (len(word)-vowels == 2 and not vowel): ans = False
        else: ans = True
    else: ans = False
    return ans


def isVowel(letter):
    ans = letter in "AEIOUY"
    return ans


main()

