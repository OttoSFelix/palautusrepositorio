import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_top3(self):
        top3 = self.stats.top(2)
        lista = []
        for t in top3:
            lista.append(str(t))

        self.assertEqual(lista, ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98'])

    def test_top_goals(self):
        top3 = self.stats.top(2, SortBy.GOALS)
        lista = []
        for t in top3:
            lista.append(str(t))

        self.assertEqual(lista, ['Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98', 'Kurri EDM 37 + 53 = 90'])

    def test_top_assists(self):
        top3 = self.stats.top(2, SortBy.ASSISTS)
        lista = []
        for t in top3:
            lista.append(str(t))

        self.assertEqual(lista, ['Gretzky EDM 35 + 89 = 124', 'Yzerman DET 42 + 56 = 98', 'Lemieux PIT 45 + 54 = 99'])

    def test_search_player(self):
        search = str(self.stats.search('Ku'))

        self.assertEqual(search, 'Kurri EDM 37 + 53 = 90')

    def test_search_none(self):
        search = self.stats.search('lkjh')

        self.assertEqual(search, None)

    def test_team(self):
        team = self.stats.team('PIT')

        self.assertEqual(str(team[0]), 'Lemieux PIT 45 + 54 = 99')


    
