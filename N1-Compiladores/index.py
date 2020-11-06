import regras_producao
from regras_producao import aplicaSVG()
from regras_producao import desenho

arquivo = open('entrada.txt','r')
resultado = []
aux = ''
reg = ''
regra = arquivo.readline().strip()
for letra in regra:

    if(letra == 'X'):
        reg = 'XX+s-X+Y+X-XY+sX-Ys+XY'
        resultado.append(reg)
    elif(letra == 'Y'):
        letra = 'Y'
    elif(letra == 's'):
        letra = 's'
    elif(letra == '+'):
        letra = '+'
    elif(letra == '-'):
        letra = '-'
    
 resultado.append(letra)

resultadoTxt = aux.join(resultado)
print(resultadoTxt)
aplicaSVG(resultadoTxt)
desenho.save()


