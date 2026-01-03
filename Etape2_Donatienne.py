"""
Projet NSI – Étape 2
Modélisation d'un carnet de contacts
"""

# Création du répertoire (liste de contacts)
repertoire = []

# Création du premier contact
contact1 = {
    "nom": "DUPONT",
    "prenom": "Jean",
    "tel": "0601020304",
    "email": "jean.dupont@mail.com",
    "favori": True
}

# Création du deuxième contact
contact2 = {
    "nom": "ALVES",
    "prenom": "Maria",
    "tel": "0708091011",
    "email": "maria.alves@mail.com",
    "favori": False
}

# Création du troisième contact
contact3 = {
    "nom": "Zola",
    "prenom": "Emile",
    "tel": "0102030405",
    "email": "e.zola@ecrivain.com",
    "favori": False
}


# Création du quatrième contact
contact4 = {
    "nom": "BERNARD",
    "prenom": "Lucas",
    "tel": "0622334455",
    "email": "l.bernard@travail.org",
    "favori": True
}


# Ajout des contacts au répertoire
repertoire.append(contact1)
repertoire.append(contact2)
repertoire.append(contact3)
repertoire.append(contact4)


# Affichage du répertoire
print("Liste des contacts :")
for contact in repertoire:
    print(
        contact["nom"],
        contact["prenom"],
        contact["tel"],
        contact["email"],
        contact["favori"]
    )

