class Player:
    def __init__(self, namn, pengar=0, boost_multiplier=1):
        self.namn= namn
        self.pengar = pengar
        self.boost_multiplier = boost_multiplier

    def earn_pengar(self, amount):
        self.pengar += amount * self.boost_multiplier

    def buy_boost(self):
        # Anta att boosten kostar 100 enheter
        boost_cost = 100
        if self.pengar >= boost_cost:
            self.pengar -= boost_cost
            self.boost_multiplier *= 2
            print(f"{self.namn} har köpt boosten! Tjänar nu pengar dubbelt så snabbt.")
        else:
            print(f"{self.namn} har inte tillräckligt med pengar för att köpa boosten.")

# Skapa en spelare
Spelare1 = Player("Spelare 1")

# Simulera att spelaren tjänar pengar
Spelare1.earn_pengar(50)
print(f"{Spelare1.namn} har nu {Spelare1.pengar} pengar.")

# Köp boosten
Spelare1.buy_boost()

# Simulera att spelaren tjänar mer pengar efter att ha köpt boosten
Spelare1.earn_money(50)
print(f"{Spelare1.namn} har nu {Spelare1.pengar} pengar.")
