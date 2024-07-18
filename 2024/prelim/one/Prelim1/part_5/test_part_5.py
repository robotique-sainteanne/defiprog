# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_5 import part_5

def test_from_problem_description():
    assert part_5("voici un petit texte test") == \
         "    i t e \n" \
         "  t c i t \n" \
         "  s i t x \n" \
         "n e o e e \n" \
         "u t v p t \n" \
         "     \n" \

def test_simple():
    assert part_5("programming is so very fun") == \
    "        g \n" \
    "        n \n" \
    "        i \n" \
    "        m \n" \
    "        m \n" \
    "        a \n" \
    "        r \n" \
    "      y g \n" \
    "    n r o \n" \
    "s o u e r \n" \
    "i s f v p \n" \
    "     \n" \
    

def test_simple_2():
    assert part_5("this is like a diagram!") == \
    "        m \n" \
    "        a \n" \
    "        r \n" \
    "    s e g \n" \
    "    i k a \n" \
    "  s h i i \n" \
    "a i t l d \n" \
    "     \n" 