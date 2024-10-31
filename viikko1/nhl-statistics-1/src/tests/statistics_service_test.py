import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_includes(self):
        player = self.stats.search("Semenko")
        self.assertEqual(str(player), str(Player("Semenko", "EDM", 4, 12)))

    def test_search_does_not_include(self):
        player = self.stats.search("Waldo")
        self.assertEqual(player, None)

    def test_team_includes_players(self):
        team = [str(player) for player in self.stats.team("EDM")]
    
        teamToBeFound = [
            str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Gretzky", "EDM", 35, 89))
        ]

        self.assertEqual(team, teamToBeFound)

    def test_top_players(self):
        top = [str(player) for player in self.stats.top(2)]

        topPlayersToBeFound = [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Lemieux", "PIT", 45, 54)),
            str(Player("Yzerman", "DET", 42, 56))
        ]

        self.assertEqual(top, topPlayersToBeFound)
        