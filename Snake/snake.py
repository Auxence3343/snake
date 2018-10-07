#!/usr/bin/env python
# *-* coding: utf-8 *-*

# Original project by Auxence, forked by KikooDX
#   ________             ______       
#   __  ___/____________ ___  /______ 
#   _____ \__  __ \  __ `/_  //_/  _ \
#   ____/ /_  / / / /_/ /_  ,<  /  __/
#   /____/ /_/ /_/\__,_/ /_/|_| \___/

from tkinter import *
from random import *

global difficulte, delai, title
list = []

life = 1
lim_x = 480
lim_y = 320
score = 0
add = 3
title = "Snake v. 1.2"


# 0 = nord, 1 = est, 2 = sud, 3 = ouest
direction = 1

def reset(event):

    list = []

    life = 1
    lim_x = 64
    lim_y = 48
    score = 0
    add = 3

    # 0 = nord, 1 = est, 2 = sud, 3 = ouest
    direction = 1

# Ne fonctionne PAS sous linux
def pause(event):
    input()

def haut(event):
    global direction
    if direction != 2 :
        direction = 0
    #print("direction ",direction)
    
def droite(event):
    global direction
    if direction != 3 :
        direction = 1
    #print("direction ",direction)
    
def bas(event):
    global direction
    if direction != 0:
        direction = 2
    #print("direction ",direction)
    
def gauche(event):
    global direction
    if direction != 1 :
        direction = 3
    #print("direction ",direction)
    
def add_corp(list,x,y):
    """ajoute un carré"""
    
    list.append([canvas.create_rectangle(x-4, y-4, x+4, y+4, fill = "white", outline = "white"), x, y])
    
    return (list)

def refresh():
    global list
    global life, direction, l_pos_x, l_pos_y, add, score, fruit_x, fruit_y, fruit
    x = 0
    
    while x < len(list):

        # deplacement case 0
        
        pos_x = list[x][1]
        pos_y = list[x][2]

        if x == 0 :
            l_pos_x_tmp = pos_x
            l_pos_y_tmp = pos_y
            
            if direction == 0:

                pos_x = pos_x + 0
                pos_y = pos_y - 8

                canvas.coords( list[x][0], pos_x - 4, pos_y - 4, pos_x + 4, pos_y + 4)

            if direction == 1:

                pos_x = pos_x + 8
                pos_y = pos_y + 0

                canvas.coords( list[x][0], pos_x - 4, pos_y - 4, pos_x + 4, pos_y + 4)

            if direction == 2:

                pos_x = pos_x + 0
                pos_y = pos_y + 8

                canvas.coords( list[x][0], pos_x - 4, pos_y - 4, pos_x + 4, pos_y + 4)

            if direction == 3:

                pos_x = pos_x - 8
                pos_y = pos_y + 0

                canvas.coords( list[x][0], pos_x - 4, pos_y - 4, pos_x + 4, pos_y + 4)
                
            
            #collision entre les cases
                    
            for items in list[1:]:
                x_col = 0
                y_col = 0

                x_test = items[1]
                y_test = items[2]
                
                if pos_x - 4 < x_test and x_test < pos_x + 4 :
                    x_col = 1
                    
                if pos_y - 4 < y_test and y_test < pos_y + 4 :
                    y_col = 1
                    
                if x_col == 1 and y_col == 1:
                    life = life - 1

                # collision avec fruit
                x_col = 0
                y_col = 0
                
                if pos_x - 4 < fruit_x and fruit_x < pos_x + 4 :
                    x_col = 1
                    
                if pos_y - 4 < fruit_y and fruit_y < pos_y + 4 :
                    y_col = 1
                    
                if x_col == 1 and y_col == 1:
                    score += difficulte
                    root.title("{}, Score : {}".format(title, score))
                    add += 1
                    fruit_x = randint(1, lim_x / 8 - 1) * 8
                    fruit_y = randint(1, lim_y / 8 - 1) * 8
                    canvas.coords(fruit, fruit_x - 4, fruit_y - 4, fruit_x + 4, fruit_y + 4)
                    
        else:
            # deplacement cases 1 - n
            l_pos_x_tmp = pos_x
            l_pos_y_tmp = pos_y

            pos_x = l_pos_x
            pos_y = l_pos_y
            
            canvas.coords( list[x][0], pos_x - 4, pos_y - 4, pos_x + 4, pos_y + 4)

        list[x][1] = pos_x
        list[x][2] = pos_y

        l_pos_x = l_pos_x_tmp
        l_pos_y = l_pos_y_tmp

        # collision avec les mur
        
        if pos_x + 4 > lim_x or pos_x - 4 < 0 :
            life = life - 1
        
        if pos_y + 4 > lim_y or pos_y - 4 < 0 :
            life = life - 1
        
        # agrandissement de la taille du serpent
            
        if add >= 1 and x == len(list) - 1 :
            list = add_corp(list, l_pos_x_tmp, l_pos_y_tmp)
            add = add - 1
        x += 1
        
    
    if life > 0 :
        #print (list)
        root.after(delai, refresh)
    else :
        root.quit()

# Choix de la difficulté
difficulte = 0

while difficulte % 1 or difficulte < 1 or difficulte > 4:
    difficulte = input("Difficulty :\n 1. Easy\n 2. Normal\
\n 3. Hard\n 4. Insane\n> ")
    try:
        difficulte = int(difficulte)
        print()
    except:
        print("Please insert a number.\n")
        difficulte = 0

delai = 100 - (difficulte * 20)
if difficulte == 4:
    difficulte = 5

# Création de la fenetre + canevas + initialisation fonctions
root = Tk()
root.title(title)
# A décommenter si vous voulez afficher l'icone (ne fonctionne pas sur certains
# systèmes d'exploitation)
#root.iconbitmap("snake_icon.ico")
root.resizable(width=False, height=False)

canvas = Canvas(root, width = lim_x, height = lim_y, background = '#262626')
canvas.pack()

list = add_corp(list,lim_x / 2, lim_y / 2)

fruit_x = randint(1, lim_x / 8 - 1) * 8
fruit_y = randint(1, lim_y / 8 - 1) * 8
fruit = canvas.create_rectangle(fruit_x - 4, fruit_y - 4, fruit_x + 4, fruit_y + 4, fill = "#A44040", outline = "#A44040")

# Touche "reset" commentée car non fonctionnelle.
#root.bind("<r>", reset)
root.bind("<p>", pause)

# Les touches de déplacement.
# Flèches
root.bind("<Up>", haut)
root.bind("<Down>", bas)
root.bind("<Left>", gauche)
root.bind("<Right>", droite)

# QWERTY
root.bind("<w>", haut)
root.bind("<s>", bas)
root.bind("<a>", gauche)
root.bind("<d>", droite)

# C'est comme Vim
root.bind("<k>", haut)
root.bind("<j>", bas)
root.bind("<h>", gauche)
root.bind("<l>", droite)

# Lancement programme principal.
refresh()

root.mainloop()
root.destroy()

print("You scored {} points ! Well played !\n".format(score))
