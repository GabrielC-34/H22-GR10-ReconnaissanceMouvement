import Webcam as wc
import HandTracker as ht
import LightController as lc
import cv2
import time
from Main_GUI import *
from Settings_GUI import *
from PyQt5 import QtWidgets
import sys

lightController = lc.LightController()


def activerMain():
    global nomGeste
    nomGeste = "None"
    vieuxGeste = "NoneTest"
    webcam = wc.Webcam()
    handProcessor = ht.HandTrackProcessor()
    webcam.openWebcam()
    listeMarqueurs = []
    global timeStart
    timeStart = time.time()
    global timeFinish
    timeFinish = time.time()
    calculerGeste = False
    global derniereDistance
    derniereDistance = 10000

    #Méthode qui calcule la distance entre le pouce et l'index dans l'image et la retourne
    def calculerDistancePouceIndex(positionIndex, positionPouce, listeMarqueurs):
        distancePouceIndex = 100
        if (len(listeMarqueurs) != 0) and (listeMarqueurs[0] != None):
            posIndexX, posIndexY = positionIndex[0], positionIndex[1]
            posPouceX, posPouceY = positionPouce[0], positionPouce[1]
            distancePouceIndex = ((posPouceX - posIndexX) ** 2) + ((posPouceY - posIndexY) ** 2)
        return distancePouceIndex

    def variationDistance(derniereDistance, distance):
        distanceAugmente = None
        deltaDistance = distance-derniereDistance
        if  deltaDistance >= 25:
            distanceAugmente = True
        elif deltaDistance <= -25:
            distanceAugmente = False
        return distanceAugmente
    ####################################################################################################################
    #Méthode qui envoie chaque image capturée par OpenCV se faire calculer par HandController.py
    def calculsEtAnalyse(img, listeMarqueurs):
        global timeStart
        global timeFinish
        global nomGeste
        global derniereDistance
        distanceAugmente = None
        listeMarqueurs.clear()
        #On envoie l'image se faire analyser pour détecter les points de la main
        processedImage, listeMarqueurs = handProcessor.analyserImage(img)
        #On envoie UNIQUEMENT 1 image/seconde se faire analyser par l'algorithme TensorFlow de reconnaissance de mouvement
        #afin d'optimiser les performances du programme
        positionIndex = listeMarqueurs[8]
        positionPouce = listeMarqueurs[4]
        if calculerGeste:
            if timeFinish - timeStart >= 1:
                if(listeMarqueurs[0] != None):
                    nomGeste = handProcessor.predictionGeste(listeMarqueurs)
                    derniereDistance = calculerDistancePouceIndex(positionIndex, positionPouce, listeMarqueurs)
                timeStart = timeFinish
        timeFinish = time.time()
        if not calculerGeste:
            distance = calculerDistancePouceIndex(positionIndex, positionPouce, listeMarqueurs)
            distanceAugmente = variationDistance(derniereDistance, distance)
            derniereDistance = distance

        processedImage = cv2.flip(processedImage, 1)
        return processedImage
    ####################################################################################################################
    #Contrôle la lumière si le geste défini est détecté
    def controleDeLumière(lightController):
        global nomGeste
        if nomGeste == "fist":
            lightController.allumerAmpoule()
        elif nomGeste == "stop":
            lightController.eteindreAmpoule()
        elif nomGeste == "call me":
            lightController.easterEgg()
    #######################################################################################################################

    #Boucle de lecture infinie de la caméra
    while webcam.webcamIsOpen == True:
        frame = webcam.readWebcam()
        frame = calculsEtAnalyse(frame, listeMarqueurs)
        #Si le geste a changé depuis le précédent, on l'envoie au LightController
        if nomGeste != vieuxGeste and nomGeste != None:
            controleDeLumière(lightController)
            vieuxGeste = nomGeste
        cv2.imshow("Webcam", frame)
    webcam.closeWebcam()

#Code qui indique ce que font les boutons dans le menu principal du programme
class MainMenu(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.boutonDemarrer.clicked.connect(self.demarrer)
        self.boutonArret.clicked.connect(self.arreter)
        self.boutonParametre.clicked.connect(self.settingsMenu)
    #Bouton qui exécute tout le programme
    def demarrer(self):
        activerMain()
    #Bouton qui quitte le programme
    def arreter(self):
        lightController.eteindreAmpoule()
        sys.exit()
    #Bouton pour aller dans les settings
    def settingsMenu(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

#Code qui indique ce que font les boutons dans le menu des paramètres
class SettingsMenu(Ui_ParametersWindpw):
    def __init__(self, window):
        self.setupUi(window)
        self.BoutonApiKey.clicked.connect(self.apiSubmit)
        self.BoutonBulbLabel.clicked.connect(self.labelSubmit)
        self.BoutonRetourMenu.clicked.connect(self.retourMenu)
    #Bouton pour submit la nouvelle API KEY
    def apiSubmit(self):
        apiKey = self.ApiKeyTextBox.text()
        lightController.changerApiKey(apiKey)
    #Bouton pour submit le nouveau Bulb Label
    def labelSubmit(self):
        bulbLabel = self.BulbLabelTextBox.text()
        lightController.changerBulbLabel(bulbLabel)
    #Bouton pour retourner au menu principal
    def retourMenu(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


#Code pour afficher le GUI
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
MainWindow = QtWidgets.QMainWindow()
SettingsWindow = QtWidgets.QMainWindow()
ui = MainMenu(MainWindow)
ui2 = SettingsMenu(SettingsWindow)
widget.addWidget(MainWindow)
widget.addWidget(SettingsWindow)
widget.setFixedWidth(960)
widget.setFixedHeight(540)
widget.show()
app.exec_()