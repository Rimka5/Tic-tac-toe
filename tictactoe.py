grille = ["-","-","-",
        "-","-","-",
        "-","-","-"]

joueur_en_cours = "X"
jeu_en_cours = True
gagnant = None

# ----afficher_grille est une fonction qui permet d'afficher les element de la grille---
def afficher_grille ():
    
    """_afficher_grille est une fonction qui permet d'afficher les element de la grille_

    Args:
        grille (_type_): _description_
    """
    print(grille[0] + "|" + grille[1] + "|" + grille[2])
    print("-----")
    print(grille[3] + "|" + grille[4] + "|" + grille[5])
    print("-----")
    print(grille[6] + "|" + grille[7] + "|" + grille[8])


# -----------verifier si la case est vide --------

def entree_joueur():
    ent = int(input("entrez un nombre : "))
    if ent >= 1 and ent <= 9 and grille[ent-1] == "-":
        grille[ent-1] = joueur_en_cours
    else:
        print ("la case n'est pas vide!")
        
    
    # -------verifier s'il y a victoire--------
    
def verifier_horizontal(grille):
        global gagnant
        if grille[0] == grille[1] == grille[3] and grille[0]!="-" :
            gagnant = grille[0]
            return True
        elif grille[3] == grille[4] == grille[5] and grille[3]!="-" :
            gagnant = grille[3]
            return True
        elif grille[6] == grille[7] == grille[8] and grille[6]!="-" :
            gagnant = grille[6]
            return True
def verifier_vertical(grille):
        global gagnant
        if grille[0] == grille[3] == grille[6] and grille[0]!="-" :
            gagnant = grille[0]
            return True
        elif grille[1] == grille[4] == grille[7] and grille[1]!="-" :
            gagnant = grille[1]
            return True
        elif grille[2] == grille[5] == grille[8] and grille[6]!="-" :
            gagnant = grille[2]
            return True
def verifier_diagonal(grille):
        global gagnant
        if grille[0] == grille[4] == grille[8] and grille[0]!="-" :
            gagnant = grille[0]
            return True
        elif grille[2] == grille[4] == grille[6] and grille[2]!="-" :
            gagnant = grille[2]
            return True
    
def verfifier_victoire():
        if verifier_diagonal(grille) or verifier_horizontal(grille) or verifier_vertical(grille):
            print(f"le gagnant est {gagnant}")
        
        
    # ---------------Verifier s'il y a égalité-------------
    
def verifier_egalite(grille):
        global jeu_en_cours
        if "-" not in grille:
            afficher_grille(grille)
            print(" y'a egalité !")
            jeu_en_cours = False
            
            
    
    # -------------Changer de joueur--------------
    
def changer_joueur():
        global joueur_en_cours
        if joueur_en_cours == "X":
            joueur_en_cours = "O"
        else:
            joueur_en_cours = "X"
            
            
            
while jeu_en_cours:
    afficher_grille()
    if gagnant != None:
        break
    entree_joueur()
    verfifier_victoire()
    verifier_egalite(grille)
    changer_joueur()
