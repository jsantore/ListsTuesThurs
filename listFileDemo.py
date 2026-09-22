games_file = open("games.txt", "r", encoding="utf-8")
games_data = games_file.readlines()
for line in games_data:
    this_game= line.split("|")
    print(this_game[0])