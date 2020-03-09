class PhoneBook:

    def __init__(self):
        self.book = [None] * 10000000

    def add(self, number, name):
        """Adds a person with name and phone number to the phone book.
        If there exists a user with such number already, then manager overwrites
        the corresponding name.
        """
        self.book[number] = name

    def delete(self, number):
        """Erases a person with number from the phone book.
        If there is no such person, then the query is ignored.
        """
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        """Looks for a person with phone number.
        Replies with the person's name, or with string “not found”
        (without quotes) if there is no such person in the book.
        """
        if self.book[number] is None:
            return "not found"
        return self.book[number]


def process_queries(queries):
    """Helper function which reads queries from standard input,
    runs phonebook manager and sends the results to standard output.
    """
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)


if __name__ == "__main__":
    phonebook = PhoneBook()

    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)