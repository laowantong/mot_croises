from random import randint
from unicodedata import normalize

# First group of crosswords before the first test end at the 75th element
CROSSWORDS_FIRST_GROUP = 77


crosswords_list = ["4/2 est de type ____",
    "(Le|la|l') ____ d'une fonction est le bloc de lignes indentées par rapport au mot-clef ____",
    "On communique avec une fonction en lui passant des ____",
    "(Le|la|l') ____8 est un guide de style pour le code python",
    "L'en-tête d'une fonction se termine par le symbole ____",
    "____ une ligne, c'est la faire débuter par des blancs/espaces",
    "Un bon programme n'est pas astucieux mais ____",
    "lifes is better without ____",
    "____ est un système des composition de documents particulièrement adapté à la production de textes scientifiques.",
    "Une fonction communique son résultat par une instruction ____",
    "En Python ou en C, % est l'opérateur ____",
    "On peut ____ des fonctions définies dans un fichier personnel ou dans (un|une) ____ ( ____ en anglais).",
    "input est un rare exemple de fonction à effet de bord. Elle renvoie (un|une) X",
    "Une ____ (en anglais, ____) est une séquence de caractère",
    "____ est une ____ d'affichage, par défaut sur la sortie ____.",
    "Le langage ____ a été crée dans les années 90, par ____ van Rossum aux Pays Bas",
    "les identificateurs énumérés entre parenthèses dans l'en-tête d'une définition sont aussi dit ____ ____",
    "Le troisième argument de pow() est ____",
    "On ____ une fonction en écrivant une docstring après son en-tête.",
    "Le ____ d'une donnée définit les  qu'elle peut prendre, ainsi que les ____ qui peuvent lui être appliquées",
    "Une ____ ne produit pas de valeur mais un effet de bord.",
    "En anglais, affectation se dit ____",
    "Le ____ d'instruction permet à l'ordinateur de savoir quelle est la prochaine instruction à exécuter",
    "Dans la plupart des langages statiques, on peut ____ une variable sans ____ sa valeur",
    "L'échange se fait classiquement à l'aide d'une variable ____",
    "La fonction ____ renvoie l'adresse-mémoire d'une valeur",
    "Si un nom de variable comprend plusieurs mots, ceux-ci sont séparés par des ____",
    "L'expression 42 est un ____, mais 1 + 2 ne l'est pas",
    "Le nom du type de destination peut être utilisé comme une fonction de ____",
    "La ____ (en anglais, ____) d'une variable est l'ensemble des lignes ou elle est connue",
    "Le choix du signe égal pour désigner l'affectation remonte au langage ____",
    "Les identificateurs Python sont sensibles à la ____",
    "L'instruction seconds = hours * 3600 est déconseillée, car elle contient un nombre ____",
    "Affecter une ____, c'est lier son nom à une ____ contenant sa valeur",
    "____ est une encyclopédie en ligne des suites numériques",
    "a = b se lit a ____ la valeur de b",
    "Le ____ libère les emplacements occupés par des valeurs sans nom",
    "En python, on écrit les variables en ____",
    "i += 1 ____ la variable i",
    "Chaque fois que Python évalue une expression, il stocke sa valeur à une certaine ____", # FAUX
    "La variable SECOND_PER_MINUTE est considérée par convention comme une ____",
    "Une ____ produit une valeur, qui apparaît dans la zone ____ du notebook",
    "Le type de la fonction arythmetic_series est ____,",
    "La taille des chaînes ou des entier Python est ____ pourvu qu'il y ait assez de mémoire",
    "input(prompt) ____ la fonction input en lui ____ prompt",
    "L'____ d'un opérateur est le nombre d'____ qu'il accepte",
    "Un opérateur peut être vu comme une fonction présentée sous forme ____",
    "Le signe d'____ se note == et non pas = (déjà pris par l'____)",
    "and est ____ sur or",
    "Une ____ indique que certains blocs de lignes ne doivent être exécutés qu'à certaines ____",
    "Le type des chaînes Python est nommé ____",
    "L'instruction ____ C lève une une erreur si la condition C est fausse et ne fait rien sinon",
    "L'accès aux variables extérieures à une fonction n'est toléré que pour les ____",
    "Si un identificateur n'est pas défini dans le cadre ____, il est cherché successivement dans les autres", # FAUX
    "En programmation, on ne se répète pas (principe ____)",
    "Dans le ____-____ ____, on commence à tester le code avant même de l'avoir écrit",
    "Une variable locale ____ temporairement toute variable de même nom définie à l'e____térieur",
    "Pour évaluer une expression il faut connaître l'____ et la ____ de ses opérateurs",
    "Le langage support de ce cours d'____ est ____3",
    "Une ____ est une notation qui représente une valeur fixe dans le code source d'un programme", # FAUX
    "Le symbole * dénote la ____",
    "Une chaîne littérale est entourée de simples ou de doubles ____",
    "Peter Norvig recommande d'apprendre à programmer en ____",
    "____ est une syntaxe légère permettant d'insérer dans un texte des informations typographiques",
    "\"Hello world\" et 1  + 2 sont des ____",
    "Python a deux types de numériques : ____ et ____",
    "Un ____ est suivi d'un test ou plus exactement d'une expression ____",
    "Les conditionnelles ____ sont plus faciles à lire que les conditionnelles ____",
    "Les identificateurs existent dans des ____ (en anglais, ____) superposé(e)s",
    "Le ____ abrège une branche else consistant en une instruction ____",
    "Dans a op b, si op a la propriété de X, b n'est pas systématiquement évalué",
    "not (A and B) == (not A) or (not B) est une loi de ____",
    "(Un/une) ____ de parité s'exprime avec l'opérateur ____",
    "Un diagramme de ____ est vulgairement appelé une patate", # bon
    "a ____ (b or c) == (a and b) or (a and c)",
    "and, or, not sont des opérateurs ____",
    "Une variable locale à une fonction f fait partie des ____ de f ou est ____ dans f",
    "____ dénote l'absence de valeurs",
    "La fonction ____(____,____,____) itère sur une suite arithmétique finie",
    "\"Boucle\" se dit ____ en anglais",
    "Tous les langages ____ offrent au moins une structure de boucle",
    "L'affectation d'une variable ____ se fait en dehors de toute fonction",
    "Pour pouvoir parcourir les chiffres d'un nombre, il faut le convertir en ____",
    "Par convention, on nomme souvent une variable ____ qui joue le rôle d'accumulateur",
    "Le standard ____ 754 définit la représentation des ____",
    "Dans le schéma de ____, la fonction de combinaison est une simple ____ de l'accumulateur",
    "Une fonction qui ne retourne aucune valeur est une ____",
    "La chaine vide \"\" est ____ pour l'opération de ____",
    "Dans le schéma de ____ du meilleur élément, le nom de l'accumulateur se termine par ____",
    "n peut être un nom acceptable sous certaines conditions, et seulement s'il s'agit d'un ____",
    "Dans for c in s:, c est une ____ et s une valeur de type \"____\"",
    "NoneType est le type des ____",
    "On recommande de ne tester l'égalité de deux flottants qu'à un ____ près",
    "La valeur des variables à un moment donné constitue l'____",
    "L'utilisation de bibliothèques de ________ évite de ____ la ____",
    "La fonction d'____ n'est pas ____ avec seulement des boucles for",
    "L'introduction du ____ fait gagner en ____ et en ____ ce qu'on perd en ____",
    "Même si on connaît ____ le nombre de périodes, le calcul des ________ s'écrit mieux avec un ____",
    "La boucle while est la plus ____",
    "La représentation ____ s'obtient par divisions successives par 2",
    "Les variables d'itération de boucles ____ (____ en anglais) doivent être distinctes",
    "On emploie une boucle while pour faire ____ quelque chose jusqu'à un état ____",
    "Une boucle séquentielle ____ nécessairement",
    "On emploie une boucle for (dite ____) lorsqu'on a une ____ à parcourir",
    "Dans la plupart des langages de programmation, le premier élément d'un tableau a ____ comme ____",
    "Une liste est délimitée par des ____, un tuple par des ____",
    "La fonction ____(a,b) renvoie le ____ (a / b, a % b)",
    "Le type tuple permet l'échange sans variable ____"
    "Le type ____ de Python offre à la fois les opérations des listes et des tableaux",
    "Une ____ est utile pour terminer l'accumulation d'entrées arbitraires"
    "Un ____ est efficace pour l'accès ____"
    "Lorsqu'une boucle s'exécute une fois en trop ou en moins, on parle d'erreur ____",
    "Une boucle infinie comporte au moins une condition de sortie ____",
    "Les éléments d'une liste, comme ceux d'un tuple, sont séparés par des ____",
    "Une ____ est efficace pour l'insertion et la suppression",
    "On emploie une boucle ________ lorsqu'un nombre infini d'_____ est possible",
    "La condition du ____ est celle qui permet le plus ____ maintien de la boucle",
    "Dans une boucle infinie, les états ____ ne rapprochent pas de l'état final ____",
    "Le tuple ____ (anglais) permet de réaliser des affectations ____ ",
    "La ____ des éléments d'un tuple dépend normalement de leur ____",
    ]


