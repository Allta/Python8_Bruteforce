
import hashlib
import requests 

# Aller chercher le dictionnaire sur l'url via la librairie requests
# Il faut retourner une liste contenant le contenu de la page web 
def readwordlist(url):
 

#Fonction permettant de hasher le password pour le tester contre le password à trouver
#elle va hasher ce qu'on lui donne en input via la librairie hashlib
#Vous pouvez choisir la méthode hash que vous voulez mais sha1 est rapide et efficace pour ce tp
def hash(wordlistpassword):
#    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    #Check si le password hashé est le même que password à trouver
 
############# append the below code ################ 

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'volleyball'
actual_password_hash = hash(actual_password)

#Recuperation de la liste des passwords

guesspasswordlist= 

# Attaque Bruteforce
bruteforce(guesspasswordlist, actual_password_hash)
 
 
