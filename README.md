# PacMan
AI PacMan project repository 

exemples du prof : SNAKE -> https://github.com/iridia-ulb/AI-book/tree/main/Snake

main.py :  - pas beaucoup de lignes, juste les arguments à passer dans l'execution ( comme le prof le souhaite , exemple dans les autres projets)
           - lance le jeu, et "manager" du jeu
game.py : - définition du jeu et de l'interface
          - il faut rajouter le mouvement précédent du pacman ( je veux bien le faire)
ghost.py : - comportement des fantomes
search.py : - fonction de recherche pour connaitre le path vers la target
            - contient une classe NODE qui permet le backTracking du chemin à parcourir à partir du node target
utils.py : - juste des variables générales qui ne changent pas

Autre fichier à implémenter : pacman.py ( avec le comportement du pacman qui appelera surement la classe search pour la fonction AStar

Donc EDWIGE , je crois que pour l'interface c'est juste dans Game.py qu'il faut bouger ( et peut etre un peu dans Main.py)
et LOIC , il faut créer un fichier pacman.py qui contient une fonction getMovePacman(pos,grid) et implémenter Astar dans search.py
(AXELLE, iplémenter le comportemant du deuxième fantome )

