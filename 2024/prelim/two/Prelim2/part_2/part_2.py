# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 2.
Ceci est le fichier template pour la partie 2 du Prelim 2.
"""

def part_2(equation: str) -> str:
    """
    Lunar arithmetic

    Parameters:
        equation (str): The equation to solve with lunar arithmetic.

    Returns:
        str: The result of the equation.
    """
    result = 0
    ### You code goes here ###
    ### Votre code va ici ###
    is_add = False
    is_mult = False
    res = ''
    numlist = []

    # Determine what the operation is 
    if '+' in equation:
        is_add = True
    elif '*' in equation:
        is_mult = True

    # Determine the two numbers in the equation
    if is_mult == True:
        numlist.append(equation[0:equation.index('*')])
        numlist.append(equation[equation.index('*')+1:])
    elif is_add == True:
        numlist.append(equation[0:equation.index('+')])
        numlist.append(equation[equation.index('+')+1:])

    # Find the maximum length of the two numbers
    biggest_num = str(max(int(numlist[i]) for i in range(len(numlist))))
    smallest_num = str(min(int(numlist[i]) for i in range(len(numlist))))

    if is_add:
        res = perform_lunar_addition(numlist, biggest_num, smallest_num)
    else:
        res = perform_lunar_multiplication(numlist, biggest_num, smallest_num)

    result = int(res)

    return str(result)


def perform_lunar_addition(numbers, biggest_num, smallest_num):
    res = ''
    
    if len(biggest_num) == 1:
        return max(numbers)
    
    smallest_num = ('0' * (len(biggest_num) - len(smallest_num))) + smallest_num
    
    for i in range(len(biggest_num) - 1, -1, -1):
        res = str(max(biggest_num[i], smallest_num[i])) + res

    return int(res)

def perform_lunar_multiplication(numbers, biggest_num, smallest_num):
    if len(biggest_num) == 1:
        return min(numbers)

    addition_terms = []
    for i in range(len(smallest_num)):
        addition_terms.append('')

    for k in range(len(smallest_num) - 1, -1, -1):
        for j in range(len(biggest_num) - 1, -1, -1):
            addition_terms[k] = str(min([smallest_num[k], biggest_num[j]])) + addition_terms[k]

    addition_terms[0] = addition_terms[0] + '0'

    

    return perform_lunar_addition(addition_terms, str(max(int(addition_terms[i]) for i in range(len(addition_terms)))), str(min(int(addition_terms[i]) for i in range(len(addition_terms)))))

# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

# print(part_2('811*81')) # Expected: '8111'
# print(part_2('345+4567')) # Expected: '4567'
print(part_2('557*57')) # Expected: '4'


