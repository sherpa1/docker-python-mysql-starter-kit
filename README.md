# Docker + Python + MySQL Starter Kit

## Consignes d'installation

- Créer un fichier .env à la racine du dossier en adaptant le fichier .env.example
- Adapter les fichiers ./db/sql/1-schema.sql et ./db/sql/2-data.sql

## Initialisation de la base de données

## Lancement des services
- `docker compose up`

## Suppression du volume local de base de données
- `rm -rf db/data`

## TODO

A améliorer / corriger : au premier lancement des services, l'application Python ne parvient pas à se connecter à la base de données. Il faut relancer les services pour que la connexion s'effectue (cf. https://www.datanovia.com/en/lessons/docker-compose-wait-for-container-using-wait-tool/docker-compose-wait-for-mysql-container-to-be-ready/)

--

<img src="https://sherpa.one/images/sherpa-logotype.png" width="120px">

__Alexandre Leroux__

_Enseignant / Formateur_<br>
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

https://sherpa.one
