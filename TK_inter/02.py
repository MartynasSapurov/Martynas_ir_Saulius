import tkinter as tk #Bibliotekos įtraukimas į projektą

window = tk.Tk() #Pagtrindinio lango sukūrimas
button = tk.Button(text="Python rules!!!",
                 fg="yellow",
                 bg="blue",
                 width=20, #Plotis simboliais
                 height=20 #Aukštis taškais
                 )
button.pack()
"""
label = tk.Label(text="Python rules!!!",
                 fg="gold",
                 bg="#3400FE",
                 width=20, #Plotis simboliais
                 height=20 #Aukštis taškais
                 ) #Antraštės sukūrimas
label.pack() #Prijungiame antraštę prie pagrindinio lango, kas bus jei praleisime šią eilutę?
"""
window.mainloop() #Paleidžiame pagrindinį ciklą
