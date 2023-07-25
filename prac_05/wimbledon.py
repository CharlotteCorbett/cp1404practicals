"""
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


"""
def main():
    FILE = "wimbledon.csv"
    results = load_files(FILE)
    process_results()
    display_results()


def load_files(FILE):
    results = []
    with open(FILE, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            stats = line.strip().split(',')
            results.append(stats)
        del results[0]
    return results


def process_results():
    countries = set()

    pass


def display_results():
    pass

main()
