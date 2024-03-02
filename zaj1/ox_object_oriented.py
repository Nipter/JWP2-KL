class Board:
    ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
    X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

    def __init__(self):
        self.__board = {}

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board
        """Tworzy nową, pustą planszę gry w kółko i krzyżyk."""
        # Wszystkie pola na początku są puste.
        for space in self.ALL_SPACES:
            self.__board[space] = self.BLANK

    def get_board_str(self):
        """Zwraca tekstową reprezentację planszy."""
        return f'''
                {self.__board['1']}|{self.__board['2']}|{self.__board['3']} 1 2 3 
                -+-+- 
                {self.__board['4']}|{self.__board['5']}|{self.__board['6']} 4 5 6 
                -+-+- 
                {self.__board['7']}|{self.__board['8']}|{self.__board['9']} 7 8 9'''

    def is_valid_space(self, space):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if space is None:
            return False
        return space in self.ALL_SPACES or self.__board[space] == self.BLANK

    def is_winner(self, player):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.__board, player  # Krótsze nazwy jako "składniowy cukier".
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or  # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or  # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or  # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or  # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or  # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or  # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or  # przekątna 1
                (b['1'] == b['5'] == b['9'] == p))  # przekątna 2

    def is_board_full(self):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in self.ALL_SPACES:
            if self.__board[space] == self.BLANK:
                return False  # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True  # Nie ma wolnych pól, zatem zwróć True.

    def update_board(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.__board[space] = mark


def main():
    """Rozgrywka w kółko i krzyżyk."""
    print('Witaj w grze kółko i krzyżyk!')
    board = Board()
    current_player, next_player = board.X, board.O  # X wykonuje ruch jako pierwszy, O jako następny.
    while True:
        print(board.get_board_str())  # Wyświetl planszę na ekranie.

        # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
        move = None
        while not board.is_valid_space(move):
            print(f'Jaki jest ruch gracza {current_player}? (1-9)')
            move = input()
        board.update_board(move, current_player)  # Wykonanie ruchu.
        # Sprawdzenie, czy gra jest zakończona:
        if board.is_winner(current_player):  # Sprawdzenie, kto wygrał.
            print(board.get_board_str())
            print(current_player + ' wygrał grę!')
            break
        elif board.is_board_full():  # Sprawdzenie remisu.
            print(board.get_board_str())
            print('Gra zakończyła się remisem!')
            break
        current_player, next_player = next_player, current_player  # Zmiana gracza.
    print('Dziękuję za grę!')


if __name__ == '__main__':
    main()  # Wywołaj main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.
