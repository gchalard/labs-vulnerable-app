# 1. Architecture

| Composant | Technologie | Exposition | Description |
|-----------|-------------|------------|-------------|
| Frontend | React.js | 0.0.0.0:2345 | Permet d'interagir avec l'API |
| API | Flask | 0.0.0.0:1234 | Permet d'interagir avec la DB de manière "procédurale" |
| IDP | Keycloak | 0.0.0.0:8080 | Permet d'enregister et d'authentifier les utiisateurs de l'application |
| DB | PostgreSQL | NA | Enregistre les utilsateurs et données de l'App |

# 2. Objectif
Compromettre l'intégrité des données, e.g supprimer/modifier les blogs des autres utilisateurs.

# 3. Déroulement
## 3.1. S'enregistrer
## 3.2. Compromission

# 4. Solution
## 4.1. Enregistrement
4.1.1.
![alt text](image.png)
4.1.2.
![alt text](image-1.png)
## 4.2. Compromission
4.2.1. Création d'un blog
![alt text](image-2.png)
4.2.2. Récupération du JWT
![alt text](image-3.png)
4.2.3. Modification du JWT
![alt text](image-4.png)
![alt text](image-5.png)
2 Solutions :
- modifier le sub
![alt text](image-7.png)
![alt text](image-8.png)
- modifications des rôles pour avoir le rôle 'admin'
![alt text](image-6.png)
4.2.4. Utiliser votre client HTTP favori pour modifier les headers et mettre le nouveau JWT
![alt text](image-9.png)