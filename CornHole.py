try:
    import tkinter as tk
except:
    print("You need Python 3.8 installed and Python Tkinter. This script will automatically install dependencies... :]")
    import os
    os.system('sudo apt-get install python3.8 python3-tk')
    import tkinter as tk

window = tk.Tk()
window.title("Corn Hole!!!")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

scoreRed = 0
scoreBlue = 0

global BlueWonBoolean
global RedWonBoolean
BlueWonBoolean = False
RedWonBoolean = False

RedText = tk.StringVar()
BlueText = tk.StringVar()

RedText.set(str(scoreRed))
BlueText.set(str(scoreBlue))

def addBlue():
    global scoreBlue
    scoreBlue += 1
    BlueText.set(str(scoreBlue))
    if scoreBlue == 21:
        global BlueWonBoolean
        BlueWonBoolean = True
        print("\nBlue Won!!!\nBLUE | RED\n "+str(scoreBlue)+"  :  "+str(scoreRed))
        
        global BlueWon
        BlueWon = tk.Label(text="Blue Won!!!",
                          foreground="white",
                          background="blue",
                          width=140,
                          height=10)
        BlueWon.pack(side=tk.TOP, fill=tk.X)

def addRed():
    global scoreRed
    scoreRed += 1
    RedText.set(str(scoreRed))
    if scoreRed == 21:
        global RedWonBoolean
        RedWonBoolean = True
        print("\nRed Won!!!\nRED | BLUE\n"+str(scoreRed)+"  :  "+str(scoreBlue))
        
        global RedWon
        RedWon = tk.Label(text="Red Won!!!",
                          foreground="black",
                          background="red",
                          width=140,
                          height=10)
        RedWon.pack(side=tk.TOP, fill=tk.X)

def resetScore():
    global scoreRed
    global scoreBlue
    global BlueWonBoolean
    global RedWonBoolean
    scoreRed = 0
    scoreBlue = 0
    RedText.set(str(scoreRed))
    BlueText.set(str(scoreBlue))
    BlueLabel.pack(side=tk.LEFT, fill=tk.X)
    RedLabel.pack(side=tk.RIGHT, fill=tk.X)
    
    if BlueWonBoolean == True:
        BlueWon.destroy()
        BlueWonBoolean = False
    elif RedWonBoolean == True:
        RedWon.destroy()
        RedWonBoolean = False
    
    BlueButton = tk.Button(window, text = "Blue Point", bg = "blue", fg = "yellow", width=30, height=15, command = addBlue)
    RedButton = tk.Button(window, text = "Red Point", bg = "red", fg = "black", width=30, height=15, command = addRed)
    ResetButton = tk.Button(window, text = "Reset", width=10, height=3, command = resetScore)
    
    BlueLabel.pack(side=tk.LEFT, fill=tk.X)
    RedLabel.pack(side=tk.RIGHT, fill=tk.X)

def Quit():
    print("Thanks for playing!!!")
    exit()

while True:
    try:
        title = tk.Label(
                        text="Corn Hole!!!",
                        foreground="green",
                        background="white",
                        width=175,
                        height=3
                        )

        BlueLabel = tk.Label(
                            textvariable=BlueText,
                            foreground="blue",
                            background="white",
                            width=10,
                            height=5
                            )

        RedLabel = tk.Label(
                            textvariable=RedText,
                            foreground="red",
                            background="white",
                            width=10,
                            height=5
                            )
        
        BlueButton = tk.Button(window, text = "Blue Point", bg = "blue", fg = "yellow", width=30, height=15, command = addBlue)
        RedButton = tk.Button(window, text = "Red Point", bg = "red", fg = "black", width=30, height=15, command = addRed)
        ResetButton = tk.Button(window, text = "Reset",bg = "orange", fg = "black", width=10, height=3, command = resetScore)
        quitButton = tk.Button(window, text = "Quit :[", bg = "yellow", fg = "orange", command = Quit)
        
        image = tk.PhotoImage(file="cornHole.png")
        imageLabel = tk.Label(image=image)
        
        BlueLabel.pack(side=tk.LEFT, fill=tk.X)
        RedLabel.pack(side=tk.RIGHT, fill=tk.X)
        
        title.pack(side=tk.TOP, fill=tk.X)
        BlueButton.pack(side=tk.LEFT, fill=tk.X)
        RedButton.pack(side=tk.RIGHT, fill=tk.X)
        imageLabel.pack(side=tk.TOP, fill=tk.X)
        quitButton.pack(side=tk.BOTTOM, fill=tk.X)
        ResetButton.pack(side=tk.BOTTOM, fill=tk.X)
        
        window.mainloop()
    except:
        exit()
