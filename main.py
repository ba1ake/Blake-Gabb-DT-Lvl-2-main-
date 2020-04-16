import sys
import time
import random
from os import system
from functions import renderscreen
from functions import worldgen
from functions import gameover
# to do
#fix sleeping, fixed i think, i might even remove it
playerdata = [[0,0],[0,0,0,0,0]] # this stores the player data in two sets
#the first list will be player exploring, there will be xp gained and distance travled
# the second list will be upgrades done, items mined, items fished,
print("welcome to my game, first things first this is a survial game, it is text based so you, the player, will have to enter text commands to make your player move,")
time.sleep(4)
input("press enter when ready...")
system("clear")
print("there are diffrent tpyes of blocks, green blocks are grass, they let you sleep on them, grey blocks are stone, you can not sleep on them. If they have a '::' pattern on them then you are able to mine on them and get iron or stone, light blue blocks is shallow water, and dark blue blocks is deep water, on both of these tiles you are able to fish for, well, fish, and finally white tiles are snow. your player is shown by the red pixal in the center of the screen")
time.sleep(4)
input("press enter when ready...")
print("the commands are, move, eat, fish, xp, and sleep")
input("press enter when ready to start...")
system("clear")
# that was the intro



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
def upgrades(xp,foodcap,movedis, energyrestore):
  clean()
  print("you have", xp,"xp, it costs 25 to upgrade")
  time.sleep(2)
  if xp < 25:
    print("you do not have enough to upgrade your skills")
    time.sleep(2)
    return("2")
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
      return ("1")
    elif option == "2":
      print("you can now run", movedis + 2,"blocks")
      time.sleep(1)
      clean()
      movedis +=2
      playerdata[1][0] += 1 # this addes one upgrade to the count
      return ("1")
    elif option == "3":
      energyrestore += 1
      print("food now restores", energyrestore, "energy")
      time.sleep(1)
      playerdata[1][0] += 1 # this addes one upgrade to the count
      clean()
      return ("1")
    elif option == "exit":
      print('exiting')
      return("2")# this will exit the the upgrade menu
    else:
      ("invaild input, exiting from xp menu")
      return "2"
  else:
    print("closing menu. dont forget aswell, it takes 25 xp")
    time.sleep(2)
    clean()
#### MAIN LOOP ####
#seed effects the sises of the islands and such
spawnrange = 999999 # this is how random-ness works for this program as the vaule x and y determins the seed so by having a massive range the randomness is increseed
#this makes it so that the player has the same map but has a diffrent spawn region each time
seed = 10
x = spawn(spawnrange)
y = spawn(spawnrange)
# this just gets the render sise and makes sure its in the paramters of spawn range and not an odd number
rendersise = input("choose render sise, and please have it as an even number ")
system("clear")
try:
  rendersise = int(rendersise)
except:
  print("not a int, setting to 20") # this is a good defult sise that i found to work very well, sometimes repl mess;s up tho
  rendersise = 20
  time.sleep(2)
  clean()
if rendersise % 2 == 0:
  pass
else:
  rendersise += 1
  print("number was not even, adding one to it to fix this")
  time.sleep(2)
  clean()
  system('clear')
# the number has to be even so that way when the border is taken off there is a uneven number of squares so there is a center point
# just some stuff
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
xp = 0
stone = 0
iron = 0
while True:
  renderscreen(x,y,rendersise,posx,posy,maxy,maxx)
  sys.stdout.write(u"\u000b")

    # brings the cursor to the start.
    #finsihs when this fully renders(there seems to be a glitch with the render) fixxed
  sys.stdout.write(u"\u001b[0m") # trues off color
  action = input("what do you want to do: ")
  if action == "help":
    print("the commands are, sleep, eat, xp, fish, help, mine, move, and quit but we dont quit")

  elif action == "move": # this is the module for getting the player to move

      #clear()
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
      if distance > movedis: #this makes sure the player doesnt go to far
        print("to far, moving by", movedis)
        time.sleep(1)
        distance = movedis
        
        print("")
        clean()
      move = input("where?: ")#all the vaild options
      if move == "up":
        posy -= distance 
      elif move == "down":
        posy += distance
      elif move == "left":
        posx -= distance
      elif move == "right":
        posx += distance
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
        ree = 0 # this is ment to just pass this with out issues
  
      energy -= distance # that way the energy useage is based of of player movement

      playerdata[0][0] += distance#distance travled
      #this makes them only able to wal a curtain distance 
  elif action == "sleep": #see if can
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
      if upgrades(xp,foodcap,movedis,energyrestore) == "1":
        xp -= 25
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
     playerdata[0][1] += 1
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
      gameover(playerdata)
  else:
      print("please retry")
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


