"""
    # Correct Sentence

    ## For the input of your function, you will be given one sentence. 
    ## You have to return a corrected version, that starts with a capital letter
    ## and ends with a period (dot).
   
    ## Pay attention to the fact that not all of the fixes are necessary.
    ## If a sentence already ends with a period (dot), then adding another one will be a mistake.

    - Input: A string.
    - Output: A string.

    >> EXAMPLE:
       
        correct_sentence("greetings, friends") == "Greetings, friends."
        correct_sentence("Greetings, friends") == "Greetings, friends."
        correct_sentence("Greetings, friends.") == "Greetings, friends."
    
    <<
"""


def correct_sentence(text: str) -> str:
    if text[-1] != '.':
        text += '.'
        return text[0].upper() + text[1:]
    else:
        return text[0].upper() + text[1:]


# These "asserts" are used for self-checking and not for an auto-testing
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("hi") == "Hi."
assert correct_sentence("welcome to New York") == "Welcome to New York."
