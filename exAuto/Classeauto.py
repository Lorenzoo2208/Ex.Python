# class Persona:
#     def saluta(self):
#         print("Ciao!")

# class Studente(Persona):
#     def saluta(self):
#         print("Ciao, sono uno studente!")

# persona1 = Persona()
# studente1 = Studente()
# persona1.saluta() #Output: Ciao!
# studente1.saluta() #Output: Ciao, sono uno studente



# class Persona:
#    specie = "Homo Sapiens" #attributo di classe




#    def __init__(self, nome, eta):
#        self.nome = nome    #attributo di istanza


#        self.eta = eta


# persona1 = Persona ("Mario", 20)
# print(persona1.specie) #Output: Homo sapiens
# print(persona1.nome)    #Output :mario

from exAuto.Classeauto import DescrizioneVeicolo, AumentaVelocita , DiminuisciVelocita, UscitadalProgramma

while True:

    print("1-Descrizione del veicolo")
    print("2-Aumenta la velocità")
    print("3-Diminuisci la velocità")
    print("4-Uscita dal programma")

    scelta = input("Seleziona cosa vuoi fare")

    if scelta == 1:

        dettagli= input("Questi sono i dettagli della macchina:")
        DescrizioneVeicolo (dettagli)

    elif scelta == 2:

         aumento = input("La velocita è aumentata di:")
         AumentaVelocita (aumento)

    elif scelta == ("3"):

        diminuzione = input("inserisci il titolo del libro da riportare:")
        DiminuisciVelocita (diminuzione)

    elif scelta == ("4"):

         uscita= input("vuoi uscire?")
         UscitadalProgramma (uscita)

