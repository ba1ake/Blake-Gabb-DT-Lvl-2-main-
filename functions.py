from noise import pnoise2
import sys
import time
from os import system
import random
seed = 10
#this list manying has getting the game to work while the game holds funtoins in realtion to the games fetures and design
def worldgen(x,y,seed):
  #this is some code i got in order toit get vaules via pnoise2, it is a simple algorwith that helps and such
 tile = (pnoise2(x/seed,y/seed,2))
  #gen's a vaule from -1 to 1

 #this checks to see if player is in range of spawn this uses pyshics vectors to do the maths to find out if it is
 #vector = 1 #this is for testing purposes
 biome = (pnoise2(x/(seed*10),y/(seed*10),2))
 if biome > 0.3:#acrapellgo
  if tile > 0.20:
    return("+") #grass
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
  else:
    return("-")
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
def renderscreen(x,y,rendersise,posx,posy,maxy,maxx,aialive,aix,aiy,playerdata):
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
   #print((xdone + x), (ydone + y))
   #print(aix, aiy)
   if aix == (0.5 * rendersise) and aiy == (0.5 * rendersise):
     gameover(playerdata)
   if ydone == (0.5 * rendersise) and xdone == (0.5 * rendersise):
    sys.stdout.write(u"\u001b[41m**") # the player
   elif xdone == aix and ydone == aiy:
     sys.stdout.write(u"\u001b[43m++")
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
   elif land == "-":
    sys.stdout.write(u"\u001b[44m  ")
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
   if ydone == (maxy):
     return() 
   else:
       x += 1
       xdone += 1
def gameover(playerdata):
  system('clear')
  print("you have died")
  time.sleep(2)
  print("you traveled over ", playerdata[0][0], " blocks over all")
  #this section gets all the data from the muti dimesion array and then prints it as a score board for the player and then uses it to get an over all score, it is dont as a function as there is two ways of getting the game over
  time.sleep(2)
  print("you gained ", playerdata[0][1], " xp")
  time.sleep(2)
  print("you fished ", playerdata[1][3], " fishs")
  time.sleep(2)
  print("you found ", playerdata[1][4], " scrap")
  time.sleep(2)
  print("you gained ", playerdata[1][0], " upgrades")
  time.sleep(2)
  print("you mined ", playerdata[1][1], " iron")
  time.sleep(2)
  print("you mined ", playerdata[1][2], " stone")
  time.sleep(2)
  print("this gives you a grand total of...")
  score = ((playerdata[0][0]) +(playerdata[0][1])) # xp plus movement
  score += ((playerdata[1][0])* 10)
  score += ((playerdata[1][1]) * 2)
  score += (playerdata[1][2])
  score += ((playerdata[1][3])*2)
  score += ((playerdata[1][4])*5)
  #this is all the vaules added up to be the score
  print("your overall score is...")
  time.sleep(1)
  if score == 0:
    print("you have 0 score.")
    time.sleep(2)
    input("press enter to exit")
    exit()
  for i in range(0, score):
    sys.stdout.write(u"\u001b[1000D")
    sys.stdout.flush()
    sys.stdout.write(str(i + 1))
    sys.stdout.flush()
    time.sleep(0.1)
  print("!")
  time.sleep(2)
  input("press enter to exit")
  exit()





