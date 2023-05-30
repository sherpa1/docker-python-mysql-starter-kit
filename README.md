# Docker + Python + MySQL Starter Kit

## Consignes d'installation

- Créer un fichier .env à la racine du dossier en adaptant le fichier .env.example
- Adapter les fichiers ./db/sql/1-schema.sql et ./db/sql/2-data.sql

## Lancement des services
- `docker compose up`

## Suppression du volume local de la base de données
- `rm -rf db/data`

## Résultat attendu

```SQL
(1, 'Prendre rdv chez le médecin', 0, 1)
(2, 'Aller faire du sport', 1, 1)
(3, 'Prendre des vacances', 0, 1)
(4, 'Réviser mon cours', 0, 1)
exited with code 0
```

--

<img src="https://sherpa.one/images/sherpa-logotype.png" width="120px">

__Alexandre Leroux__

_Enseignant / Formateur_<br>
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

https://sherpa.one
