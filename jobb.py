import threading
import time
from bankkonto import deposit_money
import subprocess
import os

def show_main():
    subprocess.run([os.sys.executable, 'main.py'])

earning_rate_per_second = 0.1
total_earned = 0.0
afk_started = False

def earn_money_while_afk():
    global total_earned
    while afk_started:
        total_earned += earning_rate_per_second
        deposit_money(earning_rate_per_second)
        time.sleep(1)

def main():
    global afk_started, total_earned
    while True:
        user_input = input("""
Skriv 'WORK' för att jobba 
Skriv 'STOP WORK' för att avsluta
Skriv 'Backa' för att gå tillbacka till huvudsidan
>""")

        if user_input.lower() == 'backa':
            show_main()

        if user_input.lower() == 'work':
            if not afk_started:
                afk_started = True
                print("You are now in AFK mode. You'll earn money while AFK.")
                threading.Thread(target=earn_money_while_afk, daemon=True).start()
            else:
                print("You are already in AFK mode.")
        elif user_input.lower() == 'stop work':
            if afk_started:
                afk_started = False
                print(f"You earned a total of {total_earned} units of money while AFK.")
                total_earned = 0.0
            else:
                print("You are not in AFK mode.")
        else:
            print("Invalid command. Please type 'work' to start or 'stop work' to stop.")

if __name__ == "__main__":
    main()



