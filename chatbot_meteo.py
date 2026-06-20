import requests

API_KEY = "346734b16c843fc96055ce5eb09d9d24"

def obtenir_meteo(ville):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units=metric&lang=fr"

    try:
        reponse = requests.get(url)
        donnees = reponse.json()

        if reponse.status_code != 200:
            return "Ville introuvable."

        temperature = donnees["main"]["temp"]
        description = donnees["weather"][0]["description"]
        humidite = donnees["main"]["humidity"]

        return (
            f"Météo à {ville}\n"
            f"Température : {temperature}°C\n"
            f"Description : {description}\n"
            f"Humidité : {humidite}%"
        )

    except Exception as e:
        return f"Erreur : {e}"

print("=== Chatbot Météo ===")
print("Tape 'quit' pour quitter.")

while True:
    ville = input("\nEntrez une ville : ")

    if ville.lower() == "quit":
        print("Au revoir !")
        break

    resultat = obtenir_meteo(ville)
    print(resultat)