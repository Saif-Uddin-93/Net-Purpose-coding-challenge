from string import Template


def get_results(division: list[dict], n: int) -> str | None:
    # Your code here

    # If n is larger than half the size of the list, then return None.
    # This is to prevent teams appearing in both categories
    max_n = len(division) // 2
    if n > max_n:
        print(f"{n}, is too big. Enter a number that is a maximum of, {max_n}")
        return
    elif n < 1:
        print(f"{n}, is too small. Enter a number that is 1 or greater")
        return

    # Sort teams in descending order according to their points.
    sorted_teams = sorted(division, key=lambda t: t["points"], reverse=True)
    # promote list gets joined and converted to a string with the first n teams
    promote = "\n".join([team["name"] for team in sorted_teams[:n]])
    # relegate list gets joined and converted to a string with the last n teams
    relegate = "\n".join([team["name"] for team in sorted_teams[-n:]])

    results_msg = Template("""Promote:
$promote

Relegate:
$relegate""").substitute({
        "promote": promote,
        "relegate": relegate
    })

    return results_msg

    # return "Promote:\n" + promote + "\n\nRelegate:\n" + relegate
