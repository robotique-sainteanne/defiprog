# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 2.
Ceci est le fichier template pour la partie 5 du Prelim 2.
"""

def part_5(p: str, q: str, e: str, M: str) -> (int, int):
    """
    Find the C and d number in RSA encryption.

    Parameters:
        p (str): The first prime.
        q (str): The second prime.
        e (str): The exponent.
        M (str): The message to encode.

    Returns:
        (int, int) : A tuple containing the C and d from RSA encryption 
    """
    C = 0
    d = 0
    ### You code goes here ###
    ### Votre code va ici ###
    
    C = (int(M)**int(e)) % (int(p) * int(q))

    phiofn = (int(p) - 1) * (int(q) - 1)
    u = 0
    v = 0


    # Use the function to calculate d
    d = mod_inverse(int(e), phiofn)


    return (C, d)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(e, totary):
    gcd, x, _ = extended_gcd(e, totary)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % totary


    

# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

print(part_5('0023', '8111', '1579', '0330')) # Expected: (168442, 127459)
print(part_5('3617', '4567', '3517', '8400')) # Expected: (13038683, 8379733)
print(part_5('5051', '5557', '3833', '0707')) # Expected: (26895292, 16016297)

