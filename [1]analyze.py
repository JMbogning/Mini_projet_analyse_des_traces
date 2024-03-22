import json
import os
import csv
import glob
from collections import defaultdict

# Chemin contenant les dossiers Attack
chemin_base = './'

# Nom du fichier CSV de sortie
fichier_csv_sortie = 'ExtendedPerceivedObjects.csv'

def charger_json(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {fichier}.")
        return None

def enregistrer_dans_csv(donnees_groupees):
    with open(fichier_csv_sortie, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Dossier', 'Fichier', 'Timestamp', 'Objet']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for dossier, fichiers in donnees_groupees.items():
            for fichier, eps in fichiers.items():
                for ep in eps:
                    timestamp = ep.get('timestamp', 'N/A')
                    for objet in ep.get('ExtendedPerceivedObjects', []):
                        writer.writerow({
                            'Dossier': dossier,
                            'Fichier': os.path.basename(fichier),
                            'Timestamp': timestamp,
                            'Objet': json.dumps(objet, ensure_ascii=False)
                        })

def analyser_et_grouper_fichiers_json(dossiers_attaques):
    donnees_groupees = defaultdict(lambda: defaultdict(list))

    for dossier in dossiers_attaques:
        chemin_dossier = os.path.join(chemin_base, dossier)
        fichiers_json = glob.glob(os.path.join(chemin_dossier, '*.json'))
        for fichier in fichiers_json:
            donnees = charger_json(fichier)
            if donnees is None:
                continue
            
            for ep in donnees.get('EP', []):
                if 'ExtendedPerceivedObjects' in ep and ep['ExtendedPerceivedObjects']:
                    donnees_groupees[dossier][fichier].append(ep)
                    # Affiche chaque objet à l'écran
                    for objet in ep['ExtendedPerceivedObjects']:
                        print(json.dumps(objet, indent=4, ensure_ascii=False))
    
    return donnees_groupees

def main():
    dossiers_attaques = ['Attack4', 'Attack15', 'Attack19']
    donnees_groupees = analyser_et_grouper_fichiers_json(dossiers_attaques)
    enregistrer_dans_csv(donnees_groupees)
    print(f"Les données ont été enregistrées dans {fichier_csv_sortie}")

if __name__ == "__main__":
    main()
