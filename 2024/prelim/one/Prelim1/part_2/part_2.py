# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 1.
Ceci est le fichier template pour la partie 2 du Prelim 1.
"""

def part_2(text: str, key: int) -> str:
    """
    Decrypts the text with Caesar cypher.

    Parameters:
        text (str): The input string.
        key  (int): The shifting key.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ''
    ### You code goes here ###
    ### Votre code va ici ###
    if key > 26 or key < -26:
        return "Invalid key. Key must be a number between -26 and 26 inclusive."

    for i in range(len(text)):
        if text[i].isalpha() and text[i] != ' ':
            if key > 0:
                if 91 > ord(text[i]) > 64 and ord(text[i]) + key > 90:
                    decrypted_text += chr((ord(text[i]) + key) - 26)
                elif 123 > ord(text[i]) > 96 and ord(text[i]) + key > 122:
                    decrypted_text += chr((ord(text[i]) + key) - 26)
                else:
                    decrypted_text += chr(ord(text[i]) + key)
            else:
                if 91 > ord(text[i]) > 64 and ord(text[i]) + key < 65:
                    decrypted_text += chr((ord(text[i]) + key) + 26)
                elif 123 > ord(text[i]) > 96 and ord(text[i]) + key < 97:
                    decrypted_text += chr((ord(text[i]) + key) + 26)
                else:
                    decrypted_text += chr(ord(text[i]) + key)
        else:
            decrypted_text += text[i]
    


    return decrypted_text


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

# print(part_2('ti kzk mab cvm kwuxmbqbqwv bzma ncv!', 28))  # Expected output: la crc est une competition tres fun!
# print(part_2('Zcfsa wdgia rczcf gwh oash, qcbgsqhshif orwdwgqwbu szwh. Qfog qifgig dzoqsfoh hcfhcf bsq toqwzwgwg. Bizzoa jsz sfoh zsc. Gigdsbrwggs bcb bwgz sbwa. Aosqsbog oq sfoh sush sfoh gcrozsg hsadig. Bizzo toqwzwgw. Dszzsbhsgeis toqwzwgwg hwbqwribh bibq, dfshwia hwbqwribh rczcf jsbsbohwg wb. Bizzoa woqizwg oqqiagob zsc bcb sttwqwhif. Aosqsbog crwc ofqi, hfwghweis.', 12))  
# Expected output: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras cursus placerat tortor nec facilisis. Nullam vel erat leo. Suspendisse non nisl enim. Maecenas ac erat eget erat sodales tempus. Nulla facilisi. Pellentesque facilisis tincidunt nunc, pretium tincidunt dolor venenatis in. Nullam iaculis accumsan leo non efficitur. Maecenas odio arcu, tristique.
# print(part_2("This text is really good as is!", 0))   # Expected output: This text is really good as is!
# print(part_2("Cb jo oiggw o fsqizcbg", -14))   # Expected output: On va aussi a reculons
