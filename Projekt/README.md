# Battleships
## Opis projektu

---
Battleships to implementacja klasycznej gry w statki stworzona w całości w języku Python przy pomocy biblioteki [pygame](https://www.pygame.org/). Aplikacja umożliwia rozgrywkę przeciwko komputerowi w dwóch trybach trudności.


Aby uruchomić grę, należy wykonać polecenie:
```bash
python3 main.py
```

## Funkcjonalności

1. Wybór poziomu trudności.
    - aplikacja pozwala na wybór poziomu trudności
      - Tryb Łatwy - komputer strzela losowo w pole użytkownika.
      - Tryb Trudny - po trafieniu statku komputer stara się najpierw zatopić trafiony statek w celu odznaczenia jak największej ilości pól. Takie zachowanie bardziej przypomina rozgrywkę przeciwko prawdziwemu użytkownikowi.
2. Wyświetlenie zasad gry.
    - aplikacja umożliwia wyświetlenie zasad gry użytkownikom, którzy nie są zaznajomieni z grą w statki,
3. Wybór ułożenia statków.
    - po wybraniu poziomu trudności, użytkownik musi ustawić swoje statki na planszy. Może to zrobić poprzez kliknięcie na statek i przeciągnięcie go na planszę, w dane miejsce. Użytkownik może również obrócić swój statek, klikając przycisk `R`, podczas zmiany pozycji statku.
    - użytkownik może również wylosować pozycję swoich statków, jeśli nie chce ich sam ręcznie ustawiać.
    - użytkownik jest w stanie przemieszczać nawet te statki, które już są na planszy
4. Rozpoczęcie gry.
    - Aby rozpocząć grę, użytkownik powinien kliknąć przycisk "Start game". W przypadku, gdy użytkownik nie rozłożył jeszcze wszystkich swoich statków, zostanie wyświetlony komunikat, aby to uczynił.
5. Rozgrywka

## Struktura
- `constants.py`
- `gui.py`
- `board.py`
- `game_logic.py`
- `main.py`