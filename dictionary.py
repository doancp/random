import requests
import tkinter as tk

def dict_entry():
    
    dict_term = entry.get().lower()
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{dict_term}?key=XXXXXXXXXXXXXXXXXXXXXXXXX" # insert your key here
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        dict_def.config(text=f"Term: {data[0]['meta']['id']}")


        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            results = [] 
            for term in data:
                results.append(term["meta"]["id"])
                for meaning in term["shortdef"]:
                    results.append(" -" + meaning) 
            
            result_output = "\n".join(results)
            result_label.config(text=result_output)


root = tk.Tk()
root.title("Dictionary")
root.geometry("500x500")


entry = tk.Entry(root)
entry.pack(pady=30)

dict_button = tk.Button(root, text="Submit Word", command=dict_entry)
dict_button.pack(pady=30)

dict_def = tk.Label(root, text="")
dict_def.pack(pady=30)

result_label = tk.Label(root, text="")
result_label.pack()







button = tk.Button(root, text="Quit", font=('Arial', 20), fg=("Red"),bg=("black"), command=root.destroy) # quit button
button.place(x=400, y=400)

root.mainloop()
