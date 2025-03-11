import curses
import random

# Definizione dei personaggi
personaggi = {
    1: {"nome": "Guerriero", "vita": 100, "forza": 15},
    2: {"nome": "Mago", "vita": 80, "forza": 20},
    3: {"nome": "Arciere", "vita": 90, "forza": 18},
    4: {"nome": "Ladro", "vita": 70, "forza": 12},
    5: {"nome": "Cavaliere", "vita": 110, "forza": 17},
    6: {"nome": "Necromante", "vita": 85, "forza": 22},
    7: {"nome": "Druido", "vita": 95, "forza": 16},
    8: {"nome": "Chierico", "vita": 75, "forza": 14}
}

# Funzione per gestire il combattimento
def combattimento(stdscr, personaggio_giocatore, personaggio_nemico):
    stdscr.clear()
    stdscr.addstr(0, 0, f"Combattimento tra {personaggio_giocatore['nome']} e {personaggio_nemico['nome']}!")
    stdscr.refresh()
    stdscr.getch()

    while personaggio_giocatore["vita"] > 0 and personaggio_nemico["vita"] > 0:
        # Turno del giocatore
        danno_giocatore = random.randint(5, personaggio_giocatore["forza"])
        personaggio_nemico["vita"] -= danno_giocatore
        stdscr.addstr(2, 0, f"{personaggio_giocatore['nome']} infligge {danno_giocatore} danni a {personaggio_nemico['nome']}!")
        stdscr.addstr(3, 0, f"Vita di {personaggio_nemico['nome']}: {personaggio_nemico['vita']}")
        stdscr.refresh()
        stdscr.getch()

        if personaggio_nemico["vita"] <= 0:
            stdscr.addstr(4, 0, f"{personaggio_nemico['nome']} è stato sconfitto!")
            stdscr.refresh()
            stdscr.getch()
            break

        # Turno del nemico
        danno_nemico = random.randint(5, personaggio_nemico["forza"])
        personaggio_giocatore["vita"] -= danno_nemico
        stdscr.addstr(5, 0, f"{personaggio_nemico['nome']} infligge {danno_nemico} danni a {personaggio_giocatore['nome']}!")
        stdscr.addstr(6, 0, f"Vita di {personaggio_giocatore['nome']}: {personaggio_giocatore['vita']}")
        stdscr.refresh()
        stdscr.getch()

        if personaggio_giocatore["vita"] <= 0:
            stdscr.addstr(7, 0, f"{personaggio_giocatore['nome']} è stato sconfitto!")
            stdscr.refresh()
            stdscr.getch()
            break

# Funzione per gestire la selezione del personaggio
def selezione_personaggio(stdscr, titolo, personaggi_disponibili):
    curses.curs_set(0)  # Nasconde il cursore
    stdscr.clear()
    stdscr.refresh()

    # Inizializza la selezione
    selezione = 1
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, titolo)

        for i, (key, value) in enumerate(personaggi_disponibili.items()):
            x = 2 + i
            if key == selezione:
                stdscr.addstr(x, 0, f"> {value['nome']} (Vita: {value['vita']}, Forza: {value['forza']})", curses.A_REVERSE)
            else:
                stdscr.addstr(x, 0, f"  {value['nome']} (Vita: {value['vita']}, Forza: {value['forza']})")

        stdscr.refresh()

        # Gestione dell'input
        key = stdscr.getch()
        if key == curses.KEY_UP and selezione > 1:
            selezione -= 1
        elif key == curses.KEY_DOWN and selezione < len(personaggi_disponibili):
            selezione += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Invio
            return selezione

# Funzione principale del gioco
def gioco(stdscr):
    stdscr.clear()
    stdscr.refresh()

    # Selezione del personaggio del giocatore
    personaggio_giocatore_scelto = selezione_personaggio(stdscr, "Scegli il tuo personaggio (usa le frecce e premi Invio):", personaggi)
    personaggio_giocatore = personaggi[personaggio_giocatore_scelto]
    stdscr.addstr(0, 0, f"Hai scelto {personaggio_giocatore['nome']}! Buona fortuna!")
    stdscr.refresh()
    stdscr.getch()

    # Selezione del personaggio nemico
    personaggio_nemico_scelto = selezione_personaggio(stdscr, "Scegli il personaggio con cui scontrarti (usa le frecce e premi Invio):", personaggi)
    personaggio_nemico = personaggi[personaggio_nemico_scelto]
    stdscr.addstr(0, 0, f"Hai scelto di scontrarti con {personaggio_nemico['nome']}!")
    stdscr.refresh()
    stdscr.getch()

    # Combattimento
    combattimento(stdscr, personaggio_giocatore, personaggio_nemico)

    stdscr.addstr(8, 0, "Grazie per aver giocato!")
    stdscr.refresh()
    stdscr.getch()

# Avvio del gioco con curses
if __name__ == "__main__":
    curses.wrapper(gioco)
