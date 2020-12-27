import random
import colorama
from colorama import init, Fore, Back, Style
# Converts ANSI to ASCII for windows cmd prompt. 
init(convert=True)

startMessage = """
  _____  _                                     _           _     _       
 |  __ \| |                                   | |         | |   (_)      
 | |__) | |__   __ _ ___ _ __ ___   ___  _ __ | |__   ___ | |__  _  __ _ 
 |  ___/| '_ \ / _` / __| '_ ` _ \ / _ \| '_ \| '_ \ / _ \| '_ \| |/ _` |
 | |    | | | | (_| \__ \ | | | | | (_) | |_) | | | | (_) | |_) | | (_| |
 |_|    |_| |_|\__,_|___/_| |_| |_|\___/| .__/|_| |_|\___/|_.__/|_|\__,_|
                                        | |                              
  _____                 _               |_|                              
 |  __ \               | |               (_)                             
 | |__) |__ _ _ __   __| | ___  _ __ ___  _ _______ _ __                 
 |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \| |_  / _ \ '__|                
 | | \ \ (_| | | | | (_| | (_) | | | | | | |/ /  __/ |                   
 |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|_/___\___|_|                                                                                                                                                                                                                                                                                      
"""

print(Fore.RED + startMessage);

allItems = ["EMF Reader", "Ghost Writing Book", "Spirit Box", "Thermometer", "Video Camera", "UV Flashlight", "Crucifix", "Glow Stick", "Head Mounted Camera (Multiplayer Only)", "Infrared Light Sensor", "Lighter", "Motion Sensor", "Parabolic Microphone", "Salt", "Sanity Pills", "Smudge Sticks", "Sound Sensor", "Tripod"]
#print(allItems);
#print(len(allItems))
random.shuffle(allItems)

textColors = list(vars(colorama.Fore).values())

rollNumber = 1;
for i in allItems:
    randomColor = random.choice(textColors);
    print(Fore.GREEN + "Press enter to roll an item")
    enterPlaceHolder = input()
    print(Fore.YELLOW + "Roll #", Fore.WHITE + str(rollNumber), Fore.CYAN + ", Item: ", randomColor + ">> ", Style.RESET_ALL + i, randomColor + " <<", Style.RESET_ALL)
    rollNumber += 1

print(Fore.RED + "That's all the items! Restart the program to roll again.")