solutions_list = ["float",
    "corps def",
    "arguments",
    "pep",
    "deuxpoints",
    "indenter",
    "clair",
    "braces",
    "latex",
    "return",
    "modulo",
    "importer bibliothèque library",
    "chaine",
    "chaine string",
    "print fonction standard",
    "python guido",
    "paramètres formels",
    "optionnel",
    "documente",
    "type opérateur",
    "instruction",
    "assignment",
    "pointeur",
    "déclarer affecter",
    "auxiliaire",
    "id",
    "underscores",
    "littéral",
    "conversion",
    "portée scope",
    "fortran",
    "casse",
    "magique",
    "variable adresse",
    "oeis",
    "reçoit",
    "carbagecollector",
    "minuscule",
    "incrémente",
    "adresse",
    "constante",
    "expression out",
    "function",
    "illimitée",
    "invoque passant",
    "arité opérandes", 
    "infixée",
    "égalité affectation",
    "prioritaire",
    "conditionnelle conditions",
    "str",
    "assert",
    "constantes",
    "local",
    "dry",
    "test driven development",
    "occulte",
    "associativité priorité",
    "algorithmique python",
    "littéral",
    "multiplication",
    "quotes",
    "dixans",
    "markdown",
    "expressions",
    "int float",
    "test booléenne",
    "chaînées imbriquées",
    "cadres frames",
    "elif if",
    "court-circuit",
    "demorgan",
    "test modulo",
    "venn",
    "and",
    "booléens",
    "arguments affectée",
    "none",
    "range start stop step",
    "loop",
    "impératifs",
    "globale",
    "chaine",
    "acc",
    "ieee flottants",
    "comptage incrémentation",
    "procédure",
    "neutre concaténation",
    "recherche sofar",
    "entier",
    "variableditération iterable",
    "instructions",
    "epsilon",
    "environnement",
    "tiercepartie réinventer roue",
    "ackermann calculable",
    "while puissance rapidité sûreté",
    "àlavance intérêtscomposés while",
    "générale",
    "binaire",
    "imbriquées nested",
    "évoluer terminal",
    "termine",
    "séquentielle séquence",
    "zero indice",
    "crochets parenthèses",
    "divmod tuple",
    "auxiliaire",
    "list",
    "sentinelle",
    "tableau direct",
    "offbyone",
    "prématurée",
    "virgules",
    "liste",
    "whiletrue itérations",
    "while long",
    "intermédiaires terminal",
    "unpacking parallèles",
]

