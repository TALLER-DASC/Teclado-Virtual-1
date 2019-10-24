rows = 0
cols = 0
teclado = []

#LEER EL ARCHIVO
fil = open("D:\Prueba1.txt", "r")
if fil.mode == 'r':
    #obtener el contenido
    lines = fil.readlines()
    c = 1
    l = 0

    #obtener la palabra a buscar
    palabra = lines[len(lines)-1]
    pal = list(palabra)
    
    #recorrer los renglones
    for line in lines:

        #encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ' , row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])     
        
        #encontrar las letras del teclado
        if c > 1 and c <= (rows+1):
            linea = line[:-1]
            letters = list(linea)
            teclado.append(letters)
        c+=1

    #Algoritmo de busqueda
    x = 0
    y = 0
    cx = 0
    cy = 0
    mov = 0
    cont = 0
    pal.append("*")
    while x < len(teclado):
        while y < len(teclado[0]):
            if (teclado[x][y] == pal[cont]):
                if(cx<x):
                    mov += x-cx
                elif(cx>x):
                    mov += cx-x
                if(cy<y):
                    mov += y-cy
                elif(cy>y):
                    mov += cy-y
                cx=x
                cy=y
                x=0
                y=0
                mov += 1
                cont += 1
            x += 1
        y += 1

print(palabra)
for x in range(len(pal)): 
    print(pal[x]) 
print(teclado)
print(teclado[0][1]) #B
