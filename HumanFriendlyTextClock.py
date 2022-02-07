class HumanFiendlyTextClock:
    pass


# Number converters
NUM_2_WORDS_DIC = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'tour', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'half'}

# connect word past or to
PAST = "past"
TO = "to"
CLOCK = "o'clock"
SPACE = " "


# Convert a number to a word in string from 1~30
def number_to_words(num):
    if num < 20 or num == 30:
        return NUM_2_WORDS_DIC[num]
    return NUM_2_WORDS_DIC[20] + SPACE + NUM_2_WORDS_DIC[num - 20]




def hello_world():
    print("Hello world")
