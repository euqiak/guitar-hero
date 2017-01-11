from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
janela=Window(800, 618)


def preencher_notas():
    vetor_notas=[0,0,0,0,0]
    for x in range(5):
        notas=Sprite('botoes.png')
        vetor_notas[x]=notas
    return vetor_notas

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

coord_y=0
m=preencher_notas()
posicionar_notas()
while True:
    janela.set_background_color((255,255,255))
    m[0].draw()
    m[1].draw()
    m[2].draw()
    m[3].draw()
    coord_y+=0.1
    m[0].set_position(janela.width/2,coord_y)
    m[1].set_position(janela.width/2+m[0].width+10,coord_y)
    m[2].set_position(janela.width/2+m[0].width+90,coord_y)
    m[3].set_position(janela.width/2+m[0].width+160,coord_y)
    for x in range(4):
        if coord_y>janela.height:
            m[x].set_position(janela.width/2,0)
            coord_y=0


    janela.update()

