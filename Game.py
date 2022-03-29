import pygame
import time
import random

import tkinter as tk
main = tk.Tk()

import mysql.connector as myc
my = myc.connect(host='localhost', user = 'root', passwd = 'Dongle@123', database = 'score')

pygame.init()

crs = pygame.mixer.Sound("crsh.wav")
pygame.mixer.music.load("music.wav")

display_width=800
display_height=600

black = (0,0,0)
white =(255,255,255)
red = (255,0,0)
blue = (251, 0, 194)
br = (248, 45, 13)
y = (251, 240, 0)
bgr = (0, 251, 21)
gr = (29, 204, 6)

car_width = 71

ps = True
crsh = True

im = pygame.image.load("l.png")

pygame.display.set_icon(im)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

sc =  pygame.image.load("sc.png")
b = pygame.image.load("c.png")
c1=pygame.image.load("1.png")
c2=pygame.image.load("2.png")
c3=pygame.image.load("3.png")
c4=pygame.image.load("4.png")
c5=pygame.image.load("5.png")
bg = pygame.image.load("bg.png")
go = pygame.image.load("g.png")

ad = pygame.image.load("Ad.jpg")

carImg = pygame.image.load("racer.png")
    
def thing_dodged(count):
    font=pygame.font.SysFont("comicsansms",40)
    text = font.render("SCORE:"+str(count),True, white)
    gameDisplay.blit(text,(0,0))

def things(tx, ty, tw, th,col):
    L = [c1,c2,c3,c4,c5]
    q = L[col]
    gameDisplay.blit(q,(tx,ty))
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    
def g(x,y):
    gameDisplay.blit(go,(x,y))
    pygame.display.update()
    
    time.sleep(3)
    
    gameDisplay.blit(b,(0,0))
    pygame.display.update()
    
    time.sleep(2)

def inp(dod):
    def a():
        o = str(t1.get())
        sq(dod,o)
    main.title("You Info")
    l1 = tk.Label(main, text = "Your Name")
    l1.pack()
    t1 = tk.Entry()
    t1.pack()

    b1 = tk.Button(main, text = "Submit", command = a)
    b1.pack()

    main.mainloop()
    

def sq(co,t):
    a = t
    c = my.cursor()
    sq = "Insert into score(Name,Score) VALUES(%s,%s)"
    val = (a,co)
    c.execute(sq,val)
    my.commit()
    
def call(p):
    font=pygame.font.SysFont("comicsansms",70)
    t = font.render("HI-Score :- " +str(p[0]),True,black)
    gameDisplay.blit(t,(150,250))
    pygame.display.update()

def see():
    c=my.cursor()
    c.execute("Select max(score) from score")
    p = c.fetchone()
    gameDisplay.blit(sc,(0,0))
    call(p)
    time.sleep(2)
    menu()
            
    
                
def text_obj(text, font):
    r = (0,0,0)
    Surface = font.render(text, True, r)
    return Surface, Surface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms",40)
    TextSurf, TextRect = text_obj(text,largeText)
    TextRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    g((display_width/2)-250,(display_height/2)-100)
    pygame.display.update()
    time.sleep(3)
    
def ano():
    m = pygame.mouse.get_pos()
    c = pygame.mouse.get_pressed()
    if 725>m[0] and m[0]>625 and 450>m[1] and m[1]>400:
            pygame.draw.ellipse(gameDisplay,y,(625,400,100,50))
            if c[0]==1:
                menu()
    else:
        pygame.draw.ellipse(gameDisplay,blue,(625,400,100,50))
    font=pygame.font.SysFont("comicsansms",35)
    q = font.render("Back",True,black)
    gameDisplay.blit(q,(629,400))
    pygame.display.update()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crs)
    message_display("You Crashed")
    
def how():
    h = pygame.image.load("h.png")
    gameDisplay.blit(h,(0,0))
    
    ano()
    time.sleep(100)
    pygame.display.update()
    
def menu():
    global ps
    mnu = True
    while mnu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(ad,(0,0))
