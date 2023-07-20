def main():
    MINIMUM_PICK = 1
    MAXIMUM_PICK = 45
    quick_picks = []
    number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_of_quick_picks, MINIMUM_PICK, MAXIMUM_PICK, quick_picks)
    print_quick_picks(quick_picks)


def generate_quick_picks(number_of_quick_picks, MINIMUM_PICK, MAXIMUM_PICK, quick_picks):
    from random import randint
    for pick in range(number_of_quick_picks):
        picks = []
        # make each 'quick pick' (list of 6 random numbers)
        for random_number in range(7):
            random_pick = randint(MINIMUM_PICK, MAXIMUM_PICK)
            if random_pick in picks:
                new_random_pick = randint(MINIMUM_PICK, MAXIMUM_PICK)
                picks.append(new_random_pick)
            else:
                picks.append(random_pick)
        quick_picks.append(picks)
    return  quick_picks


def print_quick_picks(quick_picks):
    for quick_pick in quick_picks:
        print(f"{quick_pick[0]:>2} {quick_pick[1]:>2} {quick_pick[2]:>2} {quick_pick[3]:>2} {quick_pick[4]:>2} {quick_pick[5]:>2}")


main()