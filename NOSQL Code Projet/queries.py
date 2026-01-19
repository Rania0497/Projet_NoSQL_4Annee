from pymongo import MongoClient

# Connexion
client = MongoClient("mongodb://localhost:27017/")
db = client['Projet']          # <-- nom exact de ta DB
collection = db['race_track']  # <-- nom exact de ta collection

# Récupérer le document
doc = collection.find_one({})  # un seul document

if doc is None:
    print("⚠️ Aucun document trouvé ! Vérifie le nom de la DB et de la collection.")
else:
    # Afficher tous les circuits
    print("=== Tracks ===")
    for track in doc['track']:
        print(track)

    # Afficher toutes les courses
    print("\n=== Races ===")
    for race in doc['race']:
        print(race)

    # Afficher les courses d'un circuit spécifique (Track_ID = "2")
    print("\n=== Courses du circuit Track_ID=2 ===")
    for race in doc['race']:
        if race['Track_ID'] == "2":  # ou int(race['Track_ID']) == 2 si tu convertis en nombre
            print(race)
