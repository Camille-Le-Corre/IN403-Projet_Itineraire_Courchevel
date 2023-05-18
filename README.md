# IN403-Projet_Itineraire_Courchevel
Itinéraire du plus court chemin entre deux points de la station de ski de Courchevel

Mars et avril 2023

##################################

LE CORRE Camille

LEFEVRE Laura

LDD BI

##################################


# Introduction

Ce projet a pour but de créer un programme permettant à un skieur d’aller d’un point A à un point B dans le domaine skiable de Courchevel, le plus rapidement possible.
L’algorithme doit donc trouver le plus court chemin reliant ces 2 points, pour indiquer au skieur quelles sont les pistes et les remontées mécaniques qu’il doit emprunter.
Le skieur a la possibilité d’indiquer son niveau (débutant, intermédiaire ou téméraire), ce qui lui proposera un itinéraire adapté à son niveau.


# Le graphe

Dans un premier temps, nous avons défini les sommets du graphe. Chaque intersection entre des pistes, chaque bifurcation d’une piste, ou bien un début ou une fin d’une remontée mécanique représente un sommet. Nous en avons trouvé 188 et les avons numérotés. Chaque sommet possède également un nom suivant une nomenclature précise, afin de pouvoir décrire au skieur un lieu lors de l’affichage de l’itinéraire (ceci est détaillé par la suite).
Les arcs représentent des pistes ou des remontées mécaniques, que le skieur peut emprunter pour se rendre d’un sommet à un autre.
Le graphe obtenu est donc un graphe orienté, car on ne peut que descendre une piste et une remontée mécanique ne peut être prise que dans un seul sens.
Ce graphe est également connexe. Cependant, il n’est pas fortement connexe car le sommet 185 (représentant le village de St Bon 1100m) est accessible par une piste rouge mais aucun arc ne part de ce sommet. On peut supposer que dans la réalité, on a des navettes qui permettent de rejoindre Courchevel-Le praz 1300m qui se trouve à proximité.


# Stockage des données du graphe

Le dessin du graphe est une représentation visuelle, mais qui ne peut pas être utilisée par notre algorithme. Pour stocker les données issues du graphe, nous avons décidé d’utiliser un dictionnaire dans lequel chaque élément est un arc du graphe, qui contient plusieurs informations comme le nom de la piste ou de la remontée mécanique, la couleur de la piste, sa longueur, le type de remontée, … Au total, le graphe contient 361 arcs. Ces informations seront par la suite utilisées par l’algorithme pour trouver le plus court chemin, puis pour afficher l’itinéraire à emprunter au skieur.
Dans ce dictionnaire, les clés, uniques, sont un tuple de 3 valeurs : (sA, sB, type) avec sB un successeur de sA et le type correspond à la couleur de la piste ou au type de remontée mécanique de l’arc (sA, sB). Ce type est nécessaire pour rendre les clés du dictionnaire uniques car il existe des pistes différentes, partant d’un même sommet et arrivant à un autre même sommet. Par exemple, il y a une piste rouge et une piste noire entre les sommets 63 et
62.
Chaque clé est associée à une valeur, qui est une liste de 2 éléments : [longueur_arc, nom_arc]. Le poids d’un arc (sA, sB) correspond au temps nécessaire pour aller du sommet sA au sommet sB. Le temps de descente d’une piste est défini en fonction de sa longueur, de sa couleur et du niveau du skieur. En effet, plus une piste est difficile et plus les skieurs téméraires iront vite tandis que les débutants iront lentement. Pour chaque couleur de piste, un temps de descente est donné pour un skieur de niveau intermédiaire. A partir de ce temps de base, un coefficient de vitesse est appliqué pour obtenir les temps des skieurs de niveau débutant ou téméraire.

Pour plus de réalisme, nous avons décidé de faire jouer également la longueur de la piste. Les temps indiqués dans ce tableau sont les temps nécessaires pour parcourir une unité de piste. Une unité correspond à la longueur de la piste tothor (près du téléski Epicéa, du sommet 159 à 153). Ainsi, pour une piste environ 2 fois plus grande que la piste tothor, il faudra multiplier les temps par 2.

Le temps d’une remontée mécanique repose sur le temps d’attente moyen, le type de remontée et sa longueur. En effet, les téléphériques sont plus rapides que les télécabines, eux-mêmes plus rapides que les télésièges, qui vont plus vite que les téléskis. Nous avons également décidé d’intégrer les remontées gratuites, dont la vitesse est la même que les téléskis. Nous avons estimé le temps moyen d’attente de 5 minutes. Une unité de longueur est la même que pour les pistes : c’est la longueur de la piste tothor.


