from game import game
import logging
import sys


if __name__ == "__main__":
    game = game('MAP_GEN/MAP32.txt', 'LOG/LOG32.txt')

    game.run_game()
