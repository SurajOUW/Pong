# Pong in python3
# Ynov B1 A
# Project n°2

import turtle

screen = turtle.Screen() #initialisation de l'écran du Pong
screen.title(Pong)
screen.bgcolor("black") #couleur background
screen.setup(width=1000, height=700)  #taille fenêtre
screen.tracer(0) #vitesse du jeu

# Player 1
player_one = turtle.Turtle()
player_one.speed(0) #vitesse d'animation (déplacement des pixels)
player_one.shape("square") #faire du personnage un carré de 20x20px par défaut
player_one.color("white")
player_one.shapesize(strech_wid=6, strech_len=1)
player_one.penup() #initialise le refresh du writter du score
player_one.goto(-900, 0)

# Player 2
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square") #faire du personnage un carré de 20x20 px par défaut
player_two.color("white")
player_two.shapesize(strech_wid=6, strech_len=1)
player_two.penup()
player_two.goto(900, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #la balle est un carré basique de 20x20 px
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.px = 2 #initialisation du nombre de pixels par lequel la balle va bouger
ball.py = 2 #même chose mais ici sur l'ordonnée et non l'abscisse

#Mise en place des fonction de mouvement du joueur 1 et 2
def player_one_down():
    y = player_one.ycor() #init y tant que position J1 (vers le bas uniquement)
    y -= 30 #l'animation bouge par 30 pixels
    player_one.sety(y) #set y comme la position J1

def player_one_up():
    y = player_one.ycor() #position J1 vers le haut
    y += 30
    player_one.sety(y) #set y comme la position de J1

def player_two_down():
    y = player_two.ycor()
    y -= 30
    player_two.sety(y)

def player_two_up():
    y = player_two.ycor()
    y += 30
    player_two.sety(y)

# Parameters keyboard
screen.listen() #autorise les commandes claviers
screen.onekeypress(player_one_up, "z")
screen.onekeypress(player_one_down, "s")
screen.onekeypress(player_two_up, "Up")
screen.onekeypress(player_two_down, "Down")

# Main
while True:
    screen.update()

    # Setting the movement of the ball and checking bordelines
    ball.setx(ball.xcor() + ball.px) #set le mouvement par rapport à l'abscisse
    ball.sety(ball.ycor() + ball.py) #set le mouvement par rapport à l'ordonnée

    # Borderline top
    if ball.ycor() > 350:
        ball.sety(350)
        ball.py *= -1 #inverse la direction de la balle
    # Borderline bot
    elif ball.ycor() < -350:
        ball.sety(-350)
        ball.py *= -1
    # Borderline right
    if ball.xcor() > 450:
        score_1 += 1 #indentation du score
        pen.clear() #refresh du writter du score à chaques changements
        pen.write("Joueur 1: {} Joueur 2: {}".format(score_1, score_2), align="center", font=("Courier", 18, "normal"))
        ball.goto(0, 0) #reset la balle au centre
        ball.px *= -1
    # Bordeline left
    elif ball.xcor() < -450:
        score_2 += 1
        pen.clear()
        pen.write("Joueur 1: {} Joueur 2: {}".format(score_1, score_2), align="center", font=("Courier", 18, "normal"))
        ball.px *= -1

    # Collision on players
    if ball.xcor() < -440 and ball.ycor() < player_one.ycor() + 50 and ball.ycor() > player_one.ycor() -50:
        ball.px *= -1

    elif ball.xcor() < 440 and ball.ycor() < player_two.ycor() + 50 and ball.ycor() > player_two.ycor() -50:
        ball.px *= -1