# Le plus court chemin

Nous avons choisi l’algorithme de Dijkstra pour déterminer le plus court chemin entre les deux sommets choisis par l’utilisateur. Cette partie est le cœur du projet, il était donc important de trouver un bon algorithme pour répondre de manière efficace à la demande de l’utilisateur.

On se trouve dans un problème de plus court chemin en One to one (une origine, une destination) correspondant au sommet de départ (là où se trouve le skieur) et au sommet de destination du skieur. Ces deux points étant choisis par l’utilisateur, il nous fallait aussi trouver un moyen de sélection approprié qui sera détaillé dans la dernière partie.

Pour expliquer le choix de l’algorithme, celui de Dijkstra correspondait bien avec notre cas puisque notre graphe n’a pas de valeurs négatives et c’est un cas non traitable avec cet algorithme. Il permet d’obtenir une complexité en O(n2) en utilisant un tableau. 
Néanmoins, il existe un moyen plus facile et efficace mais il faut que le graphe soit un DAG. Or, ce n’est pas notre cas. On aurait aussi pu utiliser l’algorithme de Ford-Bellman mais sa complexité est en O(n.m), il n’est donc pas conseillé d’utiliser cet algorithme pour des graphes denses qui donnerait une complexité en O(n3). Ayant un graphe plutôt complexe, nous avons éliminé cette possibilité. De plus, il existe l’algorithme de Floyd-Warshall mais celui-ci est utilisé pour du All to all, ce qui ne concorde pas avec notre situation.


# Affichage de l'itinéraire

Une fois le plus court chemin trouvé par l’algorithme de Dijkstra, il faut transmettre les informations des arcs successifs à parcourir au skieur. En effet, cet algorithme renvoie une liste des numéros des sommets successifs avec entre les sommets, le type de l’arc à emprunter. Il est donc important de transformer cette liste de sommets en une série d'indications claires à donner au skieur, qui puisse être compréhensible par tout le monde.

Par exemple, la liste [45, ‘ts’, 59, ‘r’, 55] signifie que le skieur doit d’abord prendre le télésiège du sommet 45 au sommet 59, puis qu’il doit descendre la piste rouge entre les sommets 59 et 55.


# Interface graphique

L’interface graphique repose sur l’utilisation de la librairie tkinter. Elle est découpée en plusieurs parties, en fonction de la phase dans laquelle l’utilisateur se trouve. Ces phases sont les suivantes :

	1- Accueil sur l’application
	2 - Sélection du niveau
	3- Sélection du sommet de départ et du sommet d’arrivée
	4- Consultation de l’itinéraire du plus court chemin

À tout moment, il est possible de revenir à la phase 2 grâce à un bouton “Retour” situé en bas à droite de la fenêtre.

Phase 1 : accueil sur l’application

Dans un premier temps, une image du logo de la station est affiché pendant 2 secondes, elle sert d’accueil sur l’application. Pour cela, les librairies Image et ImageTk sont utilisées.
L’image n’est affichée que si l’utilisateur vient de lancer l’application. Elle ne doit pas être affichée lorsque celui-ci appuie le bouton “Retour”.

Phase 2 : sélection du niveau

Le skieur doit maintenant sélectionner son niveau parmi trois proposés. Comme décrit précédemment, il s’agit du niveau “débutant”, “intermédiaire” ou “téméraire”. Il faut stocker ce choix dans une variable globale (niveau_skieur). Cette variable sera utilisée par la suite afin de calculer les temps de descente des pistes lors de la recherche du plus court chemin.

Phase 3 : Sélection du sommet de départ et du sommet d’arrivée

Une fois le niveau sélectionné, une nouvelle image s’affiche. Il s’agit du plan de la station. On y retrouve chacun des 188 sommets sur lesquels nous nous basons depuis le début. Le plan est affiché grâce aux librairies Image et ImageTk. Le skieur doit à présent choisir son sommet de départ et son sommet d’arrivée. Le premier sommet qu’il clique est le sommet de départ, le deuxième est le sommet d’arrivée. Un sommet sélectionné devient rouge. Deux sommets, pas un de moins, pas un de plus doivent être sélectionnés pour pouvoir demander l’itinéraire du plus court chemin. L'utilisateur peut ensuite cliquer sur le bouton "Obtenir l'itinéraire".
