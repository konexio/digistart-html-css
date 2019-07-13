[Instructions pour les professeurs](./formateur.md)

# Préparation

- Ouvrir votre éditeur de texte `VSCode`
- Dans la barre des tâches utilisez `Fichier > Ouvrir un dossier`
- cliquer sur le dossier `cours4` puis cliquer sur `Ouvrir`


# Instructions

Réaliser cette page HTML :

![resultat](./resultat.png)

- Créer un fichier `index.html`
- Ecrire le code pour obtenir la structure HTML principale
	`DOCTYPE` + `html` + `head` + `body`

*Vérifier régulièrement la page sur votre navigateur au fur et à mesure de l'écriture du code.*

### HTML

- Dans le `<body>` écrire le code pour avoir :

	- Une balise `<nav>` avec :
		- 1 balise `<h2>` avec le texte : `Mes vacances de rêve`
		- 1 liste `<ul>` avec 3 lignes `<li>`
		- Chaque ligne `<li>` contient une balise ancre `<a>` vers les 3 sections de la page
		- Les sections sont `Ville`, `Montagne`, `Espace`


	- Une balise `<section>` avec un ID `ville` comprenant
		- 1 balise H3
		- 1 paragraphe de texte
		- 1 image de ville (`ville.jpg`)


	- Une balise `<section>` avec un ID `montagne` comprenant
		- 1 balise `<h3>`
		- 1 paragraphe de texte
		- 1 image de montagne (`montagne.jpg`)

	- Une balise `<section>` avec un ID `espace` comprenant
		- 1 balise H3
		- 1 paragraphe de texte
		- 1 image de grands espaces (`espace.jpg`)

- Dans le `<head>`
	- Relier le fichier HTML à un fichier `style.css`

## CSS 

*Vérifier régulièrement la page sur votre navigateur au fur et à mesure de l'écriture du code.*

Créer le fichier `style.css` avec les règles suivantes :

### SELECTEURS DE TYPE ELEMENT

- Créer un sélecteur d'élément `<body>` avec pour propriété :
	- `margin` de valeur `0`

- Créer un sélecteur d'élément `<section>` avec pour propriété :
	- `padding` de valuer `30px`

- Toutes les balises `<h3>` de la page sont centrées = SELECTEUR DE TYPE ELEMENT H3
	- Propriété `text-align` avec la valeur `center`

- Pour l'élément `<nav>` :
	- Sa hauteur est de 70px, height:70px = SELECTEUR DE TYPE ELEMENT NAV
	- sa balise `<h2>` a une marge intérieure de `0px`, une marge extérieure de `20px` et se cale à gauche = SELECTEUR de TYPE ELEMENT nav + ELEMENT h2 avec les propriétés margin, padding et float

	- Sa balise `<ul>` a les propriétés suivantes : = SELECTEUR DE TYPE ELEMENT nav + ul
		- `display` avec la valeur `block` pour que la liste reste sur une seule ligne
		- `margin` avec la valeur `0` pour ne pas avoir de marge intérieure
		- `list-style` avec la valeur `none` pour ne pas avoir de puce sur chaque ligne
		- `padding` avec la valeur `24px` pour la marge extérieure

	- Ses balises `<li>` ont les propriétés suivantes : SELECTEUR DE TYPE ELEMENT nav + li
		- `float` avec la valeur `left` pour que les lignes se calent à gauche
    - `margin-left` avec la valeur `15px` pour séparer les `<li>` de 15 pixels à gauche

	- Ses balises `<a>` (ancres) utilisent la couleur noire = SELECTEUR DE TYPE ELEMENT nav + a
		- Utiliser la propriété `color` avec la valeur : `black` (ou `#000000`)

### SELECTEURS DE TYPE CLASS

- Les images de la page doivent utiliser une classe = IMAGE avec les propriétés suivantes :
	- `width` avec la valeur `300px` pour limiter la taille de l'image à 300 px
	- `border-radius` avec la valeur `10px`	pour donner un effet arrondi aux 4 coins de l'image

### SELECTEURS DE TYPE ID

- Les sections VILLE et ESPACE ont un fond de couleur `#0475BA` (couleur Konexio)
- SELECTEUR DE TYPE ID pour les id VILLE et ESPACE
	Avec la propriété `background-color` et la valeur `#0475BA`