from collections import deque

line = deque()
tam = 3 

global f, r
f = -1
r = -1
#--------    
# # Maximum numbers to be stored in the array. We can increase the quantity by changing the value 5 with a new one
#arr = array('i',[])     # An empty array for queue implementation

#firstin - inclusao
def stackup(element):
    global r, f 
    while r and f == tam - 1:
        r = -1
        f = -1
    if len(line) < tam:
        if r < tam - 1:
            line.append(element)
            print(line)
            r = r + 1
            print("R: ", r)
            print("F: ", f)
        else:
            print("false overflow")
    else:
        print("OVERFLOW")
            
#firstout - remove
def unstack():
    global f
    global r
    if not empty():
        line.popleft()
        print(line)
        f = f + 1
    print("F: ", f)
    print("R: ", r)
    
# consult
def consult(line):
    a = int(input("Qual numero você deseja consultar: "))
    if a not in line:
        print("Valor está na pilha")
    else:
        print("Valor não encontrado")

#método que retorne um booleano indicando se a linha está vazia
def empty():
    print("Underflow")
    return len(line) == 0

    
        
        


