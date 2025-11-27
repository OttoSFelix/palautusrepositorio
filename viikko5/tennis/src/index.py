from tennis_game import TennisGame


def main():
    game = TennisGame("p1", "p2")

    while True:
        point = input('Point won by:')
        game.won_point(point)
        print(game.get_score())


if __name__ == "__main__":
    main()
