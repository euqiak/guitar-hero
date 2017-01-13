from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
janela=Window(800, 618)
from PPlay.keyboard import*
from PPlay.collision import *
#dificuldade = Sprite("dificuldade.png")

def preencher_notas():
    vetor_notas=[]
    for x in range(5):
        notas = Sprite('botoes.png')
        vetor_notas.append(notas)
    return vetor_notas

def guitarra():
    vetor_guitarra = []
    for x in range(4):
        notas = Sprite('botoes.png')
        vetor_guitarra.append(notas)
    return vetor_guitarra


def posicionar_notas(): #aqui eu tenho que ver direito como a guitarra e as notas dela vão ficar pra eu posicionar as notas que vão cair
    global coord_y,a,b,c,d, m
    m[0].set_position(250,coord_a)
    m[1].set_position(250,coord_b)
    m[2].set_position(250,coord_c)
    m[3].set_position(250,coord_d)
    for x in range (4):
        if m[x].height>janela.height-m[x].height:
            m[x].set_position(250,0)

def mover_notas(q,w,e,r):
    global a,b,c,d
    a += q
    b += w
    c += e
    d += r

def posicionar_notasguitarra():
    global g
    g[0].set_position(250,500)
    g[1].set_position(250+g[0].width+10,500)
    g[2].set_position(250+g[0].width+90,500)
    g[3].set_position(250+g[0].width+160,500)


mouse = Window.get_mouse()
teclado = Window.get_keyboard()
comecar = Sprite("comecar.png")
dificuldade = Sprite("dificuldade.png")
sair = Sprite("sair.png")
opsong = Sound("lonelyboy.ogg")
lvlsong = Sound("reptilia.ogg")
pip = Sound("gong.ogg")

opsong.play()
pontuação=0
ptc=str(pontuação)
coord_a=0
coord_b=0
coord_c=0
coord_d=0


va=0.3
vb=0.5
vc=0.6
vd=0.9

m=preencher_notas()
#print(len(m))
g=guitarra()
posicionar_notasguitarra()
posicionar_notas()

janela.set_background_color((255,255,255))
comecar.set_position (janela.width/2 - comecar.width/2, 50)
dificuldade.set_position (janela.width/2 - dificuldade.width/2, 150)
sair.set_position (janela.width/2 - sair.width/2, 350)
comecar.draw()
dificuldade.draw()
sair.draw()
voltar = 0#0 é falso, n é pra voltar a tela. 1 volta. Agora você pode voltar da tela
          #de dificuldade apertando ESC ao invés de fechar o jogo

while True:
    if mouse.is_over_object(comecar) and mouse.is_button_pressed(1):
        opsong.pause()
        lvlsong.play()
        while True:
            m = preencher_notas()
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
            coord_a += va
            coord_b += vb
            coord_c += vc
            coord_d += vd
            if(m[0].collided(g[0]))and teclado.key_pressed('a'):
                pontuação+=10
            if(m[1].collided(g[1]))and teclado.key_pressed('s'):
                pontuação+=10
            if(m[2].collided(g[2]))and teclado.key_pressed('d'):
                pontuação+=10
            if(m[3].collided(g[3]))and teclado.key_pressed('f'):
                pontuação+=10


            m[0].set_position(250,coord_a)
            m[1].set_position(250+m[0].width+10,coord_b)
            m[2].set_position(250+m[0].width+90,coord_c)
            m[3].set_position(250+m[0].width+160,coord_d)
            if coord_a>janela.height:
                    m[0].set_position(janela.width/2,0)
                    coord_a=0
            if coord_b>janela.height:
                    m[1].set_position(janela.width/2,0)
                    coord_b=0
            if coord_c>janela.height:
                    m[2].set_position(janela.width/2,0)
                    coord_c=0
            if coord_d>janela.height:
                    m[3].set_position(janela.width/2,0)
                    coord_d=0
            if(teclado.key_pressed("ESC")):
                janela.close()

        janela.update()
    janela.update()


    if mouse.is_over_object(dificuldade) and mouse.is_button_pressed(1):

        while (voltar == 0):
            a=1
            b=2
            c=3
            janela.set_background_color((255,255,255))
            janela.draw_text(str(a), janela.width/2, 100, 50, (130,200,238,), "Courier", True, False)
            janela.draw_text(str(b), janela.width/2, 250, 50, (130,238,175), "Courier", True, False)
            janela.draw_text(str(c), janela.width/2, 400, 50, (237,194,175), "Courier", True, False)
            janela.draw_text("Pressione Esc para voltar", janela.width/2 - 100 , 550, 25, (0, 0, 0), "Courier", True, False)

            if teclado.key_pressed('1'):
                va=0.2
                vb=0.4
                vc=0.1
                vd=0.3
                pip.play()

            if teclado.key_pressed('2'):
                va=0.3
                vb=0.5
                vc=0.6
                vd=0.9
                pip.play()

            if teclado.key_pressed('3'):
                va=0.9
                vb=1
                vc=1.1
                vd=1.4
                pip.play()

            if(teclado.key_pressed("ESC")):
                janela.set_background_color((255,255,255))
                comecar.set_position (janela.width/2 - comecar.width/2, 50)
                dificuldade.set_position (janela.width/2 - dificuldade.width/2, 150)
                sair.set_position (janela.width/2 - sair.width/2, 350)
                comecar.draw()
                dificuldade.draw()
                sair.draw()
                voltar = 1

            janela.update()


    if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
        janela.close()
    janela.update()

