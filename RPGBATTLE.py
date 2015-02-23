
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox



root = Tk()

w= Label (root, text="RPG Game")
w.pack()




messagebox.showinfo("RPG BATTLE", "This RPG game will let you name your hero, randomly generate his or her stats, and let you battle some banditos")

#varibles
player = simpledialog.askstring("What is your name?", "Name your hero")

HP = random.randint(50,100)

strength = random.randint(1,10)

agility = random.randint(1 , 10)

wisdom = random.randint(1 , 5)

enemyhp = random.randint(50,70)
enemystrength = random.randint(1,10)
attackdmg = random.randint(1,20)
enemydmg = random.randint(1,20)
enemyhp2 = random.randint(40,100)
enemystrength2 = random.randint(1,10)
enemydmg2 = random.randint(5,20)



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
if enemystrength2 >= 6:
    enemydmg2 += 3
if agility <= 4 :
    enemydmg2 += 3
if agility >= 6 :
    enemydmg2 -= 1
if agility >= 8 :
    enemydmg -= 4

#fighting
messagebox.showinfo("START!","You are travelling on the road and a gang of two bandits jump out and try and rob you! You know you can take them."
                             " You can tell from your excellent perception that one bandit has {} HP and the second one has {}!"
                             " Time to fight!".format(enemyhp, enemyhp2))

choice = None
while choice != "no":
    choice = simpledialog.askstring("Fight?", "Do you want to attack? yes or no?")
    if choice == "yes" or "y":
        enemyhp -= attackdmg
        enemyhp2 -= attackdmg
    if choice == "yes" or "y" :
        HP -= enemydmg and enemydmg2
        messagebox.showinfo("Enemy Health", "The enemy now has {} HP. Enemy 2 has {}" .format(enemyhp, enemyhp2))
        messagebox.showinfo("Enemy Attack", "Your enemy has attacked you for {} HP. Enemy 2 attacked you for {} HP".format(enemydmg, enemydmg2))
        messagebox.showinfo("Your health", "Your health is now at {}." .format(HP))


    if enemyhp <= 0:
        enemydmg -= enemydmg
    if enemyhp2 <= 0:
        enemydmg2 -= enemydmg2



    if HP <= 0 and enemyhp <=0:
        messagebox.showinfo("Dead", "You killed the bandits but their final blow made you bleed out and die.")
        break

    if enemyhp <= 0 and enemyhp2 <= 0:
        messagebox.showinfo("Enemies Killed", "You have defeated the bandits!"
                                              " Great job {} is now wanted for murder because the bandits were homeless people begging for food not robbers and this isn't medieval Europe,you can't just kill people...".format(player))

        break

    if HP <= 0 or choice =="no":
        messagebox.showinfo("{} is dead".format(player), "You greatly underestimated the bandits and they killed you. What were you thinking?".format(player))
        
        
        break