print("How many crosswords do you want?",
        "    if '0', all crosswords are selected",
        "    if '01', crosswords down to the first test are selected",
        "    if '02', crosswords from the first to the second test are selected", sep='\n')
try_number = input(">>> ") # How many crosswords ?

# Because we love pep8, max length for each line: 80 characters
print("Attention/Achtung:"
      "--> If there are many solutions, then juste use a space."
      "--> If the words needs \"-\", then don't write it ", sep='\n')

def to_ascii(s):
    return normalize('NFD', s).encode("ascii", "ignore").decode("utf8").upper()

solutions_list = list(map(to_ascii, solutions_list))

if try_number == '0':
    try_number = len(crosswords_list)
    print(f"Let's go for {len(crosswords_list)} crosswords ! ;)")
elif try_number == '01':
    crosswords_list = crosswords_list[0:CROSSWORDS_FIRST_GROUP-1]
    solutions_list = solutions_list[0:CROSSWORDS_FIRST_GROUP-1]
    try_number = CROSSWORDS_FIRST_GROUP
elif try_number == '02': 
    crosswords_list = crosswords_list[CROSSWORDS_FIRST_GROUP-1:]
    solutions_list = solutions_list[CROSSWORDS_FIRST_GROUP-1:]
    try_number = len(crosswords_list)
else:
    try_number = int(try_number)


for _ in range(try_number):
    number_in_list = randint(0, len(crosswords_list)-1)
    crossword_for_this = crosswords_list[number_in_list]
    solution_for_this = solutions_list[number_in_list]

    print(crossword_for_this)
    answer = to_ascii(input(">>> "))
    answer = answer.replace(' ', '')

    if answer == solution_for_this.replace(' ', ''):
        print("Good !\n")
    else:
        if ' ' in solution_for_this:
            print(f"Solutions are : {solution_for_this}\n")
        else:
            print(f"Solution is : {solution_for_this}\n")

    crosswords_list.remove(crossword_for_this)
    solutions_list.remove(solution_for_this)
