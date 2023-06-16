
ALLOWED_COLORS = ['purple', 'pink', 'red', 'blue', 'yellow', 'green', 'white', 'brown']
ALLOWED_CODE_LENGTH = 4

COLOR_NOT_ALLOWED = "Color not allowed"
COLOR_NOT_REPEAT = "Colors are not allowed to repeat"
BAD_CODE_GUESS_LENGTH = "Code or Guess length is incorrect"

def evaluate(code, guess):
    well_placed = 0
    missplaced = 0

    if len(code) != ALLOWED_CODE_LENGTH or len(guess) != ALLOWED_CODE_LENGTH:
        raise Exception(BAD_CODE_GUESS_LENGTH)
    
    seen_code_colors = dict()
    seen_guess_colors = dict()

    for (a, b) in zip(code, guess):
        if a not in ALLOWED_COLORS or b not in ALLOWED_COLORS:
            raise Exception(COLOR_NOT_ALLOWED)
        
        if a in seen_code_colors or b in seen_guess_colors:
            raise Exception(COLOR_NOT_REPEAT)

        if (a == b):
            well_placed+=1
        elif b in code:
            missplaced+=1
        
        seen_code_colors[a] = True
        seen_guess_colors[b] = True

    return [well_placed, missplaced]