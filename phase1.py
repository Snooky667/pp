import argparse
import requests
import json
from datetime import timedelta
import datetime


#. Création des todaydate pour default input user in -d & -f
today_date = datetime.date.today()
formatted_date = today_date.strftime("%Y-%m-%d")

def analyser_commande():
    parser = argparse.ArgumentParser(description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.') #. Symboles est une liste
    #. liste des options disponibles
    #. options obligatoire
    parser.add_argument('symboles', nargs='+', help="Nom d'un symbole boursier")
    #. options pas obligatoire
    
    
    parser.add_argument('-d', '--debut', help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)', default=None)
    parser.add_argument('-f', '--fin', help='Date recherchée la plus récente (format: AAAA-MM-JJ)', default=formatted_date)
    parser.add_argument('-v', '--valeur',choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], help=' La valeur désirée (par défaut: fermeture)', default='fermeture')

    args = parser.parse_args()     

    if args.debut is None:          #. Dans le cas ou on met pas de date de début
        args.debut = args.fin       #. debut = fin
    return args


def produire_historique(symbole, debut, fin, valeur):         #. Fonction pour produire lhistorique
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/' #. Grement que le prof a donner
    params = {                                                  #. Aucune calisse d'idée comment sa marche
    'début': debut,
    'fin': fin,
    }