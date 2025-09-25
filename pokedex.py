import requests
import tkinter as tk



def get_pokemon():

    pokemon_name = entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        poke_name.config(text=f"Name: {data['name']}")

        type_name.config(text="Type(s): " + ",".join(t["type"]["name"] for t in data["types"]))

        for tu in data["types"]:
            type_url = tu["type"]["url"]
        type_response = requests.get(type_url)
        type_data = type_response.json()
        strong_name.config(text="Strong against: " + ",".join(s["name"] for s in type_data["damage_relations"]["double_damage_to"]))
        weak_name.config(text="Weak against: " + ",".join(w["name"] for w in type_data["damage_relations"]["double_damage_from"]))


    else:
        poke_name.config(text="Pokemon not found")


root = tk.Tk()
root.title("Pokedex")
root.geometry("500x500")


entry = tk.Entry(root)
entry.pack(pady=30)

poke_button = tk.Button(root, text="Submit Pokemon Name", command=get_pokemon)
poke_button.pack(pady=40)

poke_name = tk.Label(root, text="", fg=("dark red"))
poke_name.pack()

type_name = tk.Label(root, text="", fg=("red"))
type_name.pack()

strong_name = tk.Label(root, text="", fg=("blue"))
strong_name.pack()

weak_name = tk.Label(root, text="", fg=("indigo"))
weak_name.pack()


button = tk.Button(root, text="Quit", font=('Arial', 20), fg=("Red"),bg=("black"), command=root.destroy) # quit button
button.place(x=400, y=400) # places quit button at that coordinates on window

root.mainloop()