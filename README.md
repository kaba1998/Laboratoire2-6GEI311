# Laboratoire2-6GEI311
Description :

Architecture des logiciels
Laboratoire2
 Auteur: AICHA KABA

utilisation
Avant d'executer le programme 
Aller dans le fichier Lab2  par exemple sys.path.append(
"C:/Users/Aicha/Desktop/Lab2/Lab2/x64/Release") modifier l'emplacement 
modifier aussi l'emplacement du fichier qui contienne la video par 
Lab2.Start("", "C:/Users/Aicha/Desktop/Lab2/Lab2/Example.avi")
# Pour la compilation 

Description
le programme droit etre compilé dans visual studio 
les instructions de configuration est la suivante 
il faut etre en mode Release
clique  droit sur Lab2 aller dans propriétés 
General ->  type de configuration = bibilothéque dynamique(.dll)
nom de la cible = Lab2
 parametre avancés = .pyd
Dans Répertoire VC++ clique sur repertoire include = c:/user/Aicha/AppData/Local/Programs/Python/Python310/inclure ( c'est les inclures de python )
Répertoire de bibliothéques = c:/User/Aicha/AppData/Local/Programs/Python/Python310/Libs (c'est la bibliotheque dans python)
# il faut installer le keyboard et le DirectShow avec Python3 sur ton ordinateur 
 # pour la compilation utilsateur doit executé avec python en ouvant une indice de commande 
 python PATH_TO_FILE
  
  
  Appuyer sur la touche P pause la vidéo
  si elle jouait et la fait jouer si elle était pausée
  Appuyer sur la touche A met la vitesse de la vidéo à 2x le rythme normal
  si elle était au rythme normal. Si la vidéo était déjà accélérée,
  cette touche remet sa vitesse à la normale Appuyer sur la touche 
  R recommence la vidéo au début
  Appuyer sur la touche Q ferme le programme
