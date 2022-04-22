from tkinter import *
from PIL import  ImageTk, Image
import random

root=Tk()
root.title("Dice Game")
root.geometry("700x800")
root.configure(background = "#e6e4c1")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

Pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Bulbasour =ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Charmender =ImageTk.PhotoImage(Image.open("charmender.jpg"))
Squirtle =ImageTk.PhotoImage(Image.open("squirtle.jpg"))
Ratata =ImageTk.PhotoImage(Image.open("ratata.jpg"))
Nidoking =ImageTk.PhotoImage(Image.open("nidoking.jpg"))
Jigglypuff =ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Meowth =ImageTk.PhotoImage(Image.open("meowth.jpg"))
Persion =ImageTk.PhotoImage(Image.open("persion.jpg"))
Abra =ImageTk.PhotoImage(Image.open("abra.jpg"))
Kadabra =ImageTk.PhotoImage(Image.open("kadabra.jpg"))
Iyvasour =ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
Paras =ImageTk.PhotoImage(Image.open("paras.jpg"))



player1score = Label(root, text = "Player 1", bg = "#67b1cf",fg = "white")
player1score.place(relx = 0.1,rely = 0.3, anchor = CENTER)

player2score = Label(root, text = "Player 2", bg = "#67b1cf",fg = "white")
player2score.place(relx = 0.9,rely = 0.3, anchor = CENTER)

player1scoreLabel = Label(root, bg = "#67b1cf",fg = "white")
player1scoreLabel.place(relx = 0.1,rely = 0.4, anchor = CENTER)

player2scoreLabel = Label(root, bg = "#67b1cf",fg = "white")
player2scoreLabel.place(relx = 0.9,rely = 0.4, anchor = CENTER)

randomDice = Label(root,bg = "#b05b2a",fg = "white")
randomDice.place(relx = 0.5,rely = 0.6,anchor = CENTER)

pokemonList=[Pikachu,Bulbasour,Charmender,Squirtle,Ratata,Nidoking,Jigglypuff,Meowth,Persion,Abra,Kadabra,Iyvasour,Paras]
powerList = [200,60,50,50,40,90,70,60,70,30,70,100,40]

label = Label(root)

label.place(relx =0.5 ,rely = 0.5, anchor = CENTER)
player1Score = 0
def player1():
    global player1Score
    randomNo1 = random.randint(0,13)
    randomPokemon1 = pokemonList[randomNo1]
    label["image"] = randomPokemon1
 
    randomPower1 = powerList[randomNo1]
    player1Score = player2Score + randomPower1
    player1scoreLabel["text"] =str(player1Score)
    
player_1_btn = Button(root,image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor= CENTER)

player2Score = 0
def player2():
    global player2Score
    randomNo2 = random.randint(0,13)
    randomPokemon2 = pokemonList[randomNo2]
    label["image"] = randomPokemon2
    
    randomPower2 = powerList[randomNo2]
    player2Score = player2Score + randomPower2
    player2scoreLabel["text"] =str(player2Score)
    
    
player_2_btn = Button(root,image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6, anchor= CENTER)

root.mainloop()
