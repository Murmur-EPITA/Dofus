# Dofus Adjs-list builder
- ## Utilisation
1. Lancer Dofus et attendre que le personnage soit sur la map.
2. Lancer le script.
3. Rentrer sa position actuelle dans la nouvelle fenêtre.
- ## Ce qu'il faut faire
- Se déplacer seulement avec les touches directionnelles du clavier UP, RIGHT, DOWN, LEFT (1 clic pour déplacer le 
curseur pour check si le perso peut aller dans cette direction, un deuxième pour cliquer et se déplacer)
  - Pour dire qu'on ne peut pas accéder à la case du haut, il y a juste à appuyer sur la touche 'a' du clavier.
  - Pour case du haut: 'd'
  - Pour case du bas: 's'
  - Pour case de gauche: 'q'
- ## Ce qu'il NE FAUT PAS faire
  - Se déplacer de case en case avec sa souris (le bot ne sait plus ou le joueur est et tout ce qui est fait après est erroné)
  - Redimensionner sa fenêtre de jeu
  - Aller faire autre chose sur une autre fenêtre (il faut d'abord arrêter le bot avec la touche 'b')
- ## En cas d'erreur
  - Si appuie sur une touche 'z', 'd', 's' ou 'q' par erreur, il suffit de rappuyer dessus une seconde fois.
  - Si déplacement de case avec la souris, immédiatement appuyer sur 'u' et renseigner ses positions actuelles.
  - Si redimensionnement de fenêtre, ntm et relance le bot: 'b' pour arrêter.
- ## Rappel des touches
  - 'UP_ARROW; RIGHT_ARROW; DOWN_ARROW; LEFT_ARROW': 1 fois bouge le curseur, 2 fois déplace le perso
  - 'z; d; s; q': indique qu'on ne peut pas accèder respectivement à la case du haut, de droite, du bas, de gauche, un second appuie sur la même touche annule l'action
  - 'u': ouvre une fenêtre pour renseigner sa position
  - 'b': stoppe le bot
