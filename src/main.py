from string import Template


def get_results(division: list[dict], n: int) -> str:
    # Your code here

    # If n is larger than half the size of the list, then return None.
    # This is to prevent teams appearing in both categories
    max_n = len(division) // 2
    if n > max_n:
        raise Exception(
            f"{n}, is too big. Enter a number that is a maximum of, {max_n}"
            )
    elif n < 1:
        raise Exception(
            f"{n}, is too small. Enter a number that is 1 or greater"
            )

    # check if too many scores are equal
    avg_points = sum([team["points"] for team in division]) / len(division)
    all_teams_equal_scores = avg_points == division[0]["points"]

    if all_teams_equal_scores:
        raise Exception(
            "All teams have the same score. \
Cannot promote or relegate any teams."
            )

    # Sort teams in descending order according to their points.
    sorted_teams = sorted(division, key=lambda t: t["points"], reverse=True)
    top_teams = sorted_teams[:n]
    last_teams = sorted_teams[-n:]
    top = top_teams[0]["points"]
    last = last_teams[-1]["points"]
    top_n_equal_scores = [t for t in sorted_teams if t["points"] == top]
    last_n_equal_scores = [t for t in sorted_teams if t["points"] == last]

    if max_n < len(top_n_equal_scores):
        raise Exception(
            "Too many teams in the top \
with the same score to promote"
            )

    if max_n < len(last_n_equal_scores):
        raise Exception(
            "Too many teams in the bottom \
with the same score to relegate"
            )

    # promote list gets joined and converted to a string with the first n teams
    promote = "\n".join([team["name"] for team in top_teams])

    # relegate list gets joined and converted to a string with the last n teams
    relegate = "\n".join([team["name"] for team in last_teams])

    results_msg = Template("""Promote:
$promote

Relegate:
$relegate""").substitute({
        "promote": promote,
        "relegate": relegate
    })

    return results_msg
