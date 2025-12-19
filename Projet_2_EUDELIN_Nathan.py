FICHIER_CONTACTS="contacts.txt"
def charger_contact():
    contacts=[]
    try:
        with open(FICHIER_CONTACTS, "r", encoding='utf-8')as fichier:
            contact = {
                "nom":nom,
                "prenom":prenom,
                "tel":tel,
                "email":email,
            }
            contacts.append(contact)
    except FileNotFoundError:
        print()

def telephone_valide(tel):
    return len(tel)==10


def ajouter_contact(contacts):
    nom=input("Nom :").upper
    prenom=input("Prénom :")
    tel=input("Numéro de téléphone :")
    while not telephone_valide(tel):
        tel=input("Le numéro est invalide, réessayer :")









