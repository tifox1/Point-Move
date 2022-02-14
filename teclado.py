#Esta clase contendra todos los estados del teclado, es decir si esta precionado o no
class KeyState:
    def __init__(self):
        self.event = {
            'key_d': False,
            'key_a': False,
            'key_space': False,
            'static': False
        }
