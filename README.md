# SOSMacGyver

Description:
Le jeux est constitué d'un labyrinthe comprenant des positions.
Su ce labyrinth se positionne les objets suivants:
- des murs
- Mac Gyver
- le gardien
- les 3 items constituant la seringue (tube, ether, et l'aiguille)

Objectif du jeux:
Mac Gyver doit sortir du labyrinthe en ayant récupérer le tube, l'ether, et l'aiguille
pour fabriquer une seringue afin d'endormir le gardien.

Fonctionnalités du jeux:

- La structure (départ, emplacement des murs, arrivée), est enregistrée dans un fichier texte.
- MacGyver est contrôlé par les touches directionnelles du clavier.
- Les objets sont répartis aléatoirement dans le labyrinthe et changent d’emplacement si l'utilisateur ferme le jeu et le relance.
- La fenêtre du jeu est un carré pouvant afficher 15 sprites sur la longueur.
- MacGyver se déplace de case en case, avec 15 cases sur la longueur de la fenêtre !
- Il récupèrera un objet simplement en se déplaçant dessus.
- Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et a trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).


Créer un environnement virtuel:
windows: py -3.8 -m venv venv
mac/linux: python3 -m venv venv

Activer l'environement virtuel:
windows: source venv\Scripts\activate
mac/linux: source/bin/activate

Installer la dépendance pygame:
pip3 install -r requirements.txt
