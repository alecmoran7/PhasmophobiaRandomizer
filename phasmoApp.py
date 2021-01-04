from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import appTemplate
import random



class RandomizerApp(QtWidgets.QMainWindow, appTemplate.Ui_MainWindow):
    allLocations = ["Tanglewood Street House", "Edgefield Street House", "Ridgeview Road House", "Grafton Farmhouse", "Bleasdale Farmhouse", "Brownstone High School", "Asylum", "Prison"]
    allItems = ["EMF Reader", "Ghost Writing Book", "Spirit Box", "Thermometer", "Video Camera", "UV Flashlight", "Crucifix", "Glow Stick", "Infrared Light Sensor", "Lighter", "Motion Sensor", "Parabolic Microphone", "Salt", "Sanity Pills", "Smudge Sticks", "Sound Sensor"]
    allLightSources = ["Strong Flashlight", "Flashlight", "Candle"]
    allItemsCopy = allItems.copy()
    random.shuffle(allItems)
    numberOfRolls = 0
    rollsLeft = 16

    def __init__(self, parent=None):
        super(RandomizerApp, self).__init__(parent)
        self.setupUi(self)
        self.rollButton.clicked.connect(self.rollHandler)                       # Button - Roll Item
        self.checkPhotoCam.stateChanged.connect(self.photocamHandler)           # Checkbox - Add Photo Cameras
        self.checkLightSource.stateChanged.connect(self.lightsourceHandler)     # Checkbox - Add Light Sources
        self.checkHeadCam.stateChanged.connect(self.headcamHandler)             # Checkbox - Add Head Cameras
        self.checkTripods.stateChanged.connect(self.tripodHandler)              # Checkbox - Add Tripods
        self.locationButton.clicked.connect(self.locationHandler)               # Button - Roll Location
        self.lightsourceButton.clicked.connect(self.lightsourceRollerHandler)   # Button - Roll Light Source
        self.resetButton.clicked.connect(self.resetHandler)                     # Button - Reset
        self.exitButton.clicked.connect(self.exitHandler)                       # Button - Exit
        
        #Quickrollers
        self.quickRoll3.clicked.connect(self.quickrollHandler3)               # Button - QuickRoll with 3 items
        self.quickRoll4.clicked.connect(self.quickrollHandler4)               # Button - QuickRoll with 4 items
        self.quickRoll5.clicked.connect(self.quickrollHandler5)               # Button - QuickRoll with 5 items
        self.quickRoll6.clicked.connect(self.quickrollHandler6)               # Button - QuickRoll with 6 items
        self.quickRoll7.clicked.connect(self.quickrollHandler7)               # Button - QuickRoll with 7 items

    def rollHandler(self):
        if self.rollsLeft > 0:
            self.lastItemRolled.setText(self.allItems[0])
            self.listOfItems.addItem(self.allItems[0])
            self.allItems.pop(0)
            self.numberOfRolls += 1
            self.numRolls.display(self.numberOfRolls)
            self.rollsLeft -= 1

    ## Photocam Handler
    def photocamHandler(self):
        if self.checkPhotoCam.isChecked() == 1:
            self.allItems.append("Photo Camera")
            random.shuffle(self.allItems)
            self.rollsLeft += 1
            print("Added Photo Camera")
        else:
            if "Photo Camera" in self.allItems:
                self.allItems.remove("Photo Camera")
                print("Removed Photo Camera")
                self.rollsLeft -= 1

    ## LightSource Handler
    def lightsourceHandler(self):
        if self.checkLightSource.isChecked() == 1:
            self.allItems.append("Candle")
            self.allItems.append("Flashlight")
            self.allItems.append("Strong Flashlight")
            random.shuffle(self.allItems)
            self.rollsLeft += 3
            print("Added Candle, Flashlight, and Strong Flashlight")
        else:
            if "Candle" in self.allItems:
                self.allItems.remove("Candle")
                self.allItems.remove("Flashlight")
                self.allItems.remove("Strong Flashlight")
                print("Removed Candle, Flashlight, and Strong Flashlight")
                self.rollsLeft -= 3

    ## HeadCam Handler
    def headcamHandler(self):
        if self.checkHeadCam.isChecked() == 1:
            self.allItems.append("Head-Mounted Camera")
            random.shuffle(self.allItems)
            self.rollsLeft += 1
            print("Added Head-Mounted Camera")
        else:
            if "Photo Camera" in self.allItems:
                self.allItems.remove("Head-Mounted Camera")
                print("Removed Head-Mounted Camera")
                self.rollsLeft -= 1                

    ## Tripod Handler
    def tripodHandler(self):
        if self.checkTripods.isChecked() == 1:
            self.allItems.append("Tripod")
            random.shuffle(self.allItems)
            self.rollsLeft += 1
            print("Added Tripod")
        else:
            if "Tripod" in self.allItems:
                self.allItems.remove("Tripod")
                print("Removed Tripod")
                self.rollsLeft -= 1

    ## Location Button Handler
    def locationHandler(self):
        randomLocation = self.allLocations[random.randint(0,7)]
        self.locationRolled.setText(randomLocation)

    ## Light Source Roller Button Handler
    def lightsourceRollerHandler(self):
        randomLightSource = self.allLightSources[random.randint(0,2)]
        self.lightSourceRolled.setText(randomLightSource)

    ## Reset Button Handler        
    def resetHandler(self):
        self.allItems = self.allItemsCopy.copy()
        random.shuffle(self.allItems)
        self.rollsLeft = 16
        self.numberOfRolls = 0

        ## Reset Displays
        self.listOfItems.clear()
        self.lastItemRolled.setText("")
        self.locationRolled.setText("")
        self.numRolls.display(self.numberOfRolls)
        self.lightSourceRolled.setText("")
        
        ## Reset Check Boxes
        self.checkPhotoCam.setChecked(False)
        self.checkLightSource.setChecked(False)
        self.checkHeadCam.setChecked(False)
        self.checkTripods.setChecked(False)

    def quickRoll(self, numItems):
        self.resetHandler()
        while numItems > 0:
            self.rollHandler()
            numItems -= 1
        self.locationHandler()
        self.lightsourceRollerHandler()

    ## Quick Roll Handler 3
    def quickrollHandler3(self):
        self.quickRoll(3)
    
    ## Quick Roll Handler 4
    def quickrollHandler4(self):
        self.quickRoll(4)    

    ## Quick Roll Handler 5
    def quickrollHandler5(self):
        self.quickRoll(5)

    ## Quick Roll Handler 6
    def quickrollHandler6(self):
        self.quickRoll(6)

    ## Quick Roll Handler 7
    def quickrollHandler7(self):
        self.quickRoll(7)

    ## Exit Button Handler        
    def exitHandler(self):
            sys.exit()

def main():
    app = QApplication(sys.argv)
    form = RandomizerApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
