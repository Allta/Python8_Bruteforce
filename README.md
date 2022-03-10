# TP BruteForce Password - Ynov Python B1

### Tips   

:raising_hand: Si vous avez des soucis n'hésitez pas à m'appeler. 
 
## Exercice 1 : Password Generator
 
Dans un programme python créer une fonction qui permet de générer un mot de passe aléatoire.

Il faudra utiliser la librairie `random` comme pour le TP Guess the Number. 

Pour générer une liste de caractère à utiliser vous pouvez soit créer une variable possédant tous les caractères : 

```python
strings="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
 ```
 
 Ou alors vous pouvez utiliser la librairie `strings` : 
 
 ```python 
 import string

strings = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"
chars = string.printable[:-5]
```


 
## Exercice 2: Bruteforce Password
 
Dans cet exercice il faut bruteforcer le mot de passe prédifini dans la variable : 
  

 
