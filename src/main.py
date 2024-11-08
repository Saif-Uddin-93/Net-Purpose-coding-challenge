def get_results(division: list[dict], n: int) -> str | None:
    # Your code here

    # If n is larger than half the size of the list, then return None.
    # This is to prevent teams appearing in both categories
    max_n = len(division) // 2
    if n * 2 > len(division):
        print(f"{n}, is too big. Enter a number that is a maximum of, {max_n}")
        return
    elif n<1:
        print(f"{n}, is too small. Enter a number that is 1 or greater")
        return

    # Sort teams in descending order according to their points.
    sorted_teams = sorted(division, key=lambda t: t["points"], reverse=True)
    # promote list gets the first n teams
    promote = [team["name"] for team in sorted_teams[:n]]
    # relegate list gets the last n teams
    relegate = [team["name"] for team in sorted_teams[-n:]]

    return "Promote:\n" + "\n".join(promote) + "\n\nRelegate:\n" + \
        "\n".join(relegate)
