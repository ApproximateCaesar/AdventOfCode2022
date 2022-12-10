# https://adventofcode.com/2022/day/2

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day2_rock_paper_scissors/day2_input.txt") as f:
    input_txt = f.read().split()

# Split into two columns
strategy_guide = []
i = 0
while i < len(input_txt):
    game = [input_txt[i], input_txt[i + 1]]
    strategy_guide.append(game)
    i += 2


# get total score over all games
def get_total_score(strategy_guide):
    total_score = 0
    for game in strategy_guide:
        if game[0] == 'A':
            if game[1] == 'X':
                total_score += 1 + 3
            if game[1] == 'Y':
                total_score += 2 + 6
            if game[1] == 'Z':
                total_score += 3 + 0
        if game[0] == 'B':
            if game[1] == 'X':
                total_score += 1 + 0
            if game[1] == 'Y':
                total_score += 2 + 3
            if game[1] == 'Z':
                total_score += 3 + 6
        if game[0] == 'C':
            if game[1] == 'X':
                total_score += 1 + 6
            if game[1] == 'Y':
                total_score += 2 + 0
            if game[1] == 'Z':
                total_score += 3 + 3
    return total_score


# get total score over all games
def get_total_score_decrypted(strategy_guide):
    total_score = 0
    for game in strategy_guide:
        if game[0] == 'A':
            if game[1] == 'X':
                total_score += 0 + 3
            if game[1] == 'Y':
                total_score += 3 + 1
            if game[1] == 'Z':
                total_score += 6 + 2
        if game[0] == 'B':
            if game[1] == 'X':
                total_score += 0 + 1
            if game[1] == 'Y':
                total_score += 3 + 2
            if game[1] == 'Z':
                total_score += 6 + 3
        if game[0] == 'C':
            if game[1] == 'X':
                total_score += 0 + 2
            if game[1] == 'Y':
                total_score += 3 + 3
            if game[1] == 'Z':
                total_score += 6 + 1
    return total_score


print(f"The total score for using the encrypted strategy is {get_total_score(strategy_guide)}")
print(f"The total score for using the decrypted strategy is {get_total_score_decrypted(strategy_guide)}")
