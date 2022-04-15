class Book:
    def __init__(self, writer, name):
        self.writer = writer
        self.name = name

    def __repr__(self):
        return f"{self.writer}-{self.name}"

class Library():

    def __init__(self, *books: Book):
        self.books = list(books)

    def append_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def sort_books(self, option: str, reverse: bool):
        self.books.sort(key=lambda book: getattr(book, option), reverse=reverse)

    def find_books(self, **options: any):
        books = []
        for book in self.books:
            for option, value in options.items():
                if getattr(book, option) != value:
                    break
            else:
                books.append(book)
        return books


def check_value():
    while True:
        try:
            x = int(input())
            break
        except:
            print("Введены некорректные данные ")
    return x
def base_menu():
    print("Введите 0, чтобы завершить")
    print("Введите 1, чтобы просмотреть библиотеку")
    print("Введите 2, чтобы добавить книгу")
    print("Введите 3, чтобы удалить книгу")
    print("Введите 4, чтобы найти книгу по автору или названию")
    print("Введите 5, чтобы отсортировать библиотеку по автору или по названию")


def menu():
    print("Здравствуйте,я рад видеть вас в этой библиотеке:")
    home_library = Library(Book("Пушкин", "Евгений Онегин"))
    base_menu()
    check = check_value()
    while True:
        if check==0:
            break
        else:
            if (check == 1):
                print("По вашему запросу найдено:\n")
                print(home_library.books,"\n")
                base_menu()
                check=check_value()
            else:
                if (check == 2):
                    writer = input("введите автора")
                    name = input("введите название")
                    home_library.append_book(Book(writer, name))
                    base_menu()
                    check=check_value()
                else:
                    if (check == 3):
                        rem=input("введите название книги которую хотите удалить")
                        books = home_library.find_books(name=rem)
                        for book in books:
                            home_library.remove_book(book)
                        base_menu()
                        check = check_value()
                    else:
                        if (check == 4):
                            print("введите 1, чтобы искать по автору, или 2, чтобы искать по названию")
                            found=check_value()
                            if found==1:
                                rem = input("введите автора, которого хотите найти")
                                books = home_library.find_books(writer=rem)
                                print("По вашему запросу найдено:,\n")
                                print(books,"\n")
                                base_menu()
                                check = check_value()
                            else:
                                if found==2:
                                    rem = input("введите название книги, которую хотите найти")
                                    books = home_library.find_books(name=rem)
                                    print("По вашему запросу найдено:,\n")
                                    print(books,"\n")
                                    base_menu()
                                    check = check_value()
                                else:
                                    print("Введены некорректные данные ")
                        else:
                            if (check == 5):
                                print("введите 1, чтобы сортировать по автору, или 2, чтобы сортировать по названию")
                                sort = check_value()
                                if sort == 1:
                                    home_library.sort_books("writer",False)
                                    print("По вашему запросу отсортировано:,\n")
                                    print(home_library.books,"\n")
                                    base_menu()
                                    check = check_value()
                                else:
                                    if sort == 2:
                                        home_library.sort_books("name",False)
                                        print("По вашему запросу отсортировано:\n")
                                        print(home_library.books,"\n")
                                        base_menu()
                                        check = check_value()
                                    else:
                                        print("Введены некорректные данные ")
                            else:
                                print("Введены некорректные данные ")
                                check = check_value()



def main():
    menu()

if __name__ == '__main__':
    main()