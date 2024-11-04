#(1)fonction qui permet de remplir le tableau
def remplirTableau():
    tableau_notes = []

    for i in range(10):
        note = int(input(f"Entrez la note du stagiaire {i + 1} : "))
        tableau_notes.append(note)

    return tableau_notes
#jeu de test (test unitaire)
notesStagiaires = remplirTableau()
print("Les notes des stagiaires sont :", notesStagiaires)

#2 Fonction pour trouver le maximum et le minimum
def maxMinNotes(notes):
    maxNote = max(notes)
    minNote = min(notes)
    return (maxNote, minNote)

#jeu de test (test unitaire)
if __name__ == "__main__":
    notes = remplirTableau()
    resultat = maxMinNotes(notes)
    print(f"Le maximum est {resultat[0]} et le minimum est {resultat[1]}.")

