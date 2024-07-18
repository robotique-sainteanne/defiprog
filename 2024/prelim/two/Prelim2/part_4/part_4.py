# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 2.
Ceci est le fichier template pour la partie 4 du Prelim 2.
"""

def part_4(base: int, number: int) -> str:
    """
    Base shifting into modular arithmetic

    Parameters:
        base (int): The base to which you convert.
        number (int): The number to convert

    Returns:
        int: Final 4-digits code
    """
    code = 0
    ### You code goes here ###
    ### Votre code va ici ###
   
    def ConvertToBase(n, base):
        digits = []
        while n > 0:
            digits.insert(0, n % base)
            n //= base
        return digits


    for _ in range(5):
        digits = ConvertToBase(number, base)
        number = int(''.join(map(str, digits)))
    groups = [[] for _ in range(4)]
    
    for digit in str(number):
        groups[int(digit) % 4].append(int(digit))
        
    group_sums = [sum(group) for group in groups]
    reduced_sums = [sum(int(digit) for digit in str(sum_digits)) for sum_digits in group_sums]
    key = ''.join(map(str, reduced_sums))
    code = key.zfill(4)
    return code
    


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

# print(part_4(29, 982)) # Expected: '0330'
# print(part_4(23, 1053)) # Expected: '8400'
# print(part_4(65, 812)) # Expected: '0707'
# print(part_4(23, 19209384857203)) # Expected: 9887
