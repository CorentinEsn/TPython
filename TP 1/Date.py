class Date:
    def __init__(self, jour, mois, annee):  # Constructeur
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __init__(self, date):   # Constructeur depuis une chaîne de caractères de type "jj/mm/aaaa"
        split = date.split("/")
        self.jour = split[0]
        self.mois = split[1]
        self.annee = split[2]

    def __eq__(self, other):    # Surcharge de l'opérateur ==
        return self.jour == other.jour and self.mois == other.mois and self.annee == other.annee

    def __It__(self, other):    # Surcharge de l'opérateur <
        if self.annee < other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois < other.mois:
                return True
            elif self.mois == other.mois:
                if self.jour < other.jour:
                    return True
        return False

    def __str__(self):  # Surcharge de l'opérateur print()
        return "{}/{}/{}".format(self.jour, self.mois, self.annee)