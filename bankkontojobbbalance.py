import threading
import time
from bankkonto import deposit_money  # Importera funktionen deposit_money från bank.py
import subprocess
import os

class Spelare:
    def __init__(self, namn, pengar=0, boost_multiplikator=1):
        self.namn = namn
        self.pengar = pengar
        self.boost_multiplikator = boost_multiplikator

    def tjana_pengar(self, belopp):
        self.pengar += belopp * self.boost_multiplikator

    def kopa_boost(self):
        boost_kostnad = 100
        if self.pengar >= boost_kostnad:
            self.pengar -= boost_kostnad
            self.boost_multiplikator *= 2
            print(f"{self.namn} har köpt boosten! Tjänar nu pengar dubbelt så snabbt.")
        else:
            print(f"{self.namn} har inte tillräckligt med pengar för att köpa boosten.")

def show_main():
    subprocess.run([os.sys.executable, 'main.py'])

bank_kontosaldo = 0.0  # Initialisera bankkontots saldo
spelare = Spelare("Spelare 1")  # Skapa en instans av spelaren
Vinst_per_second = 0.1  # Ange din vinsttakt per sekund här
afk_started = False
total_earned = 0.0

def visa_bank_saldo():
    global bank_kontosaldo
    print(f"Bankkontosaldo: {bank_kontosaldo:.2f}")

def satta_in_pengar(belopp):
    global bank_kontosaldo
    bank_kontosaldo += belopp
    spelare.tjana_pengar(belopp)  # Använd spelarens tjana_pengar-metod

def earn_money_while_afk():
    global total_earned, afk_started, Vinst_per_second
    while afk_started:
        spelare.tjana_pengar(Vinst_per_second)  # Använd spelarens tjana_pengar-metod
        deposit_money(Vinst_per_second)  # Sätt in de tjänade pengarna på banken
        total_earned += Vinst_per_second
        time.sleep(1)

def main():
    global afk_started, total_earned
    while True:
        user_input = input("""
Skriv 'visa saldo' för att visa ditt saldo
Skriv 'jobba' för att jobba 
Skriv 'sluta jobba' för att avsluta
Skriv 'backa' för att gå tillbaka till huvudsidan
>""")

        if user_input.lower() == 'backa':
            show_main()

        if user_input.lower() == 'jobba':
            if not afk_started:
                afk_started = True
                print("Du är nu i AFK-läge. Du kommer tjäna pengar medan du är borta.")
                threading.Thread(target=earn_money_while_afk, daemon=True).start()
            else:
                print("Du är redan i AFK-läge.")
        elif user_input.lower() == 'sluta jobba':
            if afk_started:
                afk_started = False
                print(f"Du tjänade totalt {total_earned} enheter pengar medan du var borta.")
                total_earned = 0.0
            else:
                print("Du är inte i AFK-läge.")
        elif user_input.lower() == 'visa saldo':
            visa_bank_saldo()
        else:
            print("Ogiltigt kommando. Skriv 'visa saldo', 'jobba', 'sluta jobba' eller 'backa'.")

if __name__ == "__main__":
    main()
