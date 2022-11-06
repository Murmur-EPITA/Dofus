# Dofus Adjs-list builder
- ## Installation
1. Télécharger Python 3.11.
2. Ouvrir Powershell dans le dossier racine du bot. (Shift + clic droit dans l'explorateur de fichiers)
3. Créer environnement virtuel Python:
   1. Dans Powershell: 'python -m venv venv'
   2. '.\venv\Scripts\Activate.PS1'
   3. 'pip install -r requirements.txt'
- ## Utilisation
1. Lancer Dofus et attendre que le personnage soit sur la map.
2. Lancer le script.
   1. Comme pour l'installation, ouvrir un Powershell dans le dossier racine du bot.
   2. Activer l'environnement virtuel avec '.\venv\Scripts\Activate.PS1'
   3. 'python -m src.main'
3. Rentrer sa position actuelle dans la nouvelle fenêtre.
- ## Ce qu'il faut faire
- Se déplacer seulement avec les touches directionnelles du clavier UP, RIGHT, DOWN, LEFT (1 clic pour déplacer le 
curseur pour check si le perso peut aller dans cette direction, un deuxième pour cliquer et se déplacer)
  - Pour dire qu'on ne peut pas accéder à la case du haut, il y a juste à appuyer sur la touche 'z' du clavier.
  - Idem pour case du haut: 'd'
  - Idem pour case du bas: 's'
  - Idem pour case de gauche: 'q'
- ## Ce qu'il NE FAUT PAS faire
  - Se déplacer de case en case avec sa souris (le bot ne sait plus ou le joueur est et tout ce qui est fait après est erroné)
  - Redimensionner sa fenêtre de jeu de manière à ce que les bandes noires sur les côtés soient visibles.
  - Déplacer la fenêtre de jeu. (En cas de déplacement, appyer sur la touche 'i')
  - Aller faire autre chose sur une autre fenêtre (il faut d'abord arrêter le bot avec la touche 'b').
- ## En cas d'erreur
  - Si appuie sur une touche 'z', 'd', 's' ou 'q' par erreur, il suffit de rappuyer dessus une seconde fois.
  - Si déplacement de case avec la souris, immédiatement appuyer sur 'u' et renseigner ses positions actuelles.
  - Si redimensionnement de fenêtre, ntm et relance le bot: 'b' pour arrêter.
- ## Rappel des touches
  - 'UP_ARROW; RIGHT_ARROW; DOWN_ARROW; LEFT_ARROW': 1 fois bouge le curseur, 2 fois déplace le perso
  - 'z; d; s; q': indique qu'on ne peut pas accèder respectivement à la case du haut, de droite, du bas, de gauche, un second appuie sur la même touche annule l'action
  - 'u': ouvre une fenêtre pour renseigner sa position
  - 'b': stoppe le bot
  - 'i': bouge la fenêtre en haut à gauche pour le bon fonctionnement du bot


## Ce bot utilise la souris et le clavier pour fonctionner, ce faisant il n'est pas possible d'utiliser son ordinateur normalement lorsque le bot tourne.
## Pour ce faire, il faut installer tout ça dans une machine virtuelle.