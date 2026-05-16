# 📚 Biblioteka (Programowanie Obiektowe)

## 📜 Opis projektu

Aplikacja konsolowa napisana w Pythonie w paradygmacie programowania obiektowego (OOP).
Program umożliwia logowanie użytkowników, wypożyczanie książek oraz obsługę próśb o przedłużenie terminu zwrotu.

Projekt rozszerza wersję strukturalną o:

* klasy i obiekty,
* dziedziczenie,
* hermetyzację,
* polimorfizm,
* metodę specjalną `__str__`.

---

## 🏗️ Struktura projektu

🗂️ `app.py` – główny plik aplikacji zawierający wszystkie klasy i logikę programu.

---

## 🧱 Wykorzystane klasy

### 📖 Book

Reprezentuje książkę w bibliotece.

Atrybuty:

* tytuł
* autor
* łączna liczba egzemplarzy
* liczba dostępnych egzemplarzy

Metody:

* `borrow()`
* `return_copy()`
* `__str__()`

---

### 👤 User

Klasa bazowa dla wszystkich użytkowników.

Atrybuty:

* login
* hasło
* rola

Metody:

* `authenticate()`

---

### 📚 Reader

Dziedziczy po `User`.

Dodatkowe atrybuty:

* lista wypożyczonych książek
* lista próśb o przedłużenie

---

### 👨‍💼 Librarian

Dziedziczy po `User`.

Umożliwia:

* przegląd wszystkich wypożyczeń,
* obsługę próśb o przedłużenie.

---

### 🏛️ Library

Przechowuje kolekcje książek i użytkowników oraz realizuje logikę biznesową.

---

## ⚙️ Funkcjonalności

### 👤 Czytelnik

* 🔐 logowanie
* 📖 przeglądanie katalogu
* 📚 wypożyczanie książek
* 👀 podgląd własnych wypożyczeń
* ⏳ wysyłanie próśb o przedłużenie
* 🚪 wylogowanie

### 👨‍💼 Bibliotekarz

* 🔐 logowanie
* 📖 przeglądanie katalogu
* 📋 podgląd wszystkich wypożyczeń
* ✅ akceptowanie lub ❌ odrzucanie próśb o przedłużenie
* 🚪 wylogowanie

---

## 🛠️ Zastosowane elementy OOP

🧬 Dziedziczenie (`Reader`, `Librarian` → `User`)
🔒 Hermetyzacja (`_password`, `_available_copies`)
🔁 Polimorfizm (`menu()` zależne od typu użytkownika)
✨ Metoda specjalna `__str__()` w klasie `Book`
🏷️ `@property` dla liczby dostępnych egzemplarzy

---

## 👥 Dane testowe

### 📚 Czytelnicy

| Login | Hasło |
| ----- | ----- |
| jan   | 1234  |
| anna  | abcd  |
| marek | pass  |

### 👨‍💼 Bibliotekarz

| Login | Hasło |
| ----- | ----- |
| admin | admin |

---

## 📚 Przykładowe książki

* Wiedźmin
* Pan Tadeusz
* 1984
* Projekt Hail Mary
* Dune

---

## 🚀 Jak uruchomić program

```bash
python app.py
```

---

## 🎯 Przykładowy scenariusz testowy

1. Zaloguj się jako `jan / 1234`
2. Wypożycz książkę
3. Wyślij prośbę o przedłużenie
4. Wyloguj się
5. Zaloguj się jako `admin / admin`
6. Obsłuż prośbę

---

## 👤 Autor

Cyprian
