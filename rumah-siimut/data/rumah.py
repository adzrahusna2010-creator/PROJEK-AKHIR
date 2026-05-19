class Rumah:

    def __init__(self, nama_rumah, kebersihan, password):

        self.nama_rumah = nama_rumah
        self._kebersihan = kebersihan
        self.__password = password

    def status(self):

        print("\n===== STATUS RUMAH =====")
        print("Nama Rumah :", self.nama_rumah)
        print("Kebersihan :", self._kebersihan)

    def tampilkan_password(self):
        print("Password Rumah :", self.__password)
