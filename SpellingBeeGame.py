import pythoncom
import threading
import time
import sys
import pygame
import random
from win32com.client import Dispatch
mywords=[]
with open(file='words.txt', mode='r') as file:
    # reading each line
    for line in file:
        for word in line.split():
            mywords.append(word)

X=650
Y=490

white = (255, 255, 255)

yellow=(243,250,0)
pygame.init()
surface=pygame.display.set_mode((X, Y))
pygame.display.set_caption('SpellingBee')
surface.fill(white)
gamerun=1


images=['three.png','two.png','one.png']
pygame.mixer.init()
clock=pygame.time.Clock()
basefont=pygame.font.SysFont('bahnschrift',30)

scorefont=pygame.font.SysFont('comicsansms',33)

highscore=pygame.font.SysFont('comicsansms',23)
bg2=pygame.image.load('bg2.png')

checkbtn=pygame.image.load('check.png')
devname=pygame.font.SysFont('comicsansms',23)

def startgame(gamerun):
    background = pygame.image.load('spelling.jpg')
    x = 20
    y = 20
    global devname
    for i in range(3):
        surface.fill(white)
        background = pygame.transform.scale(background, (350+x, 350+y))
        surface.blit(background, (40, 50))
        picture = pygame.image.load(images[gamerun - 1])
        picture = pygame.transform.scale(picture, (80, 80))
        surface.blit(picture, (280, 40))
        gamerun += 1
        # sound = pygame.mixer.Sound('tick.mp3')
        # sound.play()
        developername = devname.render(f'Developer: Hasanat Lodhi', True, (32, 57, 47))
        surface.blit(developername,(180,10))
        pygame.display.update()
        x+=20
        y+=20
        pygame.time.wait(1500)
inputrect=pygame.Rect(180,400,260,38)
def maingame():
    beeimg = pygame.image.load('spellingbee.jpg')
    background = pygame.transform.scale(beeimg, (550, 100))
    surface.blit(background, (50, 0))

def playsound():
    pass
   # sound=pygame.mixer.Sound('beat.mp3')
   # sound.set_volume(0.05)
   # sound.play()

buttonclick=False

threadingrunning=True

textchoice=random.choice(mywords)
gameisover=False
def sayword():
    while threadingrunning:
        global buttonclick
        global gameisover
        if gameisover:
            continue
        if buttonclick==True:
            time.sleep(4)
            buttonclick = False
        else:
            global textchoice
            pythoncom.CoInitialize()
            speak = Dispatch("SAPI.SpVoice")
            speak.Speak(f"Please enter {textchoice}")
            time.sleep(5)

start=True

t1 = threading.Thread(target=sayword)

usertext = ''
lives=4
score=0


def checkwords():
    global isrruning
    global threadingrunning
    global textchoice
    global score
    pythoncom.CoInitialize()
    speak = Dispatch("SAPI.SpVoice")
    if (usertext == textchoice):
        correct = pygame.image.load('correct.png')
        correct = pygame.transform.scale(correct, (200, 200))
        surface.blit(correct, (220, 135))
        pygame.display.update()
        clap = pygame.mixer.Sound('clap.wav')
        clap.play()
        speak.Speak("You entered the correct Spelling")
        # time.sleep(2)
        bg2 = pygame.image.load('bg2.png')
        bg = pygame.transform.scale(bg2, (650, 490))
        surface.blit(bg, (0, 0))
        pygame.display.update()
        score+=1
    else:
        wrongpic = pygame.image.load('no.png')
        wrongpic = pygame.transform.scale(wrongpic, (150, 150))
        surface.blit(wrongpic, (230, 155))
        pygame.display.update()
        wrong = pygame.mixer.Sound('wrongans.wav')
        wrong.play()
        speak.Speak("You entered the wrong spelling")
        global lives
        lives -= 1
        bg2 = pygame.image.load('bg2.png')
        bg = pygame.transform.scale(bg2, (650, 490))
        surface.blit(bg, (0, 0))
        pygame.display.update()
        consective=0
        for i in range(lives):
            pygame.draw.circle(surface, (17, 43, 32), (40, 190 + consective), 13, 6)
            consective += 30
        pygame.display.update()
    if lives==0:
        return True
    textchoice = random.choice(mywords)


isrruning=True
gameover=pygame.image.load('gamov.gif')


def totallives():
    consective = 0
    for i in range(lives):
        pygame.draw.circle(surface, (17, 43, 32), (40, 190 + consective), 13, 6)
        consective += 30


def endgame():
    global score
    global lives
    global start
    global usertext
    global gameisover
    global textchoice
    global threadingrunning
    quitpic=pygame.image.load('quit.png')
    reply=pygame.image.load('playagain.png')
    gameisover=True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                getpos=pygame.mouse.get_pos()
                if getpos[0]>=355 and getpos[0]<=434:
                    if getpos[1] >= 374 and getpos[0] <= 437:
                        pygame.quit()
                        sys.exit()
                if getpos[0] >= 201 and getpos[0] <= 268:
                    if getpos[1] >= 371 and getpos[0] <= 436:
                        score=0
                        lives=4
                        x = 65
                        y = 50
                        for i in range(10):
                            bg = pygame.transform.scale(bg2, (x, y))
                            surface.blit(bg, (0, 0))
                            pygame.display.update()
                            pygame.time.wait(10)
                            x += 65
                            y += 50
                        textchoice=random.choice(mywords)
                        threadingrunning = True
                        gameisover = False
                        spellingbee()
        surface.fill((255, 255, 255))
        bg = pygame.transform.scale(gameover, (X, Y))
        quitpic = pygame.transform.scale(quitpic, (90, 90))
        surface.blit(bg, (0, 0))
        surface.blit(quitpic, (350, 360))
        replypic = pygame.transform.scale(reply, (70, 70))
        surface.blit(replypic, (200, 370))
        clock.tick(40)
        usertext=''
        pygame.display.update()


def spellingbee():
    global checkbtn
    global start
    global usertext
    global isrruning
    global buttonclick
    while isrruning:
        if start:
            startgame(gamerun)
            start=False
            x = 65
            y=50
            for i in range (10):
                bg=pygame.transform.scale(bg2, (x,y))
                surface.blit(bg,(0,0))
                pygame.display.update()
                pygame.time.wait(10)
                x+=65
                y+=50
            playsound()
            t1.start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    usertext=usertext[:-1]

                else:
                    if(len(usertext)<16):
                        usertext+=event.unicode
                        print(usertext)
            if event.type == pygame.MOUSEBUTTONDOWN:
                getpos=pygame.mouse.get_pos()
                if getpos[0]>=460 and getpos[0]<=502:
                    if getpos[1]>=403 and getpos[1]<=436:
                        buttonclick=True
                        returned=checkwords()
                        if returned:
                            endgame()
                        usertext=''
        pygame.draw.rect(surface, yellow, inputrect)

        text=basefont.render(usertext,True,(0, 51, 102))
        textscore=scorefont.render(f'Your score is {score}',True,(255, 51, 0))
        surface.blit(text,inputrect)
        surface.blit(textscore, (200, 103))
        checkbtn = pygame.transform.scale(checkbtn, (50, 50))
        surface.blit(checkbtn, (455, 393))
        totallives()
        pygame.display.update()
        clock.tick(40)
        maingame()
        pygame.display.update()

spellingbee()