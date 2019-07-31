import os
import sys
import mainwindow as CatUI
from PyQt5 import QtWidgets, QtGui, QtCore

class CatGenerator (QtWidgets.QMainWindow, CatUI.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        CatUI.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.intonly = QtGui.QIntValidator()
        self.AdoptionFees.setValidator(self.intonly)

        self.ExportBtn.clicked.connect(self.exportToTxt)

    def exportToTxt(self):
        exportPath1 = QtWidgets.QFileDialog.getExistingDirectory(parent=self,
                    caption="Locate Export Folder")
        self.catNameExport = self.CatNames.toPlainText()
        self.adoptionExport = self.AdoptionFees.text()
        self.contactExport = self.ContactPhone.toPlainText()
        self.engExport = self.EngDesc.toPlainText()
        self.frExport = self.FrenchDesc.toPlainText()
        print(self.catNameExport, self.adoptionExport, self.contactExport, self.engExport, self.frExport)

        if self.catNameExport == "" or self.adoptionExport == "" or self.contactExport == "" or self.engExport == "" or self.frExport == "":
            self.emptyDial = QtWidgets.QMessageBox.warning(self,"Error","All fields must be filled with at least one character. Export aborted.")
            pass
        else:
            txtfile = open(exportPath1 + "/" + self.catNameExport + ".txt", "w")
            txtfile.write("English will follow!" + "\n\n" + self.frExport + "\n" + "Pour en savoir plus sur l'adoption de " + self.catNameExport + ", envoyez-nous un message sur notre page Facebook! https://www.facebook.com/heartinhandrescue/" + "\n" + "Vous pouvez également appeler/texter " + self.contactExport + "\n" + "Les frais d'adoption responsables sont de " + self.adoptionExport + "$." + "\n" +  "L'adoption responsable signifie que cette adoption est accompagnée de tous les soins vétérinaires, y compris:" + "\n" + "- tous les vaccins de base" + "\n" + "- stérilisation" + "\n" + "- micropuce" + "\n" + "- 2 traitements de déparasitage" + "\n" + "- 2 traitements revo" + "\n" + "Représentant plus de 600,00 $ de coûts vétérinaires par chat." + "\n" + "Vous aiderez une organisation locale à but non lucratif et contribuerez à mettre un terme au cycle de reproduction des chats sauvages grâce à cette adoption." + "\n" + "Si vous souhaitez visiter et éventuellement adopter " + self.catNameExport + ", veuillez téléphoner au " + self.contactExport + " ou par SMS. Vous pouvez également nous envoyer un message via notre page Facebook: https://www.facebook.com/heartinhandrescue/"
                + "\n\n" + "A PROPOS DE NOUS" + "\n" + "Notre organisme, Heart in Hand Rescue Coeur en Main, est un organisme de sauvetage à but non lucratif basé à Montréal, Québec. Comme nous n’avons pas de locaux physiques, nous nous efforçons de prendre soin de nos chats et chatons grâce à des familles d’accueil." + "\n" + "Nos chatons et nos chats sont pris en charge dans des familles d’accueil qui les aiment et les gâtent. Ils sont très socialisés et jamais élevés dans des cages. Ils sont intégrés dans l’environnement familial pouvant inclure d’autres chats et chiens." + "\n" + "Nous faisons le maximum pour les chatons et nous incluons tout ce qui permettra à nos amis à fourrure d’avoir le meilleur début possible dans la vie ainsi qu’avec leur nouvelle famille. Pour plus d’informations, communiquez avec nous sur notre page Facebook! https://www.facebook.com/heartinhandrescue/" + "\n\n" + self.engExport + "\n\n" + "To inquire about adopting " + self.catNameExport + ", message us on our Facebook page! https://www.facebook.com/heartinhandrescue/" + "\n" + "You can also call/text " + self.contactExport + "\n" + "Responsible adoptions fees : " + self.adoptionExport + "$" + "\n" + "Responsible adoption means that this adoption comes with all vet care including: " + "\n" + "- all basic vaccines" + "\n" + "- sterilization" + "\n" + "- Microchip" + "\n" + "- 2 deworming treatments" + "\n" + "- 2 revo treatments" + "\n" + "Representing well over $600.00 worth of veterinary costs each. You'll be helping a local non-profit organization and helping stop the cycle of reproducing feral cats with this adoption." + "\n" + "If you wish to visit and potentially adopt" + self.catNameExport + ', please call or text ' + self.contactExport + "." + "\n" + "You can also message us though our Facebook page: https://www.facebook.com/heartinhandrescue/" + "\n\n" + "ABOUT US:" + "\n" + "Heart in Hand Rescue Coeur en Main is a non-profit organization based in Montreal, Quebec. As we have no physical shelter, we rely on volunteer fosters to take care of cats and kittens." + "\n" + "We’ve been saving cats and kittens since 2014. All cats/kittens are under the care of Heart in Hand Rescue Coeur en Main. Adopters must come through us for adoption of any cat(s) or kitten(s). We promote responsible adoption that comes with all the vet care included. We do NOT give kittens away." + "\n" + "All our cats and kittens come with sterilization agreements since we support the cause of reducing the overpopulation of felines in our area. Thousands of cats and kittens are neglected, live in hardship and are euthanized each year because of humans who do not do right by them by providing appropriate vet care and sterilization." + "\n" + "We aim to reduce this kind of unnecessary animal suffering and give all cats that we save a second chance at a better life. \nThanks for checking out this kitten, please check our page for more! https://heartinhandrescue.wordpress.com/")
            txtfile.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = CatGenerator()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
