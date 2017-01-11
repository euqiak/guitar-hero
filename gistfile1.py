from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
import time
janela=Window(800, 618)


def preencher_notas():
    vetor_notas=[0,0,0,0]
    for x in range(4):
        notas=Sprite('botoes.png')
        vetor_notas[x]=notas
    return vetor_notas

def mover_notas(a,s,d,f): #as letras são as velocidades da nota de acordo com a música
        m[0].move_y(a)
        m[1].move_y(s)
        m[2].move_y(d)
        m[3].move_y(f)
        for x in range(3):
            if m[x].y>janela.height-m[x].height:
                m[x].set_position()#voltam pra posição inicial


#Preenchimento e posicionamento das notas, eu coloquei as coordenadas que você usou no seu código, mas elas não bateram com a guitarra
m=preencher_notas()
m[0].set_position(m[0].width+35/2, 0)
m[1].set_position(m[0].width+105 / 2, 0)
m[2].set_position(m[0].width+173  / 2, 0)
m[3].set_position(m[0].width+232  / 2, 0)

janela=Window(800, 600)
janela.set_background_color((255,255,255))
mouse = Window.get_mouse()
keys = Window.get_keyboard()
lvl1_sheet = open("sheet", "r")#Esse arquivo ta aberto em modo de leitura e contem o tempo de cada nota
start = time.time()
curr = time.time()
i = 0#contador dos vetores de botões
#w = 0
#j = 0


#####menu inicial#####
fundomenu = Sprite('fundo.jpg')
comecar = Sprite('comecar.png')
comecar.set_position(janela.width/2-110, 150)
sair = Sprite('sair.png')
sair.set_position(janela.width/2-100, 250)

fundomenu.draw()
comecar.draw()
sair.draw()

#####coisas que vão aparecer no game#####
fundofase = Sprite('background.jpg')
green = Sprite('green.png')
red = Sprite('red.png')
yellow = Sprite('yellow.png')
blue = Sprite('blue.png')
vector = [green, red, yellow, blue]
sprite_vector = 10 * [vector]#Associei tudo num vetor, era assim q tinha q fazer pra usar varios sprites duma vez né?
print(len(sprite_vector))
fret = Sprite('neck.jpg')
lvl1_song = Sound('reptilia.ogg')#Segundo o aviso do esteban na biblioteca do PPlay, o som tem q estar nesse formato

###posicionando essa bosta toda###
fret.set_position(300, 0)
for i in range(len(sprite_vector)):
    sprite_vector[i][0].set_position(fret.x + 35 - green.width / 2, 0)
    sprite_vector[i][1].set_position(fret.x + 105 - green.width / 2, 0)
    sprite_vector[i][2].set_position(fret.x + 173 - green.width / 2, 0)
    sprite_vector[i][3].set_position(fret.x + 232 - green.width / 2, 0)

while (True):
    #começando o jogo
    if mouse.is_over_object(comecar) and mouse.is_button_pressed(1):
        fundofase.draw()
        fret.draw()
        lvl1_song.play()

        m[0].draw()
        m[1].draw()
        m[2].draw()
        m[3].draw()


        notes = float(lvl1_sheet.readline())
        #Essa variavel le uma linha a cada while. A partir dai q eu to tendo um perrengue
        while(lvl1_song.is_playing()):
            while(notes != ""):#Passa o tempo das notas até chega no fim do arquivo
                curr = time.time()
                #Um intervalo de tempo pq a precisão do float deixa isso meio zoado
                if ((notes - 0.01) < (curr - start) < (notes + 0.01)):
                    sprite_vector[i][0].move_y(0.01)
                    sprite_vector[i][0].draw()
                    notes = float(int(lvl1_sheet.readline() * 100) / 100)
                    print(notes)
                if(sprite_vector[i][0].y != 0):
                    i += 1
                janela.update()
                #Aqui ele checa tudo o q ja começou a andar e mantém andando(se a deusa quiser)
                for w in range(len(sprite_vector)):
                    for j in range(len(sprite_vector[0])):
                        if(sprite_vector[w][j].y != 0):
                            sprite_vector[w][j].move_y(0.1)
                            sprite_vector[w][j].draw()
                            janela.update()
                #E reposiciona o q ja saiu da tela
                for w in range(len(sprite_vector)):
                    for j in range(len(sprite_vector[0])):
                        if(sprite_vector[w][j].y > janela.height):
                            sprite_vector[w][j].y = 0
                            janela.update()
                if(i > 9):
                    i = 0
            janela.update()
        #Reposicionando essa bosta toda, mas acho q essa parte pode ser desnecessaria agora
        green.set_position(fret.x + 35 - green.width / 2, 0)
        red.set_position(fret.x + 105 - green.width / 2, 0)
        yellow.set_position(fret.x + 173 - green.width / 2, 0)
        blue.set_position(fret.x + 232 - green.width / 2, 0)

        for x in range(4):
            m[x].draw()

        janela.update()
    #janela.draw_text('Sair', janela.width/2-100, 250, 50, (255,255,255), "Hero Bold", True, True)

    janela.update()


janela.update()
lvl1_sheet.close()
