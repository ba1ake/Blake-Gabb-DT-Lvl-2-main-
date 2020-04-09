from noise import pnoise2
import sys
import time
import random
from os import system
# to do
#fix sleeping, fixed i think, i might even remove it
playerdata = [[0,0],[0,0,0]]
#the first list will be player exploring, there will be xp gained and distance travled
# the second list will be upgrades done, items mined, items fished,






def spawn(spawnrange):
  return(random.randint((spawnrange*-1 ), spawnrange))
  #this gens the spawn area to a range set.
#this is the world genartor using perlin noise
def clean():
  #this whole part is to wipe the screen to make it look good
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[2K")#wipes line
energy = 50
def worldgen(x,y,seed):
  #this is some code i got in order toit get vaules via pnoise2, it is a simple algorwith that helps and such
 tile = (pnoise2(x/seed,y/seed,2))
  #gen's a vaule from -1 to 1

 #this checks to see if player is in range of spawn this uses pyshics vectors to do the maths to find out if it is
 #vector = 1 #this is for testing purposes
 biome = (pnoise2(x/(seed*10),y/(seed*10),2))
 if biome > 0.3:#acrapellgo
  if tile > 0.20:
    return("+")
  else:
    print(".")
 if biome > -0.1:#grassssssssssss
  if tile > 0.35:
    return("/")
  elif tile > 0.10:
    return("|")
    #if vaule is .6 - 1 it is a mountain
  elif tile > -0.3: # if it ='s it will be land
    return("+")
  
    #if vaule is .1 - .6
  elif tile > -0.4: # will be light water
    return(".")
    #if vaule is .3 - .3 it is light water
    #lower vaules are deep water
 elif biome > -0.3: #hilly boi biome

   if tile > .10:
     return("=") #edges of moutain
   elif tile > -0.1:
     return ("/") #black
   elif tile > -0.3:
     return ("|") # black
   else:
     return(".")
 else: # just ocean
  if tile > 0.3:
    return ("/") # this should try to resemble some ice bergs or something
  else:
   return("-")
def upgrades(xp,foodcap,movedis, energyrestore):
  clean()
  print("you have", xp,"xp, it costs 25 to upgrade")
  time.sleep(2)
  print()
  clean()
  option = input("press and enter 1 for max food, 2 for speed, or 3 for energy from food ")
  time.sleep(1)
  print()
  clean()
  if xp > 25:
    if option == "1":
      print("max food cap has been upgraded to", foodcap + 1)
      time.sleep(1)
      clean()
      foodcap += 1
      xp -=25
    elif option == "2":
      print("you can now run", movedis + 2,"blocks")
      time.sleep(1)
      clean()
      movedis +=2
      xp -= 25
    elif option == "3":
      energyrestore += 1
      print("food now restores", energyrestore, "energy")
      time.sleep(1)
      clean()
      xp -= 25
    elif option == "exit":
      print('exiting')
      return
    else:
      ("invaild input, exiting from xp menu")
      return
  else:
    print("you dont have enough xp to upgrade a skill, move around and do stuff to gain xp.")
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
clean()
try:
  rendersise = int(rendersise)
except:
  print("not a int, setting to 20")
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
iron = 1
#the main bit
while True:
 sys.stdout.write("\033[0;0f")#puts the curser at top of screen
 x = posx
 y = posy
 ydone = 0
 xdone = 1
 #rendering
 while True:
   #this is all the vaules for the rending color, 
  land = worldgen(x,y,seed)
  if ydone == (0.5 * rendersise) and xdone == (0.5 * rendersise):
    sys.stdout.write(u"\u001b[41m  ")
  elif ydone == 0:
    sys.stdout.write(u"\u001b[41m  ")#red for border
  elif ydone == (maxy-1):
    sys.stdout.write(u"\u001b[41m  ")#red for border
  elif xdone == (maxx):
    sys.stdout.write(u"\u001b[41m  ")#red
  elif land == "+":
     sys.stdout.write(u"\u001b[42m  ")#green
     #this checks to see if it needs to re render the color
  elif land == "=":
    sys.stdout.write(u"\u001b[40m  ")#black
  elif land == "/":
     sys.stdout.write(u"\u001b[47m  ")#white
  elif land == ".":
    sys.stdout.write(u"\u001b[46m  ")#cyan
  elif land == "|":
    # gonna make this mineable blocks, so some rock can be mined at a better rate than others, and these ones have the possbliy to drop more iron, which will then be used to excape, and then maybe add a diffrent world you go to
    sys.stdout.write(u"\u001b[40m::") #black
  elif land == "x":
    sys.stdout.write(u"\u001b[43;1m  ") # yellow
  elif land == "H":
    sys.stdout.write(u"\u001b[43m  ") #diffrent shade of yellow but i dont think it works in repl.it  
  else:
    sys.stdout.write(u"\u001b[44m  ")
  #this is when line hits the 30th pixal
  if xdone == (maxx): # goes to next line
    #drops down to the bigeiing of the nest line so that the render sising code works
    sys.stdout.write(u"\u001b[1000D")
    sys.stdout.write(u"\u001b[1B")
    x = posx
    xdone = 0
    ydone += 1
    y += 1
  if ydone == (maxy): # this is when the whole thing has rendered and contains options like moveing, sleeping, maybe eating at some point
    sys.stdout.write(u"\u000b")
    # brings the cursor to the start.
    #finsihs when this fully renders(there seems to be a glitch with the render) fixxed
    sys.stdout.write(u"\u001b[0m")
    action = input("what do you want to do ")
    if action == "move": # this is the module for getting the player to move

      #clear()
      while True: #this is a while true loop as i can use it to auto exit a secton and skip the other parts which a normal thign wont be able to do
       if energy <= 0:
         print("you have run out of enegry, GAME OVER")
         exit()
       else:
          ree = 1
       try:
        distance = int(input("now far "))
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
      move = input("where? ")#all the vaild options
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
        energy += distance# this is so that the energy stays the same
      clean()
      clean()
      if distance < 0:
        distance = distance * -1
      else:
        ree = 0 # this is ment to just pass this with out issues
  
      energy -= distance
      
      #this makes them only able to wal a curtain distance 
    elif action == "sleep": #see if can sleep
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
     food_or_scrap = random.randint(1,4)
     if food > foodcap:
       print("you have to many fish")
       time.sleep(1)
       clean()
       break
     backupx = posx
     backupy = posy
     x = (rendersise/2) + posx
     y = (rendersise / 2) + posy
     if worldgen(x,y,seed) == "." or worldgen(x,y,seed) == "-":
       if food_or_scrap == 4:
        print("you didnt catch a fish but got some scrap")
        scrap +=1
        time.sleep(1)
        clean()
       else:
        print("you fished and caught a fish, congrats")
        time.sleep(1)
       xp += 1
       clean()
       food +=1
       posy = backupy
       posx = backupx
     else:
       print("fun fact, fishing with out water is somewhat hard to do")
       time.sleep(2)
       clean()
       xp += 1
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
          energy = 50
      else:
        print("you know, you can really eat food thats not there. Right?")
        time.sleep(1)
        clean()
    elif action == "xp":
      upgrades(xp,foodcap,movedis,energyrestore)
      print("you now have ",xp, " xp remaining")# the resone for this being a fucntion is i might change how it is done so by having this as a function will make it eair to move it
    elif action == "mine":
     stoneoriron = random.randint(1,4)#gets wether or not its iron
     backupx = posx# backups pos's
     backupy = posy
     x = (rendersise/2) + posx
     y = (rendersise / 2) + posy#converts pos's to the players pos
     if worldgen(x,y,seed) == "|":#checks to see if its a ore rich block
       if stoneoriron == 4:
        print("you found some iron, lucky")
        iron +=1
        xp += 4 # this way it adds up to 5 per iron
        time.sleep(1)
        clean()
       else:
        print("you were able to find some stone.")
        time.sleep(1)
     xp += 1
     clean()
     stone +=1
     posy = backupy
     posx = backupx
     if worldgen(x,y,seed) != "|":#CHECKS to see if its not an orerich stone
       print("you are not able to mine here")
       time.sleep(2)
       clean()
       energy += 1 # once agin to counter so no energy is used up
     posx = backupx#restores back up's
     posy = backupy
     energy -= 1
    else:
      print("please retry")
      time.sleep(1)
      clean()
    print("your energy is ", energy)
    time.sleep(1)
    clean()
    system('clear')#this wipes screen for next render
    break
  x += 1
  xdone += 1
  #this starts work on the next pixal


