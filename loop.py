teams = []
def get_teams(*args, **kwargs):
    for country in (kwargs):
        for n in range(1, 5):
            generated_teams = (f'{country}{n}')
            teams.append(generated_teams)
print(teams)


get_teams("eng", "spa", "ita", "fra", "port", "germ", "swis", "bel", "turk", "dutch", 'rus', "pol", "scot", "grec")
