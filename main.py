from noise import pnoise2
import sys
import time
import random
def spawn(spawnrange):
  return(random.randint((spawnrange*-1 ), spawnrange))
#this is the world genartor using perlin noise
world = []
"""
def clear():
  #this is to clear the line
  print("                                   ")
  sys.stdout.write(u"\u001b[1A")
  sys.stdout.write(u"\u001b[1000D")
"""
def clean():
  #this whole part is to wipe the screen to make it look good
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[1000D")
        print("                                   ")
        print("                                   ")
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[1A")
        sys.stdout.write(u"\u001b[1000D")

energy = 100
def worldgen(x,y,seed):
  #this is some code i got in order toit get vaules via pnoise2, it is a simple algorwith that helps and such
 tile = (pnoise2(x/seed,y/seed,2))
  #gen's a vaule from -1 to 1

 #this checks to see if player is in range of spawn this uses pyshics vectors to do the maths to find out if it is
 #vector = 1 #this is for testing purposes
 biome = (pnoise2(x/(seed*10),y/(seed*10),2))
 if biome > 0.3:#acrapellgo
  if tile > 0.10:
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
     return("=")
   elif tile > -0.1:
     return ("/")
   elif tile > -0.3:
     return ("|")
   else:
     return(".")
 else: # just ocean
  if tile > 0.3:
    return ("/") # this should try to resemble some ice bergs or something
  else:
   return("-")

#### MAIN LOOP ####

#seed effects the sises of the islands and such
spawnrange = 1 # this is how random-ness works for this program as the vaule x and y determins the seed so by having a massive range the randomness is increseed
#this makes it so that the player has the same map but has a diffrent spawn region each time
seed = 15
x = spawn(spawnrange)
y = spawn(spawnrange)




# this just gets the render sise
rendersise = input("choose render sise, and please have it as an even number ")
try:
  rendersise = int(rendersise)
except:
  print("not a int, setting to 30")
  rendersise = 30 
if rendersise % 2 == 0:
  pass
else:
  rendersise += 1
  print("number was not even, adding one to it to fix this")
  time.sleep(1)
maxy = rendersise
maxx = rendersise
posx = x
posy = y
xdone = 0
ydone = 0
spawnrange = 1

while True:
 sys.stdout.write("\033[0;0f")
 #posx -= 1 #this is for testing this moves to left
 #posy += 1
 x = posx
 y = posy
 ydone = 0
 xdone = 1
 #rendering
 while True:
   #this is all the vaules for the rending color,   
  land = worldgen(x,y,seed)
  if ydone == 0:
    sys.stdout.write(u"\u001b[41m  ")#red
  elif ydone == (maxy-1):
    sys.stdout.write(u"\u001b[41m  ")#red
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
    sys.stdout.write(u"\u001b[40m  ") #black
  elif land == "x":
    sys.stdout.write(u"\u001b[43;1m  ") # yellow
  elif land == "H":
    sys.stdout.write(u"\u001b[43m  ") #diffrent shade of yellow but i dont think it works in repl.it
    
  else:
    sys.stdout.write(u"\u001b[44m  ")
  #this is when libne hits the 30th pixal
  if xdone == (maxx): #= 30
    #drops down to the bigeiing of the nest line so that the sising code works
    sys.stdout.write(u"\u001b[1000D")
    sys.stdout.write(u"\u001b[1B")
    x = posx
    xdone = 0
    ydone += 1
    y += 1
  if ydone == (maxy):
    sys.stdout.write(u"\u000b")
    # brings the cursor to the start.
    #finsihs when this fully renders(there seems to be a glitch with the render)
    sys.stdout.write(u"\u001b[0m")
    action = input("what do you want to do ")
    if action == "move": # this is the module for getting the player to move

      #clear()
      while True:
       if energy == 0:
         print("to tired to move, you have died.")
         exit()
       else:
          ree = 1
       try:
        distance = int(input("now far "))
        break
       except:
        print("not a str")
        time.sleep(1)
        clean()
      if distance > 10:
        print("to far moving by ten")
        time.sleep(1)
        distance = 10
        print("")
        clean()
      move = input("where? ")
      if move == "up":
        posy -= distance
      elif move == "down":
        posy += distance
      elif move == "left":
        posx -= distance
      elif move == "right":
        posx += distance
      clean()
      clean()
      energy -= distance
    elif action == "sleep":
     backupx = posx
     backupy = posy
     posx = (rendersise/2) + posx
     posy = (rendersise / 2) + posy
     if worldgen(x,y,seed) == "+":
      sleep = 50
      print("you feel better")
      time.sleep(1)
      clean()
     else:
       print("cant sleep, need to be on grass to sleep")
       time.sleep(1)
       clean()
     posx = backupx
     posy = backupy

    else:
      print("please retry")
      time.sleep(1)
      clean()
    print("your energy is ", energy)
    time.sleep(1)
    clean()
    break
  x += 1
  xdone += 1
  #this starts work on the next pixal


