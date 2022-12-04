ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"
PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"

SCORE_TABLE = {
    PLAYER_ROCK: 1,
    PLAYER_PAPER: 2,
    PLAYER_SCISSORS: 3
}

WINNING_TABLE = {
    (ENEMY_ROCK, PLAYER_ROCK): 3,
    (ENEMY_ROCK, PLAYER_PAPER): 6,
    (ENEMY_ROCK, PLAYER_SCISSORS): 0,
    (ENEMY_PAPER, PLAYER_ROCK): 0,
    (ENEMY_PAPER, PLAYER_PAPER): 3,
    (ENEMY_PAPER, PLAYER_SCISSORS): 6,
    (ENEMY_SCISSORS, PLAYER_ROCK): 6,
    (ENEMY_SCISSORS, PLAYER_PAPER): 0,
    (ENEMY_SCISSORS, PLAYER_SCISSORS): 3
}

f = open(r"C:\Code\advent\2022\day2\day2input.txt")

total = 0

for line in f:
    enemy_choice = line[0]
    player_choice = line[2]

    total += WINNING_TABLE[(enemy_choice, player_choice)] + SCORE_TABLE[player_choice]

print("Done. Total score: " + str(total))