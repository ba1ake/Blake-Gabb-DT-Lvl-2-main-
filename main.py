import sys
import time
import random
from os import system
from functions import renderscreen
from functions import worldgen
from functions import gameover
#makes the AIs list
#to do
#fix sleeping, fixed i think, i might even remove it
playerdata = [[0,0],[0,0,0,0,0]] # this stores the player data in two sets
#the first list will be player exploring, there will be xp gained and distance travled
# the second list will be upgrades done, items mined, items fishe
#some functions remain in this file


def spawn(spawnrange):
  return(random.randint((spawnrange*-1 ), spawnrange))
  #this gens the spawn area to a range set.
#this is the world genartor using perlin noise
def clean():
  #this whole part is to wipe the screen to make it look good
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[2K")#wipes line
energy = 50
#### MAIN LOOP ####
spawnrange = 0
seed = 10
x = spawn(spawnrange)
y = spawn(spawnrange)
rendersise = 20
maxy = rendersise
maxx = rendersise
posx = x
posy = y
xdone = 0
ydone = 0
food = 1
scrap = 0
foodcap = 5
movedis = 10
energyrestore = 10
xp = 99
stone = 0
iron = 0
aialive = [0,0,0]
aisx = []
aisy = []
#even numbers IE 2,4,6 will be things that attack fast
#odd nubers will be things that can not see oyu at ling ranges.
# threses will be gened at random given the diffacty mutiplyer
# ^ all the above info is only run twice and is info for the game to int
while True:
  if aialive < 0:
    aialive += 1
    aix = 0
    aiy = 0
  if aialive == 0:
   aix = random.randint(1,20)
   aix += posx
   aiy = random.randint(1,20)
   aiy += posy
   print("ai respawned")
   time.sleep(2)
   aialive = 1

  renderscreen(x,y,rendersise,posx,posy,maxy,maxx,aialive,aix,aiy,playerdata)
  #this is the code for the th8ingy to move his pos
  if aix > (0.5 * rendersise):
    aix -= 1
  elif aix < (0.5 * rendersise):
    aix += 1
  else:
    if aiy > (0.5 * rendersise):
      aiy -=1
    elif aiy < (0.5 * rendersise):
      aiy+= 1
    else:
      print()
  if aiy > 20 or aiy < -20:
   if aialve > 0:
    aialive = -5
    print("ai lost")
  elif aix > 20 or aix < -20:
   if aialve > 0:
    aialive = -5
    print("ai lost")
  else:
    aialive = 1
    #render funtion
  sys.stdout.write(u"\u000b")
  sys.stdout.write(u"\u001b[0m") #stops color
  action = input("what do you want to do: ")
  if action == "help":
    print("the commands are, sleep, eat, xp, fish, help, mine, move, and quit but we dont quit")

  elif action == "move": 
      while True: #this is a while true loop as i can use it to auto exit a secton and skip the other parts which a normal thign wont be able to do
       if energy <= 0:
         print("you have run out of enegry, GAME OVER")
         time.sleep(2)
         gameover(playerdata)
       try:
        distance = int(input("how far: "))
        break
       except:
        print("not a int")
        time.sleep(1)
        clean()
      if distance > movedis:
        print("to far, moving by", movedis)
        time.sleep(1)
        distance = movedis
        
        print("")
        clean()
      move = input("where?: ")
      if move == "up":
        posy -= distance 
        aiy += distance
      elif move == "down":
        posy += distance
        aiy -= distance
      elif move == "left":
        posx -= distance
        aix += distance
      elif move == "right":
        posx += distance
        aix -= distance
      else:
        print("invaild direction")
        time.sleep(2)
        # this is so that the energy stays the same
        distance = 0
      clean()
      clean()
      if distance < 0:
        distance = distance * -1
      else:
        ree = 0
  
      energy -= distance
      playerdata[0][0] += distance 
  elif action == "sleep":
     backupx = posx
     backupy = posy
     x = (rendersise/2) + posx
     y = (rendersise / 2) + posy #this gets where the player should be
     if worldgen(x,y,seed) == "+": # if its grass he can sleep
      energy = 50
      print("you feel better")
      time.sleep(1)
      clean()
     else: # if not grass he cant sleep
       print("cant sleep, need to be on grass to sleep")
       time.sleep(1)
       clean()
     posx = backupx
     posy = backupy
  elif action == "fish":
     food_or_scrap = random.randint(1,4) # this gets a rng vaule for what the item fished up will be
     if food > foodcap:
       print("you have to many fish")
       time.sleep(1)
       clean()
     backupx = posx
     backupy = posy
     x = (rendersise/2) + posx # this gets the middle point of the screen
     y = (rendersise / 2) + posy
     if worldgen(x,y,seed) == "." or worldgen(x,y,seed) == "-":
       if food_or_scrap == 4:
        print("you didnt catch a fish but got some scrap")
        scrap +=1
        playerdata[1][4] += 1 # adds to the scrap pver all count
        time.sleep(1)
        clean()
       else:
        print("you fished and caught a fish, congrats")
        time.sleep(1)
       xp += 1
       playerdata[0][1] += 1 # adds xp count
       playerdata[1][3] += 1 # adds to the fished pver all count
       clean()
       food +=1
       energy -= 1
       posy = backupy
       posx = backupx
       # restets all the pos's and does the energy stuff
     else:
       print("fun fact, fishing with out water is somewhat hard to do")
       time.sleep(2)
       clean()
     posx = backupx
     posy = backupy
  elif action == "eat": #this is if the player has food and if so lets them reafina some energy back from it but no more than 50
      if food > 0:
        print("you have eaten some food, you have regained some energy")
        energy += energyrestore
        time.sleep(1)
        food -= 1
        clean()
        if energy > 50:
          energy = 50 # this is to make sure the player cant have more than 50 energy at one time
          
        else:
          print("you ate some food but you were already full")
          time.sleep(1)
          clean()
      else:
        print("you know, you can really eat food thats not there. Right?")
        time.sleep(1)
        clean()
  elif action == "xp":
    clean()
    print("you have", xp,"xp, it costs 25 to upgrade")
    time.sleep(2)
    if xp < 25:
      print("you do not have enough to upgrade your skills")
      time.sleep(2)
    print()
    clean()
    option = input("press and enter 1 for max food, 2 for speed, or 3 for energy from food: ")
    time.sleep(1)
    print()
    clean()
    if xp > 25:
      if option == "1":
        print("max food cap has been upgraded to", foodcap + 1)
        time.sleep(1)
        clean()
        playerdata[1][0] += 1 # this addes one upgrade to the count
        foodcap += 1
        xp -= 25
      elif option == "2":
        print("you can now run", movedis + 2,"blocks")
        time.sleep(1)
        clean()
        movedis +=2
        playerdata[1][0] += 1 # this addes one upgrade to the count
        xp -= 25
      elif option == "3":
        energyrestore += 1
        print("food now restores", energyrestore, "energy")
        time.sleep(1)
        playerdata[1][0] += 1 # this addes one upgrade to the count
        clean()
        xp -= 25
      elif option == "exit":
        print('exiting')# this will exit the the upgrade menu
      else:
        ("invaild input, exiting from xp menu")
    else:
      print("closing menu. dont forget aswell, it takes 25 xp")
      time.sleep(2)
      clean()
    print("you now have ",xp, " xp remaining")# the resone for this being a fucntion is i might change how it is done so by having this as a function will make it eair to move it
  elif action == "mine":
     stoneoriron = random.randint(1,4)#gets wether or not its iron
     backupx = posx# backups pos's
     backupy = posy
     x = (rendersise/2) + posx
     y = (rendersise / 2) + posy#converts pos's to the players pos
     if worldgen(x,y,seed) == "|":#checks to see if its a ore rich block
       if stoneoriron == 4:
        print("you mined some iron, lucky")
        playerdata[1][1] += 1 # adds one to the iron count
        iron +=1
        xp += 4
        playerdata[0][1] += 4 # this way it adds up to 5 per iron xp-wise
        time.sleep(2)
        clean()
       else:
        print("you were able to mine some stone.")
        stone += 2
        playerdata[1][2] += 2 # adds 2 to the stone count overall
        time.sleep(2)
     xp += 1
     playerdata[0][1] += 1 # adds data to the muti dimsinal array, or list. what ever its called
     clean()
     posy = backupy
     posx = backupx
     if worldgen(x,y,seed) != "|":#CHECKS to see if its not an orerich stone
       print("you are not able to mine here")
       time.sleep(2)
       clean()
       energy += 5 # once agin to counter so no energy is used up
     posx = backupx#restores back up's
     posy = backupy
     energy -= 5
  elif action == "quit":
      gameover(playerdata) # plays the final scoreboard
  else:
      print("please retry") #this tells the player to try and reenter their input
      time.sleep(1)
      clean()
  if energy <= 0:
         print("you have run out of enegry, GAME OVER")
         time.sleep(2)
         gameover(playerdata)
  print("your energy is ", energy)
  time.sleep(1)
  clean()
  system('clear')#this wipes screen for next render


