import json
import csv
import glob
import os

# Chemin contenant les dossiers Attack
chemin_base = './'  

# Nom du fichier CSV de sortie pour les anomalies
fichier_csv_anomalies = 'anomalies_vitesse.csv'  

# Limite de vitesse plausible en m/s
limite_vitesse_plausible = 50  

def charger_json(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {fichier}.")
        return None

def enregistrer_anomalies_csv(anomalies):
    with open(fichier_csv_anomalies, 'w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['Dossier', 'Fichier', 'Objet ID', 'Vitesse (m/s)'])
        for anomalie in anomalies:
            writer.writerow(anomalie)

def analyse_plausibilite_vitesse(dossier):
    chemin_dossier = os.path.join(chemin_base, dossier)
    fichiers_json = glob.glob(os.path.join(chemin_dossier, '*.json'))
    anomalies = []
    
    for fichier in fichiers_json:
        donnees = charger_json(fichier)
        if donnees is None:
            continue
        
        for ep in donnees.get('EP', []):
            for objet in ep.get('ExtendedPerceivedObjects', []):
                vitesse = objet.get('VelocityObj')
                if vitesse is not None and vitesse > limite_vitesse_plausible:
                    anomalie = (dossier, os.path.basename(fichier), objet.get('PerceivedObjectID'), vitesse)
                    anomalies.append(anomalie)
                    print(f"Anomalie détectée: {anomalie}")
                    
    return anomalies

def main():
    dossiers_attaques = ['Attack4', 'Attack15', 'Attack19']
    toutes_anomalies = []
    
    for dossier in dossiers_attaques:
        print(f"Analyse du dossier: {dossier}")
        anomalies = analyse_plausibilite_vitesse(dossier)
        toutes_anomalies.extend(anomalies)
    
    if toutes_anomalies:
        enregistrer_anomalies_csv(toutes_anomalies)
        print(f"Les anomalies ont été enregistrées dans {fichier_csv_anomalies}")
    else:
        print("Aucune anomalie de vitesse détectée.")

if __name__ == "__main__":
    main()
