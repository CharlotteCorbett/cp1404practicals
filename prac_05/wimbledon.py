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
    wimbledon_stats = load_files()


def load_files():
    infile = "wimbledon.csv"
    wimbledon_stats = []
    with open(infile, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            stats = line.strip().split(',')
            wimbledon_stats.append(stats)
        del wimbledon_stats[0]
    return wimbledon_stats

main()
