import requests
from tkinter import *

response = requests.get(url = "https://api.kanye.rest/")
data  =response.json()
quote = data['quote']
print(quote)

window  = Tk()
window.title("Random Quote")
window.config(bg = "black")
window.minsize(height = 300 , width = 500)

def regenerate():
    response = requests.get(url = "https://api.kanye.rest/")
    response.raise_for_status()
    data  =response.json()
    quote = data['quote']
    label.config(text = quote)
    print(quote)

label  =Label(text = f"{quote}", bg = "black" , fg = "white" , font = ('Arial' , 15 , "bold"))
label.config(wraplength= 500 , justify = 'center')
label.pack(pady = 50 ,padx = 15)
button = Button(text = "Regenerate" , bg = "black", fg ="white" , command = regenerate)
button.pack(pady = 5)

window.mainloop()