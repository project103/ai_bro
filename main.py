# main.py
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class main(tk.Tk):
    symbol = ["O"]

    def __init__(self):
        super().__init__()

        self.geometry("350x350")
        self.title("Tic Tac Toe Game")
       

        self.background_image = Image.open("tic_tac_toe_back.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self, width=self.background_image.width(), height=self.background_image.height())
        self.canvas.pack(fill="both", expand=True)

        #self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        self.button1 = tk.Button(self.canvas, text="Ease", command=lambda: self.set_difficulty(1))
        self.button2 = tk.Button(self.canvas, text="Normal", command=lambda: self.set_difficulty(2))
        self.button3 = tk.Button(self.canvas, text="Hard", command=lambda: self.set_difficulty(3))
        self.button5 = tk.Button(self.canvas, text="vary Hard", command=lambda: self.set_difficulty(4))
        self.button4 = tk.Button(self.canvas, text="Start", command=self.check_and_open_gui)

        self.button1.place(relx=0.5, rely=0.4, anchor="center")
        self.button2.place(relx=0.5, rely=0.5, anchor="center")
        self.button3.place(relx=0.5, rely=0.6, anchor="center")
        self.button5.place(relx=0.5, rely=0.7, anchor="center")
        self.button4.place(relx=0.5, rely=0.8, anchor="center")

        self.radio_var = tk.StringVar()
        self.radio_button1 = tk.Radiobutton(self.canvas, text="X", variable=self.radio_var, value="X",
                                            command=lambda: self.set_symbol("X"))
        self.radio_button2 = tk.Radiobutton(self.canvas, text="O", variable=self.radio_var, value="O",
                                            command=lambda: self.set_symbol("O"))

        self.radio_button1.place(relx=0.2, rely=0.4, anchor="center")
        self.radio_button2.place(relx=0.8, rely=0.4, anchor="center")

        self.label = tk.Label(self.canvas, text="Main Name")
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        self.radio_label = tk.Label(self.canvas, text="Selected: None")
        self.radio_label.place(relx=0.5, rely=0.3, anchor="center")

        self.val = None


    def set_difficulty(self, difficulty):
        self.label.config(text="Ease" if difficulty == 1 else "Normal" if difficulty == 2 else "Hard"  if difficulty == 3 else "very hard")
        self.val = difficulty
        

    def set_symbol(self, selected_symbol):
     self.radio_label.config(text=f"Selected: {selected_symbol}")
     self.symbol.insert(0,selected_symbol)
   
    def get_symbol(self):
        return self.symbol



    def check_and_open_gui(self):
        if self.val and self.symbol:
            self.withdraw()  # Hide the current window
            subprocess.run(["python", "gui.py"])
        elif self.val == None:
            self.radio_label.config(text="you must select difficulty level!")
            print(self.symbol)
        else:
            self.radio_label.config(text="you must select symbols from (x,O)")
            

if __name__ == "__main__":
    app = main()
    app.mainloop()