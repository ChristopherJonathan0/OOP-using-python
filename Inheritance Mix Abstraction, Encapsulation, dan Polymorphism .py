from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount

    def get__amount(self): 
        return self.__amount 

    def set__amount(self, x): 
        self.__amount = x 

    def process_payment(self, amount):
        print("Processing payment...")

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Pembayaran tunai sebesar Rp{self._amount} diproses")


class DigitalPayment(Payment):
    def process_payment(self, amount, nameewalet):
        self.nameewalet = nameewalet
        print(f"nama e-wallet {self.nameewalet}")

class CardPayment(Payment):
    def process_payment(self, amount, cardname):
        self.cardname = cardname
        print(f"nama bank dan jenis kartu{self.cardname}")


if __name__ == "__main__":
    
    amount = int(input("Masukkan jumlah pembayaran: "))
    metode = input("Pilih metode (cash/digital/card): ").lower()

    if metode == "cash":
        p = CashPayment(amount)
    elif metode == "digital":
        p = DigitalPayment(amount)
        nama_wallet = input("Masukkan nama e-wallet: ")
        p.process_payment(amount, nama_wallet)
    elif metode == "card":
        p = CardPayment(amount)
        nama_kartu = input("Masukkan nama bank dan jenis kartu: ")
        p.cardname = nama_kartu
        p.process_payment(amount, nama_kartu)
    else:
        print("Metode tidak dikenal!")

    print("\nJumlah pembayaran:", p.get__amount())
