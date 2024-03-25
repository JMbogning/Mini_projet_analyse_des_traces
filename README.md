# MINI_PROJET_ANALYSE_DES_TRACES

### I. README pour le script d'analyse des objets perçus

Ce script Python est conçu pour analyser et regrouper des informations provenant de fichiers JSON spécifiques liés à des "attaques" ou des événements similaires, puis enregistrer ces informations dans un fichier CSV. Il s'agit d'une solution idéale pour traiter et organiser des données complexes en vue d'une analyse plus approfondie.

#### Fonctionnalités principales

- **Chargement des données JSON** : Lit et charge les données depuis des fichiers JSON situés dans des dossiers prédéfinis.
- **Analyse et regroupement** : Analyse le contenu des fichiers JSON pour extraire des objets perçus étendus (Extended Perceived Objects), regroupant les données par dossier et par fichier.
- **Exportation CSV** : Enregistre les informations regroupées dans un fichier CSV, facilitant ainsi l'analyse des données.

#### Comment utiliser ce script

1. **Préparation des dossiers** : Placez vos dossiers nommés (par exemple, `Attack4`, `Attack15`, `Attack19`) contenant les fichiers JSON dans le même répertoire que le script.
2. **Exécution du script** : Lancez le script à l'aide d'un interpréteur Python. Le script parcourra automatiquement les dossiers spécifiés, lira les fichiers JSON, et regroupera les informations nécessaires.
3. **Résultats** : Les données regroupées seront enregistrées dans un fichier CSV nommé `ExtendedPerceivedObjects.csv`. Ce fichier inclura les colonnes pour le Dossier, le Fichier, le Timestamp, et l'Objet, fournissant un aperçu clair et structuré des données analysées.

#### Structure du code

- **Fonctions principales** :
  - `charger_json(fichier)`: Charge et retourne le contenu d'un fichier JSON.
  - `enregistrer_dans_csv(donnees_groupees)`: Prend les données regroupées et les enregistre dans un fichier CSV.
  - `analyser_et_grouper_fichiers_json(dossiers_attaques)`: Analyse et regroupe les données des fichiers JSON.
  - `main()`: Fonction principale orchestrant le processus d'analyse et d'enregistrement.

#### Exigences

- Python 3.x : Assurez-vous d'avoir Python 3 installé sur votre machine.
- Bibliothèques Python : `json`, `os`, `csv`, `glob`, et `collections` sont nécessaires pour exécuter ce script. Ces bibliothèques sont généralement incluses dans l'installation standard de Python.



### II. README pour le script de détection d'anomalies de vitesse

Ce script Python a pour objectif d'identifier et d'enregistrer des anomalies de vitesse dans des données issues de fichiers JSON. Ces données représentent des objets perçus lors d'événements désignés comme "attaques" et contiennent diverses informations, y compris la vitesse des objets. Les anomalies sont définies comme des instances où la vitesse d'un objet dépasse un seuil plausible prédéfini.

#### Fonctionnalités principales

- **Chargement de données JSON** : Le script lit et charge des données depuis des fichiers JSON situés dans des dossiers spécifiques.
- **Détection d'anomalies** : Il analyse ces données à la recherche de vitesses d'objets qui dépassent une limite de vitesse plausible prédéfinie.
- **Enregistrement des anomalies** : Les anomalies détectées sont enregistrées dans un fichier CSV pour une analyse ultérieure.

#### Comment utiliser ce script

1. **Organisation des données** : Assurez-vous que vos dossiers contenant les fichiers JSON (par exemple, `Attack4`, `Attack15`, `Attack19`) sont placés dans le même répertoire que le script.
2. **Exécution du script** : Lancez le script via un interpréteur Python. Le script explorera les dossiers indiqués, recherchera et analysera les vitesses contenues dans les fichiers JSON.
3. **Résultats** : Les anomalies trouvées seront sauvegardées dans un fichier CSV nommé `anomalies_vitesse.csv`, incluant les colonnes pour le Dossier, le Fichier, l'Objet ID, et la Vitesse (m/s).

#### Structure du code

- **Fonctions principales** :
  - `charger_json(fichier)`: Ouvre et charge le contenu d'un fichier JSON.
  - `enregistrer_anomalies_csv(anomalies)`: Enregistre les anomalies détectées dans un fichier CSV.
  - `analyse_plausibilite_vitesse(dossier)`: Recherche des vitesses non plausibles dans les fichiers JSON d'un dossier spécifié.
  - `main()`: Fonction principale qui orchestre la recherche d'anomalies dans plusieurs dossiers.

#### Exigences

- **Environnement** : Python 3.x est requis pour exécuter ce script.
- **Dépendances Python** : Les modules `json`, `csv`, `glob`, et `os` sont utilisés dans ce script. Ces modules sont inclus avec Python et ne nécessitent pas d'installation supplémentaire.



