### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_1 import part_1

def test_from_problem_description():
    assert part_1(number = 4) == [' 4', ' 3-3 3', ' 2-2 2-2 2', ' 1-1 1-1 1-1 1', ' 0 0 0 0 0 0 0 0 0']
    assert part_1(number = 9) == [' 9', ' 8-8 8', ' 7-7 7-7 7', ' 6-6 6-6 6-6 6', ' 5-5 5-5 5-5 5-5 5', ' 4-4 4-4 4-4 4-4 4-4 4', ' 3-3 3-3 3-3 3-3 3-3 3-3 3', ' 2-2 2-2 2-2 2-2 2-2 2-2 2-2 2', ' 1-1 1-1 1-1 1-1 1-1 1-1 1-1 1-1 1', ' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0']
    assert part_1(number = 1) == [' 1', ' 0 0 0']
    

def test_with_2_groups():
    assert part_1(number=2) == [' 2', ' 1-1 1', ' 0 0 0 0 0']

def test_with_4_groups():
    assert part_1(number=7) == [' 7', ' 6-6 6', ' 5-5 5-5 5', ' 4-4 4-4 4-4 4', ' 3-3 3-3 3-3 3-3 3', ' 2-2 2-2 2-2 2-2 2-2 2', ' 1-1 1-1 1-1 1-1 1-1 1-1 1', ' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0']
    assert part_1(number=8) == [' 8', ' 7-7 7', ' 6-6 6-6 6', ' 5-5 5-5 5-5 5', ' 4-4 4-4 4-4 4-4 4', ' 3-3 3-3 3-3 3-3 3-3 3', ' 2-2 2-2 2-2 2-2 2-2 2-2 2', ' 1-1 1-1 1-1 1-1 1-1 1-1 1-1 1', ' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0']
