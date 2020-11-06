import svgwrite
import math

x1in = 0
y1in = 0
x2in = 0
y2in = 0


listaSalvos = []

desenho = svgwrite.Drawing('saida.svg', profile='tiny')


def desenha_linha(x1,y1,x2,y2):
    desenho = svgwrite.Drawing('saida.svg', profile='tiny')
    desenho.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(10, 10, 16, '%'))


class Linha:
    def __init__(self, x1,y1,x2,y2,theta):
        self.x1 = x1       
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.theta = theta

    def set_linha(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.theta = math.pi / 2
    
    def moveTo(self,x,y,angulo):
        self.x2 = x
        self.y2 = y
        self.theta = angulo

    
    def desenhar():
        desenha_linha(x1,y1,x2,y2)

 
        
linha_padrao = Linha()
linhaPadrao = linha_padrao.set_linha(x1in,y1in,x2in,y2in)

 def desenha(caracter):
     if(caracter == 'X'):
            linhaPadrao.x1 = linhaPadrao.x2
            linhaPadrao.y1 = linhaPadrao.y2
            linhaPadrao.x2 = linhaPadrao.x1 + 20 * math.cos(linhaPadrao.theta)
            linhaPadrao.y2 = linhaPadrao.y1 + 20 * math.cos(linhaPadrao.theta)
            linhaPadrao.desenhar()

      elif(caracter == 's'):        
            listaSalvos.append({xAtual: linhaPadrao.x2, yAtual: linhaPadrao.y2, anguloatual: linhaPadrao.theta})
      elif(caracter == 'Y'):
            if(len(listaSalvos) > 0):
                {xAtual, yAtual, anguloatual} = listaSalvos.pop()
                linhaPadrao.moveTo(xAtual,yAtual,anguloatual)
                return
          linhaPadrao.moveTo()
      elif(caracter == '+'):
          linhaPadrao.theta += math.pi / 3
      elif (caracter == '-'):
          linhaPadrao.theta -= math.pi / 3
                


def aplicaSVG(regra_prod):
    
    for(letra in regra_prod):
        char = letra
        desenha(char)

   
