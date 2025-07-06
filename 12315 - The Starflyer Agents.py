'''
Project: The starflyer agents
Juan Pablo Ovalles Ceron
8971870

'''

from sys import stdin

def occurs(hash1, hash2):
    '''
    Verifica si el hash1 aparece en el hash2, esto para evitar sustituciones ciclicas

    Args:
        hash1 (str): variable a buscar
        hash2 (str o list): hash donde se quiere buscar la variable

    Return;
        boolean: hash1 aparece en hash2

    Complejidad temporal:
    Siendo n la cantidad de hashes en hash2, es decir, cualquier constante, variable o función que ocurra en el hash hash2.
    La complejidad temporal será O(n) esto considerando el peor de los casos donde la variable que estoy buscando
    ocurre en el último lugar de una variable en la estructura, si es así habré recorrido todos los hashes antes de encontrarla

    Complejidad espacial:
    O(1) ya que no se crea una estructura nueva para realizar esto, solo se recorren las que se pasan por parámetro.
    '''
    ans = False
    if type(hash2) == str:
        ans = hash1 == hash2
    else:
        # si el hash2 es una funcion tengo que revisar si hash1 ocurre
        # en algun argumento del hash2
        args = hash2[1]
        i = 0
        while i < len(args) and not ans:
            ans = occurs(hash1, args[i])
            i +=1
    return ans

def process(string):
    stack = []  
    name = ""
    hashe = []  
    for s in string:
        
        if s.isalnum(): 
            name = ''.join((name,s))
        elif s == '(':
            if name != "":
                nextArg = [name, []]  
                if stack:
                    stack[-1][1].append(nextArg)  
                else:
                    hashe = nextArg  
                stack.append(nextArg)  
                name = ""
        else:
            if name != "":
                stack[-1][1].append(name)
                name = ""
            if s == ')':
                stack.pop()
    
    if not hashe: hashe = name
    return hashe


def replace(hash1, sust):
    '''
    Aplica una serie de sustituciones a todas las variables en un hash.
    Si es necesario se hace de manera recursiva hasta que no se pueda sustituir más.

    Args:
        hash1 (list or str): Puede ser una cadena (variable o constante) o una lista
                            que representa a una funcion de la forma [nombreFuncion, listaArgumentos]
        sust (dict): diccionario de sustituciones donde las claves son variables y el valor sus sustituciones

    Returns:
        ans (str o list): El hash con todas las sustituciones aplicadas en sus variables
        
    Complejidad temporal:
    La función recorre todos los n hashes(cadena o lista) que ocurren en hash1, en el peor caso se tiene que hash1 sea una funcion y todos sus argumentos sean variables
    ademas que cada variable aplique todas las m sustituciones en sust para llegar a su forma final entonces se tiene O(n*m), donde por cada variable se aplican m sustituciones
    Complejidad espacial:
    Para cada caso se reemplazará un hash por una versión de igual o mayor tamaño entonces la complejidad espacial es de Ω(n) para n la cantidad de hashes en la entrada.

    '''
    # si el hash de entrada es una variable busco su cambio en el diccionario de sustituciones
    if type(hash1) == str:
        if hash1[0].isupper() and hash1 in sust:
            # Si hay una sustitucion para el valor nuevo, tambien se hace
            ans = replace(sust[hash1], sust)
            sust[hash1] = ans   # se "relaja" la sustitucion
        else:
            # En este caso hash1 es constante o no esta en el diccionario de sustitucion
            ans = hash1
    else:
        name = hash1[0]
        args = hash1[1]
        newArgs = list()
        # si el hash dado es una funcion busco sustituir cada uno de sus argumentos, sin perder la estructura de la funcion
        for arg in args:
            new = replace(arg, sust)
            newArgs.append(new)
        ans = [name, newArgs]
    return ans

