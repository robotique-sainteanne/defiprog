### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_3 import part_3

def test_from_problem_description():
    assert part_3(2,[' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 9 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0']) == [[' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 8 0 0',
                                                  ' 0 0 0 0 0 0 8-8 8 0',
                                                  ' 0 0 0 0 0 0 0 8 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0'], 

                                                 [' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 7 0 0',
                                                  ' 0 0 0 0 0 0 7-7 7 0',
                                                  ' 0 0 0 0 0 7-7 7-7 7',
                                                  ' 0 0 0 0 0 0 7-7 7 0',
                                                  ' 0 0 0 0 0 0 0 7 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0',
                                                  ' 0 0 0 0 0 0 0 0 0 0']]
 


assert part_3(2,[' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 0 0 0 0 0 0 0 0 0',
                    ' 0 5 0 0 0 0 0 0 0 0']) == [[' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 4 0 0 0 0 0 0 0 0',
' 4-4 4 0 0 0 0 0 0 0'], 

[' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 3 0 0 0 0 0 0 0 0',
' 3-3 3 0 0 0 0 0 0 0',
'-3 3-3 3 0 0 0 0 0 0']]


