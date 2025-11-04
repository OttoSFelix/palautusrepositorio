from rich.console import Console
from rich.table import Table
from rich import print 
from player import PlayerReader, PlayerStats

BASE_URL = "https://studies.cs.helsinki.fi/nhlstats"
SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22",
    "2022-23", "2023-24", "2024-25", "2025-26"
]
NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR",
    "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"
]

def main():
    console = Console()
    selected_season = "2024-25"
    stats = None
    season_prompt = f"[{'/'.join(SEASONS)}] "
    console.print('Season ', end="")
    console.print(f'{season_prompt}', end="")
    console.print(f'[bold]({selected_season}):[/bold]', end="")
    season_input = input()

    if season_input:
        selected_season = season_input
        
    url = f"{BASE_URL}/{selected_season}/players"
        
    reader = PlayerReader(url)
    stats = PlayerStats(reader)


    while True:
        nat_prompt = f"[{'/'.join(NATIONALITIES)}] "
        console.print('Nationality ', end="")
        console.print(f'{nat_prompt}',style='magenta', end="")
        console.print('[bold]():[/bold]', end="")
        nat_input = input().upper()
        if not nat_input:
            console.print("\nExiting.")
            break
        
        
        players = stats.top_scorers_by_nationality(nat_input)

        table = Table(title=f"Season {selected_season} players from {nat_input}", show_header=True, header_style="bold white")
        table.add_column("Player", style="cyan", no_wrap=True)
        table.add_column("Team", style="purple")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.total())
            )
        
        console.print(table)
        console.print()

if __name__ == '__main__':
    main()