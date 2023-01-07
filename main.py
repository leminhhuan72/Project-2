from game import game
import sys


if __name__ == "__main__":
    g = game('MAP_GEN/MAP_NOISE/MAP32.txt', 'LOG32.txt')
    g.run_game()
