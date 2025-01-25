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


## Struktura
Program składa się z pięciu modułów.
- `constants.py` - przechowuje wszystkie stałe, używane w projekcie.
- `gui.py` - moduł odpowiedzialny za wyświetlanie GUI.
- `board.py` - odpowiada za logikę związaną z zarządzaniem planszą oraz rozmieszczaniem statków.
- `game_logic.py` - zawiera logikę gry, w tym funkcje obsługujące tury graczy, rozpoznawanie trafień i zatopionych statków oraz logikę komputera
- `main.py` - główny moduł, który uruchamia grę, zarządza stanem aplikacji i obsługuje interakcję z użytkownikiem