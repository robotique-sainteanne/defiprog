### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_1 import part_1

def test_from_problem_description():
    assert part_1([(3,2), (5,3), (7,2)]) == '0023'
    assert part_1([(21, 5), (2, 1), (19, 7), (5, 2)]) == '3617'
    assert part_1([(7,4), (11,2), (23,14), (3,2)]) == '5051'
    

def test_with_2_groups():
    assert part_1([(3,1), (7, 5)]) == '0019'

def test_with_4_groups():
    assert part_1([(7,4), (11,1), (23,15), (3,2)]) == '0452'
    assert part_1([(7,4), (11,1), (23,15), (3,1)]) == '3994'
