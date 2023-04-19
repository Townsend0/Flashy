import pandas
import tkinter
import random
import json
import arabic_reshaper
import bidi.algorithm

class Flashy:

    def screen_settings(self):
        self.screen = tkinter.Tk()
        self.screen.minsize(1000, 750)
        self.screen.title("Flashy")
        self.screen.config(bg = "#B1DDC6")

    
    def wrong_button(self):
        self.wrong_img = tkinter.PhotoImage(file = "wrong.png")
        self.x = tkinter.Button(image = self.wrong_img, bg = "#B1DDC6", activebackground = "#d63943")
        self.x.place(x = 150, y = 600)


    def right_button(self):
        self.right_img = tkinter.PhotoImage(file = "right.png")
        self.o = tkinter.Button(image = self.right_img, activebackground = "#30bf60")
        self.o.place(x = 750, y = 600)


    def card(self):
        self.card = tkinter.Canvas(width = 820, height = 550, highlightthickness = 0, bg = "#B1DDC6")
        self.front_img = tkinter.PhotoImage(file = "card_front.png")
        self.change = self.card.create_image(410, 275, image = self.front_img)
        self.card.place(x = 90, y = 25)
        self.language = tkinter.Label(text = "English", font = ("arial", 30, "normal"), bg = "white")
        self.language.pack(pady = 50)
        self.file = json.load(open("word.json"))
        self.word_index = str(random.randint(1, 999))
        self.word = tkinter.Label(text = self.file[self.word_index]["English"], bg = "white", font = ("arial", 40, "bold"))
        self.word.pack(pady = 100)

    
    def card_front(self):
        self.img = tkinter.PhotoImage(file = "card_front.png")
        self.card.itemconfig(self.change, image = self.img)
        self.language.config(text = "English", bg = "white", fg = "black")
        self.word_index = str(random.randint(1, 999))
        try:
            self.file[self.word_index]
        except KeyError:
            Flashy.card_front(self)
        else:
            self.word.config(text = self.file[self.word_index]["English"], bg = "white", fg = "black")
        self.x.config(state = "disabled")
        self.o.config(state = "disabled")
        def count_down(a):
            self.time.config(text = a)
            if a > 0:
                self.time.after(1000, count_down, a - 1)
            else:
                Flashy.card_back(self)
        count_down(5)



    def card_back(self):
        a = arabic_reshaper.reshape("العربية")
        self.img = tkinter.PhotoImage(file = "card_back.png")
        self.card.itemconfig(self.change, image = self.img)
        self.language.config(text = bidi.algorithm.get_display(a), bg = "#91c2af", fg = "white")
        self.word.config(text = self.file[self.word_index]["Arabic"], bg = "#91c2af", fg = "white")
        self.x.config(state = "active")
        self.o.config(state = "active")
    

    def remove_word(self):
        self.delete = self.file
        del self.delete[self.word_index]["English"]
        del self.delete[self.word_index]["Arabic"]
        self.file.update(self.delete)
        json.dump(self.file, open("word.json", "w"), indent = 4, ensure_ascii = False)
        Flashy.card_front(self)


    def skip_word(self):
        Flashy.card_front(self)


    def timer(self):
        self.time = tkinter.Label(text = "", font = ("courier", 40, "bold"), bg = "#B1DDC6")
        self.time.place(x = 485, y = 630)

