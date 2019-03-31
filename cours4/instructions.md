COURS 4 - HTML + CSS - EXERCICE

Créer un repertoire COURS4

Créer un fichier index.html

Ecrire le code pour obtenir la structure HTML principale
	DOCTYPE + HTML + HEAD + BODY

Verifier régulièrement la page sur votre navigateur au fur et à mesure de l'écriture du code.

Dans le BODY écrire le code pour avoir :

	1 <NAV> avec :
		1 balise h2 avec le texte : mes vacances de rêve
		1 liste <UL> avec 3 lignes <LI>
		Chaque ligne LI contient une balise ancre <a> vers les 3 sections de la page
		Les sections sont montagne, ville, espace

	1 <SECTION> avec un ID 'montagne' comprenant
		1 balise H3
		1 paragraphe de texte
		1 image

	1 <SECTION> 'ville' comprenant
		1 balise H3
		1 paragraphe de texte
		1 image

	1 <SECTION> 'espace' comprenant
		1 balise H3
		1 paragraphe de texte
		1 image de grands espaces (désert ou autre paysage, grand canyon, etc)

Relier le fichier HTML a un fichier style.css

Créer le fichier style.css avec les règles suivantes :

Verifier régulièrement la page sur votre navigateur au fur et à mesure de l'écriture du code.

SELECTEURS DE TYPE ELEMENT :
Toutes les balises H3 de la page sont centrées = SELECTEUR DE TYPE ELEMENT H3
	Propriété : text-align: center

POUR L'ELEMENT NAV :
	Sa hauteur est de 70px height:70px = SELECTEUR DE TYPE ELEMENT NAV
	sa balise H2 a une marge intérieure de 0px, une marge extérieure de 20px et se cale à gauche
		= SELECTEUR de TYPE ELEMENT NAV + ELEMENT H2 avec les propriétés margin, padding et float

	Sa balise UL a les propriétés suivantes : = SELECTEUR DE TYPE ELEMENT NAV + UL
	display: avec la valeur 'block' pour que la liste reste sur une seule ligne
        margin : avec la valeur 0 pour ne pas avoir de marge intérieure
        list-style avec la valeur 'none' pour ne pas avoir de puce sur chaque ligne;
        padding avec la valeur 24px pour la marge extérieure

	Ses balises LI ont les propriétés suivantes : SELECTEUR DE TYPE ELEMENT NAV + LI
	float avec la valeur = 'left' pour que les lignes se calent à gauche
        margin-left avec la valeur '15px' pour séparer les LI de 15 px à gauche

	Ses balise A (ancres) utilise la couleur noire = SELECTEUR DE TYPE ELEMENT NAV + A
	Utiliser la propriété COLOR avec la valeur : black (ou #000000)

SELECTEURS DE TYPE CLASS :
Les images de la page doivent utiliser une classe = IMAGE avec les propriétés suivantes :
    width avec la valeur '300px'		pour limiter la taille de l'image à 300 px
    border-radius avec la valeur  '10px'	pour donner un effet arrondi aux 4 coins de l'image

SELECTEURS DE TYPE ID :
	Les sections VILLE et ESPACE ont un fond de couleur #0475BA (couleur Konexio)
	SELECTEUR DE TYPE ID pour les id 'ville' et 'espace'
	Avec la propriété : background-color et la valeur : #0475BA