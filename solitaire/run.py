#!/usr/bin/python3

import os

import board

def main():
    """Main runner for the program"""
    game_board = board.Board()
    print(game_board.as_string())

if __name__ == "__main__":
    main()
