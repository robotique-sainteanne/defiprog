### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_4 import part_4

def test_from_problem_description():
    assert part_4(2,[' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 5 0 0 6 0 0 0 0 0']) == [
                    [' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 4 0 0 5 0 0 0 0 0',
                     ' 4-4 4 5-5 5 0 0 0 0'],
                    [' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 3 0 0 4 0 0 0 0 0',
                     ' 3-3 3 4-4 4 0 0 0 0',
                     '-3 3 1-1 4-4 4 0 0 0']]
    
def test_2():
    assert part_4(2,[' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 9 0 0',
                     ' 0 0 0 0 0 0 0 7 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0']) == [
                    [' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 8 0 0',
                     ' 0 0 0 0 0 0 8-2 8 0',
                     ' 0 0 0 0 0 0 6 2 6 0',
                     ' 0 0 0 0 0 0 0 6 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0'],
                    [' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0',
                     ' 0 0 0 0 0 0 0 7 0 0',
                     ' 0 0 0 0 0 0 7-2 7 0',
                     ' 0 0 0 0 0 7-2 2-2 7',
                     ' 0 0 0 0 0 5 2-2 2 5',
                     ' 0 0 0 0 0 0 5 2 5 0',
                     ' 0 0 0 0 0 0 0 5 0 0',
                     ' 0 0 0 0 0 0 0 0 0 0']]
