"""
Projet 2 NSI – Carnet de contacts
Gestion d'un répertoire avec fichier texte
"""

# ===============================
# Chargement et sauvegarde
# ===============================

def charger_contacts(nom_fichier):
    """
    Charge les contacts depuis un fichier texte.
    Retourne une liste de dictionnaires triée par nom.
    """
    repertoire = []

    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                infos = ligne.split(";")

                contact = {
                    "nom": infos[0],
                    "prenom": infos[1],
                    "tel": infos[2],
                    "email": infos[3],
                    "favori": infos[4] == "True"
                }

                repertoire.append(contact)

        repertoire.sort(key=lambda c: c["nom"])

    except FileNotFoundError:
        repertoire = []

    return repertoire


def sauvegarder_contacts(repertoire, nom_fichier):
    """
    Sauvegarde tous les contacts dans contacts.txt
    et les favoris dans favoris.txt
    """
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        for c in repertoire:
            ligne = f"{c['nom']};{c['prenom']};{c['tel']};{c['email']};{c['favori']}\n"
            fichier.write(ligne)

    with open("favoris.txt", "w", encoding="utf-8") as fichier:
        for c in repertoire:
            if c["favori"]:
                ligne = f"{c['nom']};{c['prenom']};{c['tel']};{c['email']};{c['favori']}\n"
                fichier.write(ligne)


# ===============================
# Vérifications
# ===============================

def telephone_valide(tel):
    """Vérifie que le numéro contient exactement 10 chiffres"""
    return tel.isdigit() and len(tel) == 10


def email_valide(email):
    """Vérifie la présence de @ et ."""
    return "@" in email and "." in email


# ===============================
# Fonctions du menu
# ===============================

def ajouter_contact(repertoire):
    nom = input("Nom : ").upper()
    prenom = input("Prénom : ")

    tel = input("Téléphone : ")
    while not telephone_valide(tel):
        tel = input("Téléphone invalide. Recommence : ")

    email = input("Email : ")
    while not email_valide(email):
        email = input("Email invalide. Recommence : ")

    fav = input("Favori (o/n) : ").lower()

    contact = {
        "nom": nom,
        "prenom": prenom,
        "tel": tel,
        "email": email,
        "favori": fav == "o"
    }

    repertoire.append(contact)
    repertoire.sort(key=lambda c: c["nom"])
    print("Contact ajouté.")


def afficher_repertoire(repertoire):
    for c in repertoire:
        print(f"{c['nom']:10} {c['prenom']:10} {c['tel']} {c['email']}")


def rechercher_contact(repertoire):
    debut = input("Début du nom : ").upper()
    for c in repertoire:
        if c["nom"].startswith(debut):
            print(c["nom"], c["prenom"], "-", c["tel"])


def afficher_favoris(repertoire):
    for c in repertoire:
        if c["favori"]:
            print(c["nom"], c["prenom"], "-", c["tel"])


def supprimer_contact(repertoire):
    nom = input("Nom à supprimer : ").upper()
    for c in repertoire:
        if c["nom"] == nom:
            repertoire.remove(c)
            print("Contact supprimé.")
            return
    print("Contact non trouvé.")


# ===============================
# Programme principal
# ===============================

repertoire = charger_contacts("contacts.txt")

choix = ""

while choix != "6":
    print("\n--- MENU ---")
    print("1. Ajouter un contact")
    print("2. Afficher le répertoire")
    print("3. Rechercher un contact")
    print("4. Afficher les favoris")
    print("5. Supprimer un contact")
    print("6. Quitter et sauvegarder")

    choix = input("Choix : ")

    if choix == "1":
        ajouter_contact(repertoire)
    elif choix == "2":
        afficher_repertoire(repertoire)
    elif choix == "3":
        rechercher_contact(repertoire)
    elif choix == "4":
        afficher_favoris(repertoire)
    elif choix == "5":
        supprimer_contact(repertoire)
    elif choix == "6":
        sauvegarder_contacts(repertoire, "contacts.txt")
        print("Données sauvegardées. Au revoir.")
    else:
        print("Choix invalide.")
