from data import *

a = Flashy()
a.screen_settings()
a.wrong_button()
a.right_button()
a.card()
a.timer()
a.card_front()

def remove_word():
    a.remove_word()

def skip_word():
    a.skip_word()

a.o.config(command = remove_word)
a.x.config(command = skip_word)

a.screen.mainloop()