
import random
import os
nosee="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
#r1="Red - 1"



deck=[]

#def cards():
  #  print("This is card 1")
#This is the game set up code

os.system('clear')
print("\nUUUUU     UUUUU NNNNNNN   NNNNN OOOOOOOOOOOOOOO")
print("UUUUU     UUUUU NNNNNNN   NNNNN OOOOOOOOOOOOOOO")
print("UUUUU     UUUUU NNNNN NN  NNNNN OOOOO     OOOOO")
print("UUUUU     UUUUU NNNNN NN  NNNNN OOOOO     OOOOO")
print("UUUUU     UUUUU NNNNN  NN NNNNN OOOOO     OOOOO")
print("UUUUU     UUUUU NNNNN  NN NNNNN OOOOO     OOOOO")
print("UUUUU     UUUUU NNNNN   NNNNNNN OOOOO     OOOOO")
print("UUUUUUUUUUUUUUU NNNNN    NNNNNN OOOOO     OOOOO")
print("UUUUUUUUUUUUUUU NNNNN     NNNNN OOOOOOOOOOOOOOO")
print("UUUUUUUUUUUUUUU NNNNN     NNNNN OOOOOOOOOOOOOOO")

stall=input("             Press Enter to Begin")




os.system('clear')
print("Player Select: \n")
print("1: 1 Player\n\n\n")
#stall=input("Select Mode: ")
#Soon
print("WIP: 1 Player V.S. COM")
print("WIP: 2 Player")
print("WIP: 3 Player")
print("WIP: 99 Player")

class AllCard:

    def __init__ (self, color, number):
        self.color = color
        self.number = number

#This protion of the code creates the card values that I will be using
def assign():
    #Reds
    #The first number goes 0-10
    for x in range(10):
        C1= AllCard('Red', x)
        deck.append(C1)
    #The second code goes 1-10
    for x in range(1,10):
        C1= AllCard('Red', x)
        deck.append(C1)
    for x in range(2):
        C1= AllCard('Red', '+2')
        deck.append(C1)
    #Blues
    for x in range(10):
        C1= AllCard('Blue', x)
        deck.append(C1)
    for x in range(1,10):
        C1= AllCard('Blue', x)
        deck.append(C1)
    for x in range(2):
        C1= AllCard('Blue', '+2')
        deck.append(C1)
    #Yellows
    for x in range(10):
        C1= AllCard('Yellow', x)
        deck.append(C1)
    for x in range(1,10):
        C1= AllCard('Yellow', x)
        deck.append(C1)
    for x in range(2):
        C1= AllCard('Yellow', '+2')
        deck.append(C1)
    #Greens
    for x in range(10):
        C1= AllCard('Green', x)
        deck.append(C1)
    for x in range(1,10):
        C1= AllCard('Green', x)
        deck.append(C1)
    for x in range(2):
        C1= AllCard('Green', '+2')
        deck.append(C1)
    #Wilds
    for x in range(8):
        C1= AllCard("Wild", 'Wild')
        deck.append(C1)


    

assign()

#This small part makes the code so a normal human can read it
normalpersondeck=[]
for x in range(92):

    normalpersondeck.append((deck[x].color, deck[x].number))
    #print(deck[x].color, deck[x].number)
  #  stall=input("Stallin")
print(normalpersondeck)

print("\n\n\n\n\n\n\n\n")

#This makes a shuffled deck
deckvalues=[]
for x in range(92):
    deckvalues.append(x)
random.shuffle(deckvalues)
print(deckvalues)
#for z in range(76):
    #print(normalpersondeck[deckvalues[z]])


#THIS IS THE PART THAT SPLITS
#THIS IS THE PART THAT SPLITS
#Making this bigger so my bros can see it is.


#This part of the code will deal the cards.
hand=[]
comhand=[]
for a in range(0, 14, 2):
    hand.append(normalpersondeck[deckvalues[a]])
for a in range(1, 15, 2):
    comhand.append(normalpersondeck[deckvalues[a]])
#for a in range(len(hand)):
 #   hand[0]=1
topdeck=16
down=normalpersondeck[deckvalues[15]]

