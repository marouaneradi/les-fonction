#(1)fonction qui permet de remplir le tableau
def remplirTableau():
    tableau_notes = []

    for i in range(10):
        note = int(input(f"Entrez la note du stagiaire {i + 1} : "))
        tableau_notes.append(note)

    return tableau_notes

notesStagiaires = remplirTableau()
print("Les notes des stagiaires sont :", notesStagiaires)
