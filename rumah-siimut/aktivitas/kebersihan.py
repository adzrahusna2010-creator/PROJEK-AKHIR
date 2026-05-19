from data import Rumah

class Kebersihan(Rumah):

    def __init__(self, nama_rumah, kebersihan, password):

        super().__init__(nama_rumah, kebersihan, password)

    def sapu(self):

        self._kebersihan += 10
        print("Rumah selesai disapu")

    def pel(self):

        self._kebersihan += 15
        print("Rumah selesai dipel")

    def rapikan(self):

        self._kebersihan += 20
        print("Rumah sudah rapi")