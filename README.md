# TP_GithubActions


## 1. Lié le compte via une clé SSH

#### Pour commencer, j'ai lié mon compte Github à mon ordinateur via une clé SSH

![alt text](image.png)

---


## 2. Tester un premier workflow Github

#### J'ai suivi le tuto sur https://docs.github.com/fr/actions/quickstart et j'ai créer mon premier workflow :

![alt text](image-1.png)


---

## 3. Créer deux classes python

#### Pour l'exo 3, j'ai du créer 2 classes python, une qui s'appelle SimpleMath.py et l'autre TestSimpleMath.py :

![alt text](image-2.png)

![alt text](image-3.png)

#### ensuite j'ai tester les deux fichiers avec la commande suivante :

![alt text](image-4.png)


---

## 4.  créer un workflow pour lancer les tests

#### Pour tester les fichiers python, j'ai créer un workflow adapté :

![alt text](image-5.png)

#### Après avoir push, GitHub détectera le fichier de workflow et exécutera les actions définies sur la branche main : 

![alt text](image-6.png)


---


## 5. Créer la fonction soustraction

#### Pour cette exercice j'ai modifier mes fichiers python pour ajouter la fonction "soustraction" et son test associé :

![alt text](image-8.png)

![alt text](image-7.png)

![alt text](image-9.png)

#### On peut voir ci-dessous que les tests sont bien passé après avoir push :

![alt text](image-10.png)