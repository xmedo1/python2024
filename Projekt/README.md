# Battleships

---
## Opis projektu
Battleships to implementacja klasycznej gry w statki stworzona w całości w języku Python przy pomocy biblioteki [pygame](https://www.pygame.org/). Aplikacja umożliwia rozgrywkę przeciwko komputerowi w dwóch trybach trudności.

### Wymagania i uruchomieine
Do uruchomienia projektu potrzebny jest moduł `pygame`. Można go zainstalować w następujący sposób:
```bash
pip install pygame
```

Aby uruchomić grę, należy wykonać polecenie:
```bash
python3 main.py
```
---

## Funkcjonalności

1. Wybór poziomu trudności.
    - Aplikacja pozwala na wybór poziomu trudności
      - Tryb Łatwy - komputer strzela losowo w pole użytkownika.
      - Tryb Trudny - po trafieniu statku komputer stara się najpierw zatopić trafiony statek w celu odznaczenia jak największej ilości pól. Takie zachowanie bardziej przypomina rozgrywkę przeciwko prawdziwemu użytkownikowi.
2. Wyświetlenie zasad gry.
    - Aplikacja umożliwia wyświetlenie zasad gry użytkownikom, którzy nie są zaznajomieni z grą w statki,
3. Wybór ułożenia statków.
    - Po wybraniu poziomu trudności, użytkownik musi ustawić swoje statki na planszy. Może to zrobić poprzez kliknięcie na statek znajdujący się po lewej stronie od planszy użytkowinka i przeciągnięcie go na planszę, w dane miejsce. Użytkownik może również obrócić swój statek, klikając przycisk `R`, podczas zmiany pozycji statku.
    - Użytkownik może również wylosować pozycję swoich statków, jeśli nie chce ich sam ręcznie ustawiać.
    - Użytkownik jest w stanie przemieszczać nawet te statki, które już są na planszy.
    - Aplikacja uniemożliwia użytkownikowi umieszczenie statku poza planszą oraz stykających się ze sobą statków
4. Rozpoczęcie gry.
    - Aby rozpocząć grę, użytkownik powinien kliknąć przycisk "Start game". W przypadku, gdy użytkownik nie rozłożył jeszcze wszystkich swoich statków, zostanie wyświetlony komunikat, aby to uczynił.
5. Rozgrywka.
   - Po lewej stronie znajduje się plansza użytkowinka, z zaznaczonym układem statków, które wybrał w poprzedniej fazie. Obok znajduje się plansza komputera, z niewidocznymi dla użytkownika statkami. Obok planszy komputera znajdują się niebieskie statki, które oznaczają statki, które pozostały komputerowi na planszy nie zatopione. W przypadku zatopienia statek zmienia kolor na czerwony.
   - Pierwszy ruch zawsze należy do użytkownika. Użytkownik wskazuje pole na planszy przeciwnika, które chciałby zatakować, a następnie je klika.
     - W przypadku pudła, pole to zostanie zaznaczone jako `pudło`, poprzez małą niebieską kropkę na tym polu. Użytkownik nie będzie mógł trafić ponownie w to pole, jak i we wszystkie inne, które już próbował strzelić.
     - W przypadku trafienia, ale nie zatopienia statku, na polu pojawi się czerwony znak `X`.
     - W przypadku zatopienia statku zmieni on kolor na czerwony, z czarnym `X`, oraz zmieni kolor na czerwony, po prawej stronie planszy komputera.
       - Ponieważ statki nie mogą się ze sobą stykać, po zatopieniu statku, jego okolica zostaje oznaczona jako `pudło`. Pozwala to uniknięcie zbędnych ruchów zarówno użytkownikowi, jak i komputerowi.
   - Gra kończy się w momencie, gdy któryś z graczy zatopi wszystkie statki przeciwnika.
6. Ekran końca gry
   - Po zakończeniu rozgrywki użytkownik może rozpocząć kolejną rozgrywkę, klikając w przycisk `Play again` lub zakończyć działanie aplikacji przyciskiem `Exit`.

---
## Struktura
Program składa się z siedmiu modułów.
### `constants.py`
Moduł `constants.py` zawiera stałe, używane w projekcie. Znajdują się tam:
- `BOARD_SIZE` - rozmiar planszy do gry (ilość kolumn i rzędów) - domyślnie w grze w statki jest to pole 10x10
- `CELL_SIZE` - rozmiar jednej komórki na planszy [px]
- `SCREEN_WIDTH`, `SCREEN_HEIGHT` - rozmiar wyświetlanego okna [px]
- definicje kolorów w RGB
- tekst zasad (`RULES`)

### `game_state.py`
Klasa przechowująca informacje o obecnym stanie gry.

### `running_states.py`
Logika funkcji main, obsługuje, jak zachowuje się aplikacja podczas każdego ekranu (`setup`, `start`,`gameplay`...)

### `gui.py`
Moduł `gui.py` jest odpowiedzialny za wyświetlanie GUI. Zawiera takie funkcje, jak:
- `draw_board` - Rysuje planszę i statki (wraz z trafieniami, bądź pudłami) na ekranie.
- `draw_button` - Rysuje interaktywne przyciski.
- `draw_ships_side` - Rysuje statki obok planszy.
- `highlight_sunk_ship` - Podświetla zatopione statki na planszy.

### `board.py`
Odpowiada za logikę związaną z zarządzaniem planszą oraz rozmieszczaniem statków.
- `is_safe` - Sprawdza, czy w danej komórce można umieścić statek.
- `can_place_ship` - Sprawdza, czy statek może zostać umieszczony we wskazanej pozycji na planszy.
- `place_ship` - Umieszcza statek na planszy we wskazanej pozycji.
- `generate_random_board` - Generuje losową konfigurację planszy ze statkami umieszczonymi zgodnie z zasadami gry.
- `clear_ship_from_board` - Usuwa statek z planszy, resetując zajęte przez niego komórki do `0`.

### `game_logic.py`
Zawiera logikę gry, w tym funkcje obsługujące tury graczy, rozpoznawanie trafień i zatopionych statków oraz logikę komputera.
- `add_ships_from_random_board` - Konwertuje układ statków losowej planszy na listę umieszczonych statków.
- `is_ship_sunk` - Sprawdza, czy statek w podanej pozycji został zatopiony.
- `process_shot` - Przetwarza strzał na planszy.
- `computer_shot_easy` - Wykonuje losowy strzał na planszę w trybie łatwym.
- `check_victory` - Sprawdza, czy wszystkie statki na planszy zostały zatopione.
- `mark_surrounding_as_missed` - Oznacza otaczające komórki zatopionego statku jako `pudło`.
- `is_valid_target` - Sprawdza, czy podane współrzędne są prawidłowym celem strzału. Używane tylko w trybie trudnym.
- `computer_shot_hard` - Wykonuje inteligentny strzał na planszy w trybie trudnym. Po trafieniu statku celuje w pobliskie cele, próbując go zatopić.

### `main.py`
Główny moduł, który uruchamia grę, zarządza stanem aplikacji i obsługuje interakcję z użytkownikiem

---
Autor: Nikodem Piechulski