import requests
import tkinter as tk

def dict_entry():
    
    dict_term = input("Enter Word:").lower()
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{dict_term}?key=xxxxxxxxxxxxxxx" # insert your dictionary key here 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
            
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            for entry in data:
                print(entry["meta"]["id"])



root = tk.Tk()
root.title("Dictionary")
root.geometry("500x500")











root.mainloop()


