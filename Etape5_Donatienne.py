"""
Étape 5 - Validation des données avec assert
"""

def verifier_nom(nom):
    """Vérifie que le nom est en majuscules"""
    assert nom.isupper(), "Le nom doit être en MAJUSCULES"
    return nom


def verifier_telephone(tel):
    """Vérifie que le numéro contient exactement 10 chiffres"""
    assert tel.isdigit(), "Le téléphone doit contenir uniquement des chiffres"
    assert len(tel) == 10, "Le téléphone doit contenir 10 chiffres"
    return tel


def verifier_email(email):
    """Vérifie que l'email contient @ et ."""
    assert "@" in email, "L'email doit contenir un @"
    assert "." in email, "L'email doit contenir un point"
    return email


def verifier_favori(favori):
    """Vérifie que favori est un booléen"""
    assert type(favori) == bool, "Favori doit être True ou False"
    return favori


def creer_contact(nom, prenom, tel, email, favori):
    """Crée un contact après validation des données"""

    nom = nom.upper()

    verifier_nom(nom)
    verifier_telephone(tel)
    verifier_email(email)
    verifier_favori(favori)

    contact = {
        "nom": nom,
        "prenom": prenom,
        "tel": tel,
        "email": email,
        "favori": favori
    }

    return contact