##        largeText = pygame.font.SysFont("comicsansms",200)
##        TextSurf, TextRect = text_obj("Racer",largeText)
##        TextRect.center = (display_width/2),(display_height/2)
##        gameDisplay.blit(TextSurf, TextRect)

        m = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        #Start button
        if 300>m[0] and m[0] >150 and 600>m[1] and m[1] > 500:
            pygame.draw.ellipse(gameDisplay, bgr, (150,500,150,100))
            if c[0]==1:
                game_loop()
        else:
            pygame.draw.ellipse(gameDisplay, y, (150,500,150,100))
        #Exit button
        if 686>m[0] and m[0]>537 and 600>m[1] and m[1]>500:
             pygame.draw.ellipse(gameDisplay, br, (536,500,150,100))
             if c[0]==1:
                 pygame.quit()
                 quit()
        else:
             pygame.draw.ellipse(gameDisplay, y, (536,500,150,100))
        #Score
        if 455>m[0] and m[0]>358 and 600>m[1] and m[1]>558:
            pygame.draw.ellipse(gameDisplay,blue,(358,558,100,50))
            if c[0]==1:
                see()

        else:
            pygame.draw.ellipse(gameDisplay,y,(358,558,100,50))

        if 455>m[0] and m[0]>358 and 600>m[1] and m[1]>500:
            pygame.draw.ellipse(gameDisplay,y,(358,500,100,50))
            if c[0]==1:
                h = pygame.image.load("h.png")
                gameDisplay.blit(h,(0,0))
                pygame.display.update()
                time.sleep(5)
                if 725>m[0] and m[0]>625 and 450>m[1] and m[1]>400:
                        pygame.draw.ellipse(gameDisplay,y,(625,400,100,50))
                        if c[0]==1:
                            menu()
                else:
                    pygame.draw.ellipse(gameDisplay,red,(625,400,100,50))
                font=pygame.font.SysFont("comicsansms",35)
                q = font.render("Back",True,black)
                gameDisplay.blit(q,(633,403))
                pygame.display.update()

        else:
            pygame.draw.ellipse(gameDisplay,red,(358,500,100,50))
            
        #Button Font   
        font=pygame.font.SysFont("comicsansms",40)
        t = font.render("Start",True,black)
        gameDisplay.blit(t,(170,520))
        p = font.render("Quit",True,black)
        gameDisplay.blit(p,(565,520))
        font=pygame.font.SysFont("comicsansms",20)
        q = font.render("H.Score",True,red)
        gameDisplay.blit(q,(371,568))
        q = font.render("How ?",True,black)
        gameDisplay.blit(q,(384,512))
        pygame.display.update()

def wait():
    global ps
    pygame.mixer.music.unpause()
    ps = False
    
def Pause():
    global ps
    pygame.mixer.music.pause()
    while ps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(blue)
        largeText = pygame.font.SysFont("comicsansms",200)
        TextSurf, TextRect = text_obj("Paused",largeText)
        TextRect.center = (display_width/2),(display_height/2)
        gameDisplay.blit(TextSurf, TextRect)

        m = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        #Continue button
        if 300>m[0] and m[0] >150 and 550>m[1] and m[1] > 450:
            pygame.draw.ellipse(gameDisplay, bgr, (150,450,150,100))
            if c[0]==1:
                wait()
        else:
            pygame.draw.ellipse(gameDisplay, y, (150,450,150,100))
        #Exit button
        if 686>m[0] and m[0]>537 and 550>m[1] and m[1]>450:
             pygame.draw.ellipse(gameDisplay, br, (536,450,150,100))
             if c[0]==1:
                 pygame.quit()
                 quit()
        else:
             pygame.draw.ellipse(gameDisplay, y, (536,450,150,100))
        #Button Font   
        font=pygame.font.SysFont("comicsansms",40)
        t = font.render("Back",True,black)
        gameDisplay.blit(t,(184,470))
        p = font.render("Quit",True,black)
        gameDisplay.blit(p,(565,470))
        pygame.display.update()

c = random.randint(0,4)

def game_loop():
    global ps
    global colr
    
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    thingStartx = random.randrange(135,573)
    thingStarty = -600
    thingSpeed = 4

    dodged = 0

    z = random.randrange(-1,1)
    p = random.randrange(600,800)
    
    gameExit = False
    while not gameExit:

        thingWidth=78
        thingHeight=175
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    ps = True
                    Pause()
                elif event.key == pygame.K_UP:
                    y_change = -3
                elif event.key == pygame.K_DOWN:
                    y_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change        
        gameDisplay.blit(bg,(0,0))
        
        things(thingStartx, thingStarty, thingWidth, thingHeight,c)
        thingStarty = thingStarty+thingSpeed
        
        car(x,y)
        
        thing_dodged(dodged)
        
        if x > 600 or x < 132:
            crash()
        if thingStarty > display_height:
            thingStarty= 0-thingHeight
            thingStartx = random.randrange(136,550)
            dodged+=1
            thingSpeed+=0.15 
        if y<thingStarty+170:
            print("y crossover")
            if x>thingStartx and x<thingStartx+thingWidth or x+car_width>thingStartx and x+car_width<thingStartx+thingWidth:
                print("X crossover")
                crash()
                inp(dodged)
                menu()

        
        pygame.display.update()
        clock.tick(100)
menu()
game_loop()
pygame.quit()
quit()

