# Projet_API
Le but du projet est de créer une application python permettant de récupérer les données se
trouvant dans l’api (https://jsonplaceholder.typicode.com/) pour les insérer au niveau de la
base de données.
Pour cela nous avons tout d'abord créer en local une base de données SQL contenant les différentes classes de l'API que nous avons connecté avec notre script Python grâce au module #pymysql.
Nous avons réaliser ce projet sur la base du principe du #Model-View-Controller(MVC).
Autrement dit, nous avons partagé les têches en trois parties:
-Le Model: il contient toutes les requêtes de récupération, d'insertion , de sélection, de mise à jour et de suppression sur les différentes classes.
-Le Controller: il sert d'intermédiaire entre le Model et le View.
-Le View: C'est l'interface client, il reçoit les requêtes du client(input) et le renvoit le résultat(output).
