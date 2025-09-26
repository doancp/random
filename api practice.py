import requests


pokemon_name = input("Enter Pokemon Name: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Name: ", data["name"])
    
    print("Type(s): ")
    for Type in data["types"]:
        print("-", Type["type"]["name"])

    for t in data["types"]:
        type_url = t["type"]["url"]
    
    type_response = requests.get(type_url)
    if type_response.status_code == 200:
        type_data = type_response.json()
        print("Strong against: ")
        for Strong in type_data["damage_relations"]["double_damage_to"]:
            print("-", Strong["name"])
        print("Weak against: ")
        for Weak in type_data["damage_relations"]["double_damage_from"]:
            print("-", Weak["name"])


else:
    print("Pokemon not found")