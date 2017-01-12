from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
janela=Window(800, 618)
from PPlay.keyboard import*
from PPlay.collision import *
teclado = Window.get_keyboard()


def preencher_notas():
    vetor_notas=[0,0,0,0,0]
    for x in range(5):
        notas=Sprite('botoes.png')
        vetor_notas[x]=notas
    return vetor_notas

def guitarra():
    vetor_guitarra=[0,0,0,0]
    for x in range(4):
        notas=Sprite('botoes.png')
        vetor_guitarra[x]=notas
    return vetor_guitarra

def mover_notas(a,s,d,f,g): #as letras são as velocidades da nota de acordo com a música
        m[0].move_y(a)
        m[1].move_y(s)
        m[2].move_y(d)
        m[3].move_y(f)
        m[4].move_y(g)
        for x in range(4):
            if m[x].y>janela.height-m[x].height:
                m[x].set_position()#voltam pra posição inicial

def posicionar_notas(): #aqui eu tenho que ver direito como a guitarra e as notas dela vão ficar pra eu posicionar as notas que vão cair
    global coord_y
    m[0].set_position(janela.width/2,coord_y)
    m[1].set_position(janela.width/2+m[0].width+10,coord_y)
    m[2].set_position(janela.width/2+m[0].width+90,coord_y)
    m[3].set_position(janela.width/2+m[0].width+160,coord_y)
    for x in range (4):
        if m[x].height>janela.height-m[x].height:
            m[x].set_position(janela.width/2,0)
            coord_y=0

def posicionar_notasguitarra():
    g[0].set_position(janela.width/2,500)
    g[1].set_position(janela.width/2+g[0].width+10,500)
    g[2].set_position(janela.width/2+g[0].width+90,500)
    g[3].set_position(janela.width/2+g[0].width+160,500)

def verificação(a):
    global pontuação
    for x in range(4):
        for y in range(4):
            if(m[x].collided(g[y]))and teclado.key_pressed(a):
                pontuação+=10

                print('oi')
pontuação=0
ptc=str(pontuação)
coord_y=0
m=preencher_notas()
g=guitarra()
posicionar_notasguitarra()
posicionar_notas()
while True:
    janela.set_background_color((255,255,255))
    janela.draw_text(str(pontuação), janela.width/2 + 50, 50, 50, (0,0,0,), "Arial", True, False)
    m[0].draw()
    m[1].draw()
    m[2].draw()
    m[3].draw()
    g[0].draw()
    g[1].draw()
    g[2].draw()
    g[3].draw()
    coord_y+=1

    verificação('a')

    m[0].set_position(janela.width/2,coord_y)
    m[1].set_position(janela.width/2+m[0].width+10,coord_y)
    m[2].set_position(janela.width/2+m[0].width+90,coord_y)
    m[3].set_position(janela.width/2+m[0].width+160,coord_y)
    for x in range(4):
        if coord_y>janela.height:
            m[x].set_position(janela.width/2,0)
            coord_y=0



    janela.update()

