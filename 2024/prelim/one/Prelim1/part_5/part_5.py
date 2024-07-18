# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""

### Don't forget to write your own tests with pytest ###
### Noubliez pas d'aller écrire vos propres tests ave pytest ###
def part_5(text: str):
    """
    Print the 5 given words in an interesting format.

    Parameters:
        text (str): The input string containing 5 words.

    Returns:
        what you want.
    """
    ### You code goes here ###
    ### Votre code va ici ###
    # Code makes a diagram-style representation of the length of the words in a string of 5 words
    result = ''

    # Exclude ending punctuation
    while text.endswith('!') or text.endswith('?') or text.endswith('.') or text.endswith(':') or text.endswith(';') or text.endswith(',') or text.endswith(')') or text.endswith(']') or text.endswith('}'):
        text = text[:-1]

    words = text.split(' ') # Turn the text into an array of words
    words.sort(key=len) # Sort the words by length
    longestWord = len(max(words, key=len)) # Get the length of the longest word

    # Make every word the same length by adding spaces
    for i in range(len(words)):
        words[i] = words[i] + ' ' * (longestWord - len(words[i]))

    # Reverse every word so they print from top to bottom
    for i in range(len(words)):
        words[i] = words[i][::-1] 

    # Print the words in a diagram-style format
    for i in range(longestWord + 1):
        for j in range(len(words)):
            if len(words[j]) >= longestWord and len(words[j]) > i:
                result += words[j][i] + ' '
            else:
                result += ' '
        longestWord -= 1
        result += '\n'

    return result


# You can make you own test with simple print but you will need to make pytest to have all the points
# Vous pouvez faire des tests avec print simple mais il faut utiliser pytest pour avoir tous les points

print(part_5("this is like a diagram!")) 
# # Expected output: ???

