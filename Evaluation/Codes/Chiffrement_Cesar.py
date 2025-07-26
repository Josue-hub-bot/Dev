def generate_key(n):
	
	# Lettres utilisées pour le mappage
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	# Nous allons utiliser un dictionnaire pour faire le mappage
	key = {}
	cnt = 0
	
	# Génère la clé
	for c in letters:
		# Le modulo permet de gérer un nombre qui déborde du nombre de lettre
		# Le modulo permet de redémarrer au début si la valeur de c est
		# plus grande que 25
		key[c] = letters[(cnt + n) % len(letters)]
		cnt += 1
	
	return key

# Vérifions que notre clé est bien générée
key = generate_key(3)
print("Clé de chiffrement :",key)

def encrypt(key, message):
	
	# Va contenir le message chiffré
	secret = ""
	
	# Vous devez créer une boucle for qui vérifie si le caractère est dans
	# dans la clé de mappage. Si oui, on le substitue. Sinon, on le
	# le remet tel quel.
	for c in message:
		if c in key:
			secret += key[c]
		else:
			secret += c
	return secret

# Genere la clé de chiffrement
def generate_dkey(key):
	dkey = {}
	for c in key:
		dkey[key[c]]=c
	return dkey

# Vérifions que le chiffrement fonctionne
message = "MON NOM EST JOSUE ALBERT"
secret = encrypt(key, message)
print("message initial :",message)
print("message chiffré :",secret)

# On génère une clé de mappage différente pour chiffrer
dkey = generate_dkey(key)
message = encrypt(dkey, secret)
print ("message déchiffré :", message)