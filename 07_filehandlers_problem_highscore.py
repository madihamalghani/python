import random

def game():
    print('You are playing the game...')
    score = random.randint(1, 62)  # Random score between 1 and 62

    # Fetch the high score from the file
    try:
        with open("Highscore.txt", "r") as f:
            highscore = f.read().strip()  # Read and remove any extra whitespace
            highscore = int(highscore) if highscore else 0  # Convert to int, default to 0 if empty
    except FileNotFoundError:
        # If file doesn't exist, initialize highscore as 0
        highscore = 0

    print(f'Your score: {score}')
    print(f'Current high score: {highscore}')

    # Update high score if the current score is higher
    if score > highscore:
        print("New high score achieved!")
        with open("Highscore.txt", "w") as f:
            f.write(str(score))  # Write the new high score

    return score

game()
