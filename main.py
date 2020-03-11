from noise import pnoise2
import sys
import time
import random
def spawn(spawnrange):
  return(random.randint((spawnrange*-1 ), spawnrange))
#this is the world genartor using perlin noise
world = []
def worldgen(x,y,seed):
  #this is some code i got in order toit get vaules via pnoise2, it is a simple algorwith that helps and such
 tile = (pnoise2(x/seed,y/seed,2))
  #print(tile)
  #gen's a vaule from -1 to 1

 #this checks to see if player is in range of spawn this uses pyshics vectors to do the maths to find out if it is
 #vector = 1 #this is for testing purposes
 biome = (pnoise2(x/(seed*10),y/(seed*10),2))
 if biome > 0:
  if tile > 0.25:
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
 elif biome > -0.5: #sand biome

   if tile > 0.2:
    return("H")
   elif tile > -0.3:
     return("x")
   elif tile > -0.5:
     return (".")
   else:
     return("-")
 else:
   return("-")

    
   

#seed effects the sises of the islands and such
spawnrange = 99999 # this is how random-ness works for this program as the vaule x and y determins the seed so by having a massive range the randomness is increseed
#this makes it so that the player has the same map but has a diffrent spawn region each time
seed = 22
x = spawn(spawnrange)
y = spawn(spawnrange)
maxy = 31# rendering sise for x axis
# rend5ering sise for x axis
maxx = 31 #be +1 from wanted sise for border rendering sise for y axis
posx = x
posy = y
xdone = 0
ydone = 0
spawnrange = 100

while True:
 sys.stdout.write("\033[0;0f")
 posx -= 1 #this is for testing this moves to left
 posy += 1
 x = posx
 y = posy
 ydone = 0
 xdone = 1
 #rendering
 while True:
  land = worldgen(x,y,seed)
  if ydone == 0:
    sys.stdout.write(u"\u001b[41m  ")
  elif ydone == (maxy-1):
    sys.stdout.write(u"\u001b[41m  ")
  elif xdone == (maxx):
    sys.stdout.write(u"\u001b[41m  ")
  elif land == "+":
     sys.stdout.write(u"\u001b[42m  ")
     #this checks to see if it needs to re render the color
  elif land == "=":
    sys.stdout.write(u"\u001b[40m  ")
  elif land == "/":
     sys.stdout.write(u"\u001b[47m  ")
  elif land == ".":
    sys.stdout.write(u"\u001b[46m  ")
  elif land == "|":
    sys.stdout.write(u"\u001b[40m  ") 
  elif land == "x":
    sys.stdout.write(u"\u001b[43;1m  ") 
  elif land == "H":
    sys.stdout.write(u"\u001b[43m  ") 
    
  else:
    sys.stdout.write(u"\u001b[44m  ")
  #x+=1
  #this is when libne hits the 30th pixal
  if xdone == (maxx): #= 30
    #drops down to the bigeiing of the nest line so that the sising code works
    sys.stdout.write(u"\u001b[1000D")
    sys.stdout.write(u"\u001b[1B")
    x = posx
    xdone = 0
    ydone += 1
    y += 1
    #print(ydone)
    #time.sleep(1)
  if ydone == (maxy):
    # brings the cursor to the start.
    #finsihs when this fully renders(there seems to be a glitch with the render)
    #ree = input(""
    #print(x,y,vector,biome)
    """
    print(x)
    print(y)
    print(vector)
    print(biome)
    """
    break
  x += 1
  xdone += 1


