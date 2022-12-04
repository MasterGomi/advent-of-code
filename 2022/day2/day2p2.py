ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"
PLAYER_ROCK = 1
PLAYER_PAPER = 2
PLAYER_SCISSORS = 3
LOSE = "X"
DRAW = "Y"
WIN = "Z"

SCORE_TABLE = { 
    WIN: 6,
    DRAW: 3,
    LOSE: 0
}

DESIRED_OUTCOME_TABLE = {
    (ENEMY_ROCK, DRAW): PLAYER_ROCK,
    (ENEMY_ROCK, WIN): PLAYER_PAPER,
    (ENEMY_ROCK, LOSE): PLAYER_SCISSORS,
    (ENEMY_PAPER, LOSE): PLAYER_ROCK,
    (ENEMY_PAPER, DRAW): PLAYER_PAPER,
    (ENEMY_PAPER, WIN):PLAYER_SCISSORS,
    (ENEMY_SCISSORS, WIN): PLAYER_ROCK,
    (ENEMY_SCISSORS, LOSE): PLAYER_PAPER,
    (ENEMY_SCISSORS, DRAW): PLAYER_SCISSORS
}

f = open(r"C:\Code\advent\2022\day2\day2input.txt")

total = 0

for line in f:
    enemy_choice = line[0]
    desired_outcome = line[2]

    total += DESIRED_OUTCOME_TABLE[(enemy_choice, desired_outcome)] + SCORE_TABLE[desired_outcome]

print("Done. Total score: " + str(total))