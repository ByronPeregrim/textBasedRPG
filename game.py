import time
import sys

wallet = [];

# Create Player class. Contains players name, level, health status, inventory, and amount of gold pieces.
class Player:
    def __init__(self, playerName, level, health, inventory, gold):
        self.playerName = playerName;
        self.health = health;
        self.level = level;
        self.inventory = inventory;
        self.gold = gold;

# Class for items. Contains item description string and int with value of item.
class Item:
    def __init__(self, name, itemDescription, value):
        self.name = name;
        self.itemDescription = itemDescription;
        self.value = value;

# Function to slow text display
def text(text):
    for l in text:
        sys.stdout.write(l);
        sys.stdout.flush();
        time.sleep(0.05);
    print("");
    print("");
    time.sleep(1);

# Function to slow text display even more
def slowText(text):
    for l in text:
        sys.stdout.write(l);
        sys.stdout.flush();
        time.sleep(0.3);
    print("");
    print("");


def usePotion():
    if potion in player.inventory:
        player.health = 100;
        player.inventory.remove(potion);
        text("You drink the potion. Your health is fully restored.");
    else:
        text("You do not have any potions in your inventory.");


# General player commands
def playerCommands():
    commandExecuted = False;
    while commandExecuted == False:
        command = input("Enter Command: ").lower();
        if command == "health":
            getHealth();
            break;
        elif command == "open inventory":
            getInventory();
            break;
        elif command == "open wallet":
            getGoldPieces();
            break;
        elif command == "use potion":
            usePotion();
            break;
        else:
            commandExecuted == False;

# Displays player inventory
def getInventory():
    print("--Item---------------|--Description---------------------------------------|--Value----");
    for i in player.inventory:
        print(f'{i.name:20} | {i.itemDescription:50} | {i.value:6d}gp');
    print("--------------------------------------------------------------------------------------");
    print("");

# Displays number of gold pieces in player wallet
def getGoldPieces():
    text("You have " + str(player.gold) + " gold pieces.");

# Displays players health status
def getHealth():
    text("Your health is at " + str(player.health) + "%.");



# ITEMS
potion = Item("Potion", "A health potion. Fully restores health.", 30);
woodenStick = Item("Wooden stick", "A wooden stick.", 0);
nail = Item("Nail", "A rusty nail.", 1);


# Introduction text
print("");
text("You wake up on the floor of a damp cave...")
text("A small fire crackles a few feet away...") 
text("Next to the fire sits a middle-aged man. A walking stick rests upon his knees....");
time.sleep(1.5);
text("He notices you are awake and gives you a small, knowing smile...")
time.sleep(1.5);
text("He begins to speak...")
text("'You've been sleeping for quite some time...'");
time.sleep(1.5);
text("'You probably don't remember much, do you?'");

response1 = (input("Respond: [Yes/No] ")).lower();
print("");

# First response to a question.
if response1 == "yes":
    text("'Really? That's shocking. You suffered quite a blow to the head.'");
elif response1 == "no":
    text("'I'm not surprised. You suffered quite a blow to the head.'");
else:
    text("'I'm not quite sure what you said. That blow to the head may have been worse than I thought...'");

text("'Do you remember your name?'")

playerName = input("Enter Name: ");

# Create player object
player = Player(playerName, 1, 75, [], 0);

print("");
time.sleep(1.5);

text("'Good... Hello, " + playerName + "'");
time.sleep(1.5);
slowText(".....");
text("'I can see that you're wondering where you are and how you got here...'")
time.sleep(1.5);
text("'Hmm, you really don't remember anything, do you?'")
time.sleep(1.5);
text("'I hate to be the one to tell you this, but...'");
time.sleep(1.5);
text("'Your village was attacked last night...'");
time.sleep(1.5);
text("'I found you this morning, unconcious, at the bottom of a hill just outside the village.'");
time.sleep(1.5);
text("'There was a big gash to the back of your head. I was able to stitch it up, but you're going to want to keep an eye on that.'");
time.sleep(1.5);
text("You bring your fingers to the back of your head and quickly find the wound. You wince in pain as you graze the sensitive tissue.");
time.sleep(1.5);
print("");

answer = False
while (answer == False):
    response = input("Respond: [Who are you?/Remain silent] ").lower()
    if response == "who are you?" or response == "who are you":
        time.sleep(1.5);
        text("'I'm nobody. Just a traveling merchant who happened to be in the right place at the right time.'")
        break;
    elif response == "remain silent":
        slowText(".....");
        time.sleep(1.5);
        break;
    else:
        answer = False;

print("");
text("'Anyways, how do you feel now?'");
text("To check health status type [health].");
playerCommands();

text("'Hmm, seems you still have a bit of a fever. Here. Take this potion. That should get you feeling like new again...'");
time.sleep(1);
text("The man's arm protrudes from his cloak. It extends. In his hand is a small flask with a viscous red liquid inside. ");
time.sleep(1);
text("You reach out and take the potion.");
player.inventory.append(potion);
time.sleep(1);

text("To check your inventory type [open inventory]. ");
playerCommands();

text("To use the potion type [use potion]. ");
playerCommands();

