#book class

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self._available_copies = total_copies  # hermetyzacja

    @property
    def available_copies(self):
        return self._available_copies

    def borrow(self):
        if self._available_copies > 0:
            self._available_copies -= 1
            return True
        return False

    def return_copy(self):
        if self._available_copies < self.total_copies:
            self._available_copies += 1

    def __str__(self):
        return (
            f"{self.title} - {self.author} "
            f"(dostępne: {self._available_copies}/{self.total_copies})"
        )


#user class

class User:
    def __init__(self, login, password, role):
        self.login = login
        self._password = password  # hermetyzacja
        self.role = role

    def authenticate(self, password):
        return self._password == password


#czytelnik

class Reader(User):
    def __init__(self, login, password):
        super().__init__(login, password, "czytelnik")
        self.borrowed_books = []
        self.extension_requests = []

    def menu(self):
        print("\n===== MENU CZYTELNIKA =====")
        print("1. Przeglądaj katalog")
        print("2. Wypożycz książkę")
        print("3. Moje wypożyczenia")
        print("4. Poproś o przedłużenie")
        print("5. Wyloguj")


#pracownik

class Librarian(User):
    def __init__(self, login, password):
        super().__init__(login, password, "bibliotekarz")

    def menu(self):
        print("\n===== MENU BIBLIOTEKARZA =====")
        print("1. Przeglądaj katalog")
        print("2. Lista wszystkich wypożyczeń")
        print("3. Obsłuż prośby o przedłużenie")
        print("4. Wyloguj")


#biblio

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.extension_queue = []  # (reader, book)

    # Books

    def add_book(self, book):
        self.books.append(book)

    def show_catalog(self):
        print("\n===== KATALOG =====")
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    # Users

    def add_user(self, user):
        self.users.append(user)

    def login(self):
        attempts = 0

        while attempts < 3:
            login = input("Login: ")
            password = input("Hasło: ")

            for user in self.users:
                if user.login == login and user.authenticate(password):
                    print("Zalogowano pomyślnie!")
                    return user

            attempts += 1
            print(f"Błędne dane! Próba {attempts}/3")

        print("Przekroczono limit prób.")
        return None

    # Rents

    def borrow_book(self, reader):
        title = input("Podaj tytuł książki: ")
        book = self.find_book(title)

        if not book:
            print("Nie znaleziono książki.")
            return

        if book.borrow():
            reader.borrowed_books.append(book)
            print("Książka została wypożyczona.")
        else:
            print("Brak dostępnych egzemplarzy.")

    def show_reader_borrowed(self, reader):
        print("\n===== MOJE WYPOŻYCZENIA =====")

        if not reader.borrowed_books:
            print("Brak wypożyczonych książek.")
            return

        for book in reader.borrowed_books:
            print(book.title)

    # List

    def show_all_borrowings(self):
        print("\n===== WSZYSTKIE WYPOŻYCZENIA =====")
        found = False

        for user in self.users:
            if isinstance(user, Reader):
                for book in user.borrowed_books:
                    print(f"{user.login} -> {book.title}")
                    found = True

        if not found:
            print("Brak aktywnych wypożyczeń.")



    def request_extension(self, reader):
        if not reader.borrowed_books:
            print("Nie masz wypożyczonych książek.")
            return

        print("\nWypożyczone książki:")
        for i, book in enumerate(reader.borrowed_books, start=1):
            print(f"{i}. {book.title}")

        try:
            choice = int(input("Wybierz numer książki: "))
            if 1 <= choice <= len(reader.borrowed_books):
                book = reader.borrowed_books[choice - 1]

                if book in reader.extension_requests:
                    print("Prośba dla tej książki została już wysłana.")
                    return

                reader.extension_requests.append(book)
                self.extension_queue.append((reader, book))
                print("Prośba o przedłużenie została wysłana.")
            else:
                print("Nieprawidłowy numer.")
        except ValueError:
            print("Podaj poprawny numer.")

    def process_extension_requests(self):
        print("\n===== PROŚBY O PRZEDŁUŻENIE =====")

        if not self.extension_queue:
            print("Brak próśb.")
            return

        while self.extension_queue:
            reader, book = self.extension_queue.pop(0)

            print(f"\nCzytelnik: {reader.login}")
            print(f"Książka: {book.title}")

            decision = input("Akceptować? (t/n): ").lower()

            if decision == "t":
                print("Prośba zaakceptowana.")
            else:
                print("Prośba odrzucona.")

            if book in reader.extension_requests:
                reader.extension_requests.remove(book)



library = Library()

library.add_book(Book("Wiedźmin", "Andrzej Sapkowski", 3))
library.add_book(Book("Pan Tadeusz", "Adam Mickiewicz", 2))
library.add_book(Book("1984", "George Orwell", 4))
library.add_book(Book("Projekt Hail Mary", "Andy Weir", 1))
library.add_book(Book("Dune", "Frank Herbert", 2))

library.add_user(Reader("jan", "1234"))
library.add_user(Reader("anna", "aaaa"))
library.add_user(Reader("Tomek", "Tomek"))

library.add_user(Librarian("admin", "admin"))


#main

def main():
    user = library.login()

    if user is None:
        return

    while True:
        user.menu()
        choice = input("Wybierz opcję: ")

        #menu
        if isinstance(user, Reader):
            if choice == "1":
                library.show_catalog()
            elif choice == "2":
                library.borrow_book(user)
            elif choice == "3":
                library.show_reader_borrowed(user)
            elif choice == "4":
                library.request_extension(user)
            elif choice == "5":
                print("Wylogowano.")
                break
            else:
                print("Nieprawidłowy wybór.")

        #menu pracownika
        elif isinstance(user, Librarian):
            if choice == "1":
                library.show_catalog()
            elif choice == "2":
                library.show_all_borrowings()
            elif choice == "3":
                library.process_extension_requests()
            elif choice == "4":
                print("Wylogowano.")
                break
            else:
                print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()