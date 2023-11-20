class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __init__(self, date):
        date.split("/")
        self.jour = date[0]
        self.mois = date[1]
        self.annee = date[2]

    def __eq__(self, other):
        return self.jour == other.jour and self.mois == other.mois and self.annee == other.annee

    def __It__(self, other):
        if self.annee < other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois < other.mois:
                return True
            elif self.mois == other.mois:
                if self.jour < other.jour:
                    return True
        return False

    def Afficher(self):
        print("Date : {}/{}/{}".format(self.jour, self.mois, self.annee))
