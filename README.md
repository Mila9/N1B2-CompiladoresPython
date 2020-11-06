# N1B2-CompiladoresPython

*Descrição*
Trabalho N1B2 de compiladores de _*Lsystems*_ para gerar figuras utilizando SVG

*Execução*
O programa foi elaborado utilizando python 3.8.3 e com a lib svgwrite instalada para
criação de figuras, juntamente com o math e a leitura de arquivos txt, após instalar as *libs*
e instalar o python no vscode abra a pasta e de run no programa, irá gerar um saida.svg com a imagem relativa
a gramática determinada.

**PS:Caso queira mudar a regra para gerar a imagem necessita alterar o txt seguindo o padrão exemplo da regra de produção
**e também será necessário alterar o arquivo index.py substituindo a nova regra no if de "X".


*Gramática*
A gramática determinada foi:
*"X" - Desenha uma linha*
*"s" - Salva o ponto atual em uma lista*
*"Y" - Remove um ponto da lista e assume tal ponto como atual*
*"-" - Vira 60º para esquerda*
*"+" - Vira 60° para a direita*

*Regras de Produção*
X-> XX+s-X+Y+X-XY+sX-Ys+XY
