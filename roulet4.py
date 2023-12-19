import random

def snurra_hjulet():
    return random.randint(0, 36)

def avgör_vinst(bet, resultat):
    return bet == resultat

def main():
    print("Välkommen till Enkel Roulette!")

    while True:
        input("Tryck Enter för att snurra hjulet...")
        
        resultat = snurra_hjulet()
        print(f"Bollen hamnade på {resultat}!")

        try:
            insats = int(input("Placera din insats (mellan 0 och 36): "))
        except ValueError:
            print("Ogiltig inmatning. Ange ett giltigt nummer.")
            continue

        if not (0 <= insats <= 36):
            print("Ogiltig insats. Ange ett nummer mellan 0 och 36.")
            continue

        if avgör_vinst(insats, resultat):
            vinstbelopp = insats
            print(f"Grattis! Du vann {vinstbelopp} gånger din insats.")
        else:
            vinstbelopp = -insats
            print("Tyvärr, du förlorade den här omgången.")

        spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
        if spela_igen != 'ja':
            print("Tack för att du spelade. Adjö!")
            break

if __name__ == "__main__":
    main()
