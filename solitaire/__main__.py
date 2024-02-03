from solitaire.board import Board

def main():
    """Main runner for the program"""
    game_board = Board()
    print(game_board)
    print(game_board.get_moves())

if __name__ == "__main__":
    main()
