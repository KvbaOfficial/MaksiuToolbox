# Maksiu Toolbox 737-800

Maksiu Toolbox 737-800 to aplikacja GUI napisana w Pythonie przy użyciu biblioteki `tkinter`. Aplikacja jest przeznaczona dla wirtualnych pilotów, oferując narzędzia do zarządzania lotniskami, sprawdzania pogody (METAR), oraz dostęp do zasobów online.

## Funkcjonalności

### Menu

- **Plik**:

  - **Ustaw lotniska**: Umożliwia użytkownikowi wprowadzenie kodów ICAO lotnisk wylotu i przylotu.
  - **Zapisz ustawienia**: Zapisuje ustawienia lotnisk do pliku `settings.json`.
  - **Wczytaj ustawienia**: Wczytuje ustawienia lotnisk z pliku `settings.json`.
  - **Wyjdź**: Zamyka aplikację.

- **Pomoc**:
  - **O programie**: Wyświetla informacje o programie.

### Główne funkcje

- **Ustaw lotniska**: Umożliwia użytkownikowi wprowadzenie kodów ICAO lotnisk wylotu i przylotu.
- **Pokaż METAR**: Wyświetla aktualne dane METAR dla ustawionych lotnisk.
- **Otwórz ChartFox**: Otwiera stronę ChartFox dla lotniska wylotu.
- **Otwórz SimBrief**: Otwiera stronę SimBrief.
- **Wyświetl checklistę**: Otwiera checklistę dla Boeinga 737-800.
- **Wyjdź**: Zamyka aplikację.

### Stylizacja

- Ustawienia stylów dla przycisków, ramek i tła.

### Status bar

- Wyświetla aktualny status aplikacji (np. "Gotowy", "Ustawienia zapisane").

### Zarządzanie ustawieniami

- **Zapisz ustawienia**: Zapisuje ustawienia lotnisk do pliku `settings.json`.
- **Wczytaj ustawienia**: Wczytuje ustawienia lotnisk z pliku `settings.json`.

### Sprawdzanie statusu API

- Sprawdza połączenie z API AVWX i aktualizuje status w pasku statusu.
