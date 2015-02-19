
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox



root = Tk()

w= Label (root, text="RPG Game")
w.pack()




messagebox.showinfo("RPG BATTLE", "This RPG game will let you name your hero, randomly generate his or her stats, and let you battle enemies")

#varibles
player = simpledialog.askstring("What is your name?", "Name your hero")

HP = random.randint(50,100)

strength = random.randint(1,10)

agility = random.randint(1 , 10)

wisdom = random.randint(1 , 5)

enemyhp = random.randint(50,100)
enemystrength = random.randint(1,10)
attackdmg = random.randint(1,20)
enemydmg = random.randint(1,20)

#show player info
messagebox.showinfo ("Player Name", " Your name is {}." .format(player))
messagebox.showinfo("HP", "HP is your health, your health is {}." .format(HP))
messagebox.showinfo("Strength" , "Strength will make your attacks stronger, your strength is {}." .format(strength))
messagebox.showinfo("Agility" ,  "Agility will decide how much damage you take, your agility is {}." .format (agility))
messagebox.showinfo("Wisdom" ,  "Wisdom will decide how much  your health will increase, your wisdom is {}." .format  (wisdom))
messagebox.showinfo("Attack", "Your attack damage is {}" .format(attackdmg))

#stat calculation
if strength >= 6:
    attackdmg += 3
    messagebox.showinfo("Attack Increase", "Your strength made your attack better. Your attack is now: {}." .format(attackdmg))
if strength >= 8:
    attackdmg += 5
    messagebox.showinfo("Attack Increase", "Your  very high strength made your attack better again. Your attack is now: {}." .format(attackdmg))
if agility <= 4 :
    enemydmg += 3
    messagebox.showinfo("Low Agility", "Due to low agility you will take 3 more damage every hit.")
if agility >= 6 :
    enemydmg -= 1
    messagebox.showinfo("Average Agility", "Your average agility allows you to take one less damage per hit")
if agility >= 8 :
    enemydmg -= 4
    messagebox.showinfo("Super Agile", "Your high agility allows you to dodge 4 points of damage per hit")
if wisdom >= 4:
    HP += 10
    messagebox.showinfo("High Wisdom", "You have high Wisdom so you'll get 10 extra HP")
if enemystrength >= 6:
    enemydmg += 3
#fighting
messagebox.showinfo("START!","You enter a dark damp cave for shelter in the night. A giant Grizzly Bear is sleeping in the cave, with {} health!. Time to fight!".format(enemyhp))

choice = None
while choice != "no":
    choice = simpledialog.askstring("Fight?", "Do you want to attack? Yes or no?")
    if choice == "yes" or "y":
        enemyhp -= attackdmg
    if choice == "yes" or "y" :
        HP -= enemydmg
        messagebox.showinfo("Enemy Health", "The enemy now has {} HP." .format(enemyhp))
        messagebox.showinfo("Enemy Attack", "Your enemy has attacked you for {} HP.".format(enemydmg))
        messagebox.showinfo("Your health", "Your health is now at {}." .format(HP))



    if HP <= 0 and enemyhp <=0:
        messagebox.showinfo("Dead", "You killed the bear but his final blow made you bleed out and die.")
        break

    if enemyhp <= 0:
        messagebox.showinfo("Enemy Killed", "You have defeated the bear!")
        break

    elif HP <= 0 or choice =="no":
        messagebox.showinfo("You have died", "You died, RIP")
        choice == "no"
        
        break




#2nd fight varibles
enemyhp2 = random.randint(50,100)
enemystrength2 = random.randint(1,10)
enemydmg2 = random.randint(1,20)

if enemystrength2 >= 6:
    enemydmg2 += 3
if agility <= 4 :
    enemydmg2 += 3
if agility >= 6 :
    enemydmg2 -= 1
if agility >= 8 :
    enemydmg -= 4


#2nd fight
if choice == "yes" or HP > 0:
    messagebox.showinfo("Fight 2",
                    "You spend the night in the cave and when you wake up a bandito is rummaging through your stuff!")

choice2 = None
while choice2 != "no":
    choice2 = simpledialog.askstring("Fight?", "Do you want to attack? Yes or no?")
    if choice2 == "yes" or "y":
        enemyhp2 -= attackdmg
    if choice2 == "yes" or "y":
        HP -= enemydmg2
        messagebox.showinfo("Enemy Health", "The enemy now has {} HP." .format(enemyhp2))
        messagebox.showinfo("Enemy Attack", "Your enemy has attacked you for {} HP.".format(enemydmg2))
        messagebox.showinfo("Your health", "Your health is now at {}." .format(HP))


    if enemyhp2 <= 0:
        messagebox.showinfo("Enemy Killed", "Before the bandito dies he tells you that he was only looking for food for his children.")
        break
    elif HP <= 0 or choice2 =="no":
        choice2 =="no"
        messagebox.showinfo("You have died", "As you take your final breath you see the bandito take your sword and backpack, RIP.")
        break











