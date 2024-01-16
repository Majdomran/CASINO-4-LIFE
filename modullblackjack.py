import random

def nämn():
    spelare=input("Vad heter du som ska spela?") # här lägg user sitt nämn
    print ("välkomen till blackjack",spelare)
nämn()

def skapa_kortlek():
    kortnummer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # här ligger nummer user kan få.
    kortfärger = ['Hjärter', 'Ruter', 'Klöver', 'Spader'] # här ligger olika type av färger på kort.
    kortlek = [{'nummer': nummer, 'färg': färg} for nummer in kortnummer for färg in kortfärger]# här kombinera vi nummer och färger, och sedan blandar kortleken
    random.shuffle(kortlek)
    return kortlek

def räkna_poäng(hand): # här räknar poängen för varje kort i handen
    poäng = 0
    ess_räknare = 0

    for kort in hand:
        if kort['nummer'] in ['K', 'Q', 'J']: # Om nummer är  K, Q ,J kommer det blir + eller = 10
            poäng += 10
        elif kort['nummer'] == 'A': # Om nummer är A kommer det blir + eller = 10
            ess_räknare += 1
            poäng += 11
        else:
            poäng += int(kort['nummer'])

    while poäng > 21 and ess_räknare:  # Om poängen är över 21 och det finns ess, räknas esset som 1 istället för 11
        poäng -= 10
        ess_räknare -= 1

    return poäng


def visa_hand(hand): # här visas vilka kort som 
    for kort in hand:
        print(f"{kort['nummer']} av {kort['färg']}")


def blackjack():

    kortlek = skapa_kortlek()

    spelare_hand = [kortlek.pop(), kortlek.pop()]
    dator_hand = [kortlek.pop(), kortlek.pop()]

    while True:
        spelare_poäng = räkna_poäng(spelare_hand)
        dator_poäng = räkna_poäng(dator_hand)

        print("\nDin hand:")
        visa_hand(spelare_hand)
        print(f"Poäng: {spelare_poäng}")

        if spelare_poäng == 21: # om spelare pöäng är exkt 21 blir de blackjack 
            print("Grattis!, Du har Blackjack!")
            break # Sen sluta spelet
        elif spelare_poäng > 21: # om spelare pöäng är mer än 21 blir de ett förlöst.
            print("Du har förlorat. Över 21 poäng.")
            break 

        val = input("Vill du ta ett till kort? (ja/nej): ").lower() # här frågar vill om spelare vill ta mer kort eller inte 

        if val == 'ja': # om spelare säger ja plusa vi kort han här redan.
            spelare_hand.append(kortlek.pop())
        else:
            break

    while dator_poäng < 17: # här säger vi att om dator ska ta mer om de här mindre än 17.
        dator_hand.append(kortlek.pop())
        dator_poäng = räkna_poäng(dator_hand)

    print("\nDatorns hand:")
    visa_hand(dator_hand)
    print(f"Datorns poäng: {dator_poäng}")

    if dator_poäng > 21: # om dator här mer än 21 så skriver de som stå under.
        print("Datorn har över 21 poäng. Du vinner!")
    elif spelare_poäng > dator_poäng:# om spelare ha mer än dator men inte mellan än 21 så vinner spelare.
        print("Grattis! Du vinner!")
    elif spelare_poäng < dator_poäng:# om spelare ha mindre än dator och dator ha mindre än 21 så vinner dator
        print("Du förlorar. Datorn vinner.")
    else:# om badå spelare och dator få samma blir det oavgjort.
        print("Det blev oavgjort.")

if __name__ == "__main__":
    blackjack()