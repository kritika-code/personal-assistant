from tkinter import *
import assist

def personal_assistant():
   assist.start()

def quiet():
    assist.quiet()

window = Tk() 
window.geometry("300x200")
window.wm_title("Assistant")
pane = Frame(window) 
pane.pack(fill = BOTH, expand = True) 

Label(pane, text = 'Personal Assistant', font =('Verdana', 15)).pack(side = TOP, pady = 10) 

mic = PhotoImage(file = r"F:\study\python programs\assistant\assistant\mic.png")
micimage = mic.subsample(5,5)
b1 = Button(pane, text = "StartAssistant",image=micimage,command=personal_assistant,compound = LEFT).pack(side = TOP)

off = PhotoImage(file = r"F:\study\python programs\assistant\assistant\off.png")
offimage = off.subsample(5,5)
b1 = Button(pane, text = "StartAssistant",image=offimage,command=quiet,compound = LEFT).pack(side = TOP)

exit = PhotoImage(file = r"F:\study\python programs\assistant\assistant\exit.png")
exitimage = exit.subsample(5,5)
button=Button(pane,text='exit',command=pane.quit,compound = LEFT,image=exitimage,).pack(side = TOP) 

pane.mainloop()