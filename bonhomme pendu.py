# MARK GOBRIEL
# JEUX DE BONHOMME PENDU!
# ICS4U

# LE CODE SUIVANT IMPORTE SIMPLEMENT LA LISTE DES MOTS ALÉATOIRES DE L'AUTRE FICHIER

import random
from mots import word_list

# CE CODE CHOISIT L'UNE DES MOTS DANS CETTE LISTE

def get_word():
    word = random.choice(word_list)
    return word.upper()

# CE CODE DESSINE LES CASES VIDES CONTENANT LE NOMBRE DE LETTRES DANS LE MOT MYSTÈRE

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Jouons au BONHOMME PENDU!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

# CE CODE FAIT CE QUI SUIT:
    # DIT À L'UTILISATEUR DE DEVINER UN MOT OU UNE LETTRE
    # PERMET À L'UTILISATEUR DE SAVOIR S'IL A DÉJÀ DEVINÉ CETTE LETTRE
    # INDIQUE À L'UTILISATEUR SI LA LETTRE N'EST PAS DANS LE MOT
    # INDIQUE À L'UTILISATEUR SI LA LETTRE EST DANS LE MOT
    # INDIQUE À L'UTILISATEUR S'IL A DÉJÀ DEVINÉ CE MOT
    # INDIQUE À L'UTILISATEUR SI LE MOT N'EST PAS CORRECTE
    # INDIQUE À L'UTILISATEUR QU'UNE HYPOTHÈSE N'EST PAS VALIDE SI CE N'EST PAS UNE LETTRE OU UN MOT (EXEMPLE : CHIFFRES OU SYMBOLES)
    # FÉLICITE L'UTILISATEUR S'IL A DEVINÉ LE BON MOT
    # DIT À L'UTILISATEUR LA RÉPONSE CORRECTE APRÈS AVOIR UTILISÉ TOUTES LEURS DEVINES

    while not guessed and tries > 0:
        guess = input("Veuillez deviner une lettre ou un mot:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Vous avez déjà deviné cette lettre", guess)
            elif guess not in word:
                print(guess, "n'est pas dans le mot.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bon travail,", guess, "est dans le mot !")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Vous avez déjà deviné ce mot", guess)
            elif guess != word:
                print(guess, "n'est pas le mot.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Cette supposition n'est pas valide.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Félicitations, vous avez deviné le mot ! Vous gagnez!")
    else:
        print("Désolé, vous n'avez plus d'essais. Le mot était " + word + ". Peut-être la prochaine fois!")

# CE CODE REPRÉSENTE L'ÉTAT DU PENDU SELON LE STADE OÙ ATTEINT L'UTILISATEUR

def display_hangman(tries):
    stages = [  # ETAT FINAL: tete, torso, les 2 bras et les 2 pieds
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # tete, torso, les 2 bras et une pied
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # tete, torso et les 2 bras
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # tete, torso et une seul bra
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # tete et torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # tete uniquement
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # ETAT INITIAL
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# CE CODE DEMANDE À L'UTILISATEUR S'IL VEUT JOUER ENCORE OU NON

def main():
    word = get_word()
    play(word)
    while input("Rejouer? (OUI/NON) ").upper() == "OUI":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()