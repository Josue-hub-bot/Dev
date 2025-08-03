import math
import random

def est_premier(p):
    # est _premier(p) verifie si p est un nombre Permier 
    # p(int) etant un nombre à vérifier
    # return: false ou True
    
    for i in range(2, math.isqrt(p)+1):
        # si la division n'a pas de reste alors il n'est pas premier
        if p % i == 0:
            return False
    return True

def trouve_premier(size):
    # Truver un nombre premier de maniere aleatooire. 
    # On recherche le nombre du debut de size jusqu'au double
    # size(int) le nombre à vérifier
    # return (int) un nombre premier aleatoire

    while True:
        p= random.randrange(size, 2*size)
        if est_premier(p):
            return p

def lcm(a, b):
    """
	lcm(a, b)
	Trouve le plus petit multiple commun entre a et b.
	
	Paramètres:
	a (int)
	b (int)
	
	Return
	(int)
	"""
    return a*b//math.gcd(a, b)

def trouve_e(lambda_n):
    """
	trouve_e(lambda_n)
	Trouver un entier e tel que 1 < e < λ(n) et
	gcd(e, λ(n)) = 1.
	
	Paramètres:
	lambda_n (int) : l'extrémité supérieure.
	
	Return:
	(int)
	(logical) False : si ne trouve pas
	"""
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def trouve_d(e, lambda_n):
    """
	trouve_d(e, lambda_n)
	Trouve un entier qui résout l'équation
	d⋅e ≡ 1 (mod λ(n))
	
	Paramètres:
	e (int) : e clé publique
	lambda_n : l'extrémité supérieure
	
	Return:
	(int)
	(logical) False : si ne trouve pas
	"""
    for d in range(2, lambda_n):
        if d*e % lambda_n ==1:
            return d
    return False

def facteurs(n):
    """
	facteurs(n)
	Trouve les facteurs de n.
	
	Paramètres:
	n (int) : le nombre que l'on veut trouver les facteurs.
	
	Return:
	p (int) : premier facteur
	(int) : deuxième facteur
	"""
    for p in range(2, n):
        if n % p == 0:
            return p, n//p

# Generation de clé par Alice (secret)
# Etape 1 : Generation de 2 nombres premiers distincts

size = 300
p = q = 0
while p == q:
    p = trouve_premier(size)
    q = trouve_premier(size)
print("Nombres premiers p, q :", p, q)

# Etape 2 : calculer n = p*q
n = p*q
print("Le modulo n :", n)

# Etape 3 : calculer lambda(n)
lambda_n = lcm(p-1, q-1)
print("Lambda_n :", lambda_n)

# Étape 4 : choisir un entier e tel que 1 < e < λ(n)
# et gcd(e, λ(n)) = 1.
e = trouve_e(lambda_n)
print("Clé publique (exposant) e :", e)

# Étape 5 : pour trouver d, résoudre pour d l'équation d⋅e ≡ 1 (mod λ(n)).
d = trouve_d(e, lambda_n)
print("Clé secret (exposant) d :", d)

# Fin de la génération de clés
print("---------------------------")
print("Clés publiques (e, n) :", e, n)
print("Clé secrète (d) :", d)
print("---------------------------")

# Bob veut envoyer un message à Alice.
# Le message est simple
m = 2008

# Il chiffre le message
c = m**e % n
print("Le message chiffré de Bob:", c)

# Alice déchiffre le message
m = c**d % n
print("Le message pour Alice :", m)
print("---------------------------")
# Du côté d'Eve
print("Eve peut voir :")
print(" La clé publique (e, n) :", e, n)
print(" Le message chiffré de Bob :", c)

# Nous allons factoriser n
p, q = facteurs(n)
print("Facteurs d'Eve (p, q) :", p, q)

# Eve calcul lambda
lambda_n = lcm(p-1, q-1)
print("Lambda_n de Eve :", lambda_n)

# Eve calcul d
d = trouve_d(e, lambda_n)
print("Clé secrète (exposant) d'Eve d :", d)

# Eve déchiffre le message
m = c**d % n
print("Le message pour Alice qu'Eve a trouvé :", m)
print("---------------------------")