#This code sets up the game loop
gameloop=0
while gameloop == 0:
    if len(hand) == 1:
        os.system('clear')
        stall=input("Hit Enter to Say UNO!!!")
    elif len(hand) == 0:
        stall=input("You Win!")
        break
    else:
        pass
    #This part will probobly repeat at the start of every turn
    turndone=0
    grab=0
    while turndone==0:
        os.system('clear')
        #print(nosee)
        print("Your Hand: ")
        print("0 :  ( Draw )")
        for b in range(len(hand)):
            print(b+1,": ",hand[b])
    
        print("\nDown: ", down)
        print("Your opponent has",len(comhand),"cards")

        #if cardchoose is not int:
        #print(comhand)
        cardchoose=int(input("What card do you want to put down?: "))-1

        #This knifty code splits the text so we don't have to search for it
        #print(hand[cardchoose]
        os.system('clear')
        if cardchoose==-1:
            print("\n\n\n\n\nYou drew,", normalpersondeck[deckvalues[topdeck]], "out of the deck")
            stall=input("<><><>Hit Enter To Go Back<><><>")
            hand.append(normalpersondeck[deckvalues[topdeck]])
            topdeck+=1
            turndone=1
            grab=1
        else:
            cardinfo=str(hand[cardchoose]).split(",")
            downcardinfo=str(down).split(",")


            if cardinfo[0]== "(\'Wild\'":
               # print("Epic")
                print("What Color Do you want?")
                colorlist=["Red","Blue","Yellow","Green"]
                print("\n1: Red\n2: Blue\n3: Yellow\n4: Green")
                colorchoose = input("What Color: ")
                turndone=1
                cardinfo[0] = "(\'"+str(colorlist[int(colorchoose)-1])+"\'"
                hand[cardchoose] = cardinfo[0]+","+cardinfo[1]
                os.system('clear')
            elif cardinfo[1]==downcardinfo[1]:
            # print("It works by same num")
                turndone=1
            elif cardinfo[0]==downcardinfo[0]:
            # print("It works by same color")
                if cardinfo[1] == " \'+2\')":
                    for z in range(2):
                        comhand.append(normalpersondeck[deckvalues[topdeck]])
                        topdeck+=1
                else:
                    pass
                turndone=1
            #This is the wild check code
            else:
                print("This does not work, choose another card or draw")
                turndone=0
                stall=input("<><><>Hit Enter To Go Back<><><>")

    if grab == 1:
        pass
   # if cardinfo[1] == '+2' and cardinfo[0]==downcardinfo[0]:
    #    print("\nThe other player gained 2 cards* WIP")
    else:   
        print("\n\n\n\n\n\n\nYou put", hand[cardchoose], "down")
        down = hand[cardchoose]
        hand.pop(cardchoose)
        #print(down)
        stall=input("\n<><><><><> Hit Enter To Continue <><><><><>")
    #This is the code for the COM's turn
    turndone=0
    comgrab=0
    print(comhand)

    for a in range(len(comhand)-1):
        cardinfo=str(comhand[a]).split(",")
        downcardinfo=str(down).split(",")
        
        #TAKE DIS PART OUT
       # print("\n",cardinfo,"\n",downcardinfo)
       # stall=input("MEME")

        #This is the wild check code
        if cardinfo[0]== "(\'Wild\'":
            # print("Epic")
            print("What Color Do you want?")
            colorlist=["Red","Blue","Yellow","Green"]
          #  print("\n1: Red\n2: Blue\n3: Yellow\n4: Green")
            colorchoose = random.randrange(1,4)

            turndone=1
            cardinfo[0] = "(\'"+str(colorlist[int(colorchoose)-1])+"\'"
            comhand[cardchoose] = cardinfo[0]+","+cardinfo[1]
            os.system('clear')
            break
        elif cardinfo[1]==downcardinfo[1]:
        # print("It works by same num")
            turndone=1
            break
        elif cardinfo[0]==downcardinfo[0]:
        # print("It works by same color")
            if cardinfo[1] == " \'+2\')":
                for z in range(2):
                    hand.append(normalpersondeck[deckvalues[topdeck]])
                    topdeck+=1
                    break
            else:
                break
            turndone=1
        else:
            pass
    if turndone == 0:
        comhand.append(normalpersondeck[deckvalues[topdeck]])
        topdeck+=1
        comgrab=1
    else:
        pass
            
    os.system('clear')
    if comgrab == 1:

        print("\n\n\nThe computer drew a card")
    else:
        print("\n\n\n\n\n\n\nThe Computer put", comhand[cardchoose], "down")
        down = comhand[cardchoose]
        comhand.pop(cardchoose)
        

    stael=input("\n<><><><><> Hit Enter To Continue <><><><><>")
        


















stop=input("\nThis is the End of the Game! Restart the code to try again!")
