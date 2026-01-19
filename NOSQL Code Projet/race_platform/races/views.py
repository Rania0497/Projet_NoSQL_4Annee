from django.shortcuts import render
from pymongo import MongoClient
import json

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['Projet']
collection = db['race_track']

def index(request):
    doc = collection.find_one({})
    tracks = doc['track'] if doc else []
    races = doc['race'] if doc else []
    
    # Normaliser tous les Track_ID en string
    for track in tracks:
        track['Track_ID'] = str(track['Track_ID'])
    
    for race in races:
        race['Track_ID'] = str(race['Track_ID'])
    
    # ========== AJOUTE CES LIGNES ==========
    # Calculer les statistiques
    stats = {
        'total_tracks': len(tracks),
        'total_races': len(races),
        'total_seating': sum(int(t['Seating']) for t in tracks),
        'avg_seating': round(sum(int(t['Seating']) for t in tracks) / len(tracks)) if tracks else 0,
        'oldest_track': min(tracks, key=lambda t: int(t['Year_Opened']))['Name'] if tracks else 'N/A',
        'oldest_year': min(tracks, key=lambda t: int(t['Year_Opened']))['Year_Opened'] if tracks else 'N/A',
        'newest_track': max(tracks, key=lambda t: int(t['Year_Opened']))['Name'] if tracks else 'N/A',
        'newest_year': max(tracks, key=lambda t: int(t['Year_Opened']))['Year_Opened'] if tracks else 'N/A',
        'biggest_track': max(tracks, key=lambda t: int(t['Seating']))['Name'] if tracks else 'N/A',
        'biggest_seating': max(tracks, key=lambda t: int(t['Seating']))['Seating'] if tracks else 'N/A',
    }
    # =======================================
    
    # Convertir en JSON pour JavaScript
    races_json = json.dumps(races)
    
    return render(request, 'races/index.html', {
        'tracks': tracks,
        'races': races,
        'races_json': races_json,
        'stats': stats  # AJOUTE CETTE LIGNE
    })