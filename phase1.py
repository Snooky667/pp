import argparse
import requests
import json
from datetime import timedelta
import datetime

def analyser_commande():
    parser = argparse.ArgumentParser(description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.') #. Symboles est une liste
    #. liste des options disponibles
    #. options obligatoire
    parser.add_argument('symboles', nargs='+', help="Nom d'un symbole boursier")
    #. options pas obligatoire
    
    
    parser.add_argument('-d', '--debut', help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)', default=None)
    parser.add_argument('-f', '--fin', help='Date recherchée la plus récente (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur',choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], help=' La valeur désirée (par défaut: fermeture)', default='fermeture')

    args = parser.parse_args()
    print(args)