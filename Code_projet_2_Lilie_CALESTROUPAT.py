# Projet 2
# Lilie CALESTROUPAT--LANG

        # TRIER LA LISTE
F = open('contacts.txt', 'r', encoding = 'utf-8')    # ouvrir en mode lecture
print(sorted(F))                                     # trier la liste
F.close()                                            # fermer le fichier

# Instructions pouvant aider pour les autres questions :

# chaine.upper() renvoie une copie de la chaîne chaine avec tous les caracteres en majuscules.

# if favori == True :
#     F = open('favoris.txt', 'w', encoding = 'utf-8')
#     F.write(f{nom}; {prenom}; {tel}; {email}; {favori})
# else :
#     F = open('contacts.txt', 'w', encoding = 'utf-8')
#     F.write(f{nom}; {prenom}; {tel}; {email}; {favori})