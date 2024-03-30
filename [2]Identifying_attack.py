import json
import csv
import os
import glob

# Configuration des chemins
chemin_base = './'  # Chemin vers les dossiers d'attaque
fichier_csv_anomalies = 'anomalies_detaillees.csv'  # Fichier CSV de sortie pour les anomalies

limite_vitesse_plausible = 50  # Limite de vitesse plausible en m/s

def charger_json(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {fichier}.")
        return None

def verifier_conditions(objet, ep):
    conditions = [
        ep['timestamp'] > objet['LastUpdateTime'],
        (objet['longitudeObserver'], objet['latitudeObserver']) != (objet['XcoordinateObj'], objet['YcoordinateObj']),
        objet['XcoordinateObserver'] != objet['XcoordinateObj'] or objet['YcoordinateObserver'] != objet['YcoordinateObj'],
        objet['XcoordinateObserver'] > objet['XcoordinateObj'] or objet['YcoordinateObserver'] > objet['YcoordinateObj']
    ]
    return all(conditions)

def analyser_et_enregistrer_anomalies(dossiers_attaques):
    with open(fichier_csv_anomalies, 'w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['Dossier', 'Fichier', 'Objet ID', 'Vitesse (m/s)', 'Incohérences'])

        for dossier in dossiers_attaques:
            chemin_dossier = os.path.join(chemin_base, dossier)
            for fichier in glob.glob(os.path.join(chemin_dossier, '*.json')):
                donnees = charger_json(fichier)
                if donnees:
                    for ep in donnees.get('EP', []):
                        for objet in ep.get('ExtendedPerceivedObjects', []):
                            vitesse = objet.get('VelocityObj', 0)
                            if vitesse > limite_vitesse_plausible or verifier_conditions(objet, ep):
                                writer.writerow([
                                    dossier,
                                    os.path.basename(fichier),
                                    objet.get('PerceivedObjectID', 'N/A'),
                                    vitesse,
                                    "Vérifiez les conditions de timestamp et de position"
                                ])

def main():
    dossiers_attaques = ['Attack4', 'Attack15', 'Attack19']
    analyser_et_enregistrer_anomalies(dossiers_attaques)
    print(f"Les analyses détaillées des anomalies ont été enregistrées dans {fichier_csv_anomalies}")

if __name__ == "__main__":
    main()