def compatible(hash1, hash2, sust):
    '''
    verifica si hash1 y hash2 son compatibles dadas las sustituciones en sust,
    es decir si pueden hacerse iguales a traves de la sustitucion de sus variables.

    Args:
        hash1 (str o list): primer hash a verificar puede ser una variable, constante (str) o funcion (list)
        hash2 (str o list): segundo hash a verificar puede ser una variable, constante o funcion (list)
        sust (dict): diccionario de sustituciones donde las claves son variables y el valor es la
                    sustitucion correspondiente a cada variable.
    Returns:
        boolean: hash1 y hash2 son compatibles
    
    Complejidad temporal
    En todos los llamados de la funcion el proceso mas pesado es el de sustitucion con complejidad
    O(n*m) y teniendo en cuenta que el caso recursivo se da cuando ambas son funciones con una cantidad a
    de argumentos en hash1 y hash2 entonces por cada par de argumentos se va a hacer un llamado a compatible
    llevando esto a una complejidad O(n*m*a)
    '''
    ans = False
    # Antes de verificar se aplican todas las sustituciones disponibles a ambos hashes 
    #if len(sust) != 0 and (not(type(hash1) == str and hash1[0].islower() and  type(hash2) == list) and not(type(hash2) == str and hash2[0].islower() and  type(hash1) == list)):
    if len(sust) != 0 and ((type(hash1) == str and hash1[0].isupper()) or (type(hash2) == str and hash2[0].isupper())):
        # solo si hay sustituciones en el diccionario y se cumple que los hashes no hacen la pareja funcion constante
        # ya que en el primer caso se recorreria todo el hash para no hacer sustitucion
        # y en el segundo caso de entrada sabemos que no son compatibles entonces no hace falta sustituir
        hash1 = replace(hash1, sust)    # O(n*m) con n hashes ocurrentes dentro de hash1 y m sustituciones en sust
        hash2 = replace(hash2, sust)    # O(n*m) con n hashes ocurrentes dentro de hash2 y m sustituciones en sust

    # Son trivialmente compatibles
    if hash1 == hash2: ans = True
    elif type(hash1) == str and  type(hash2) == str:
        if hash1[0].isupper(): sust[hash1] = hash2; ans = True
        elif hash2[0].isupper(): sust[hash2] = hash1; ans = True
        # si no se cumple ninguna de las anteriores ambos son constantes, y son distintas
    # los casos a continuacion consideran la pareja variable funcion variable, la asignacion solo se puede hacer
    # si la variable no ocurre dentro de los argumentos de la funcion para evitar asignaciones ciclicas
    elif type(hash1) == str and hash1[0].isupper() and  type(hash2) == list:
        if not occurs(hash1, hash2): sust[hash1] = hash2; ans = True    # O(n) con n hashes ocurrentes dentro de hash2
    elif type(hash2) == str and hash2[0].isupper() and type(hash1) == list:
        if not occurs(hash2, hash1): sust[hash2] = hash1; ans = True    # O(n) con n hashes ocurrentes dentro de hash1
    elif type(hash1) == list and type(hash2) == list:
        if hash1[0] == hash2[0] and len(hash1[1]) == len(hash2[1]):
            # si ambos son funciones y tienen el mismo nombre y cantidad de argumentos hay que ver si cada pareja de sus argumentos son compatibles
            i = 0
            ans = True
            args1 = hash1[1]; args2 = hash2[1]
            while i < len(args1) and ans:
                ans = compatible(args1[i], args2[i], sust)
                i+=1
    return ans

def main():
    '''
    Lee los datos de entrada y genera el resultado correspondiente
    '''
    line = stdin.readline().strip()
    while line != "END 0":
        line = line.split()
        name, cases = line
        cases = int(cases)
        
        sust = dict()
        i = 1
        flag = True
        hash1 = stdin.readline().strip()
        hash1 = process(hash1)  # O(n): con n tamaño de la cadena hash1
        while i < cases:
            hash2 = stdin.readline().strip()
            # solo si los hashes han sido compatibles hasta este punto se sigue procesando
            # la cadena de entrada y verificando si son compatibles, si ya falló no es necesario
            if flag:
                hash2 = process(hash2)  # O(n): con n tamaño de la cadena hash2
                flag = compatible(hash1, hash2, sust) # O(n*m*a)
                hash1 = hash2
            i+=1
        if flag: print("analysis inconclusive on %s" %name)
        else: print("%s is a Starflyer agent" %name)
            
        line = stdin.readline().strip()  
main()
