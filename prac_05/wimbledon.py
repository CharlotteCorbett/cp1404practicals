"""
This was my initial code plan:

Pseudocode/Code plan:
load file into nested list named wimbledon stats
remove first element (descriptor)

wimbledon_stats = []
champions = set()
countries = set()
champion_to_wins = {}

# loads champions and countries into sets
for stat in wimbledon_stats:
    champions.add(stat[1])
    countries.add(stat[0])

# counts total wins for each champion
for champion in wimbledon_stats:
    try:
        champion_to_wins[champion] += 1
    except KeyError:
        champion_to_wins[champion] = 1

However, as I was implementing this code, I felt that there might be a better way to solve this task then
what I was currently doing.
Upon checking the solutions branch for this file, I found that although I was on the right track,
I was not using constants and my overall program was not neatly organised.

As such, I used the solutions as a guide to figure out where I went wrong and what I can do better.
"""
FILE = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Read data file and show details of Wimbledon countries and champions"""
    results = load_files()
    champion_to_wins, countries = process_results(results)
    show_results(champion_to_wins, countries)


def load_files():
    """Load data from file and into a nested list"""
    results = []
    with open(FILE, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            stats = line.strip().split(',')
            results.append(stats)
        del results[0]
    return results


def process_results(results):
    """Process data into set of countries and dictionary of champions"""
    champion_to_wins = {}
    countries = set()
    for result in results:
        countries.add(result[COUNTRY_INDEX])
        try:
            champion_to_wins[result[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[result[CHAMPION_INDEX]] = 1
    return champion_to_wins, countries



def show_results(champion_to_wins, countries):
    """Show countries and champions"""
    print("Wimbledon Champions: ")
    for champion, wins, in champion_to_wins.items():
        print(champion, wins)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
