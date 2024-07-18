def solve(text: str):
    """
    [x] Remove capital letters that text[letter - 1] != '' i. e. letters that are not the first of a word
    [x] Add letters that have '. ' behind them capitalized (first of a sentence)
    [x] CRC -> always capitalized
    [x] Replace every '.' with '!' 
    """

    text = text.replace('.', '!')
    text = text.replace('?', '!')
    textlist = [x for x in text]
    
    for i in range(len(textlist)):
        if i == 0 or (i > 1 and textlist[i - 2] == '!'):
            textlist[i] = textlist[i].upper()
        elif textlist[i - 1] == ' ':
            textlist[i] = textlist[i]
        else:
            textlist[i] = textlist[i].lower()
    
    for j in range(len(textlist)):
        if j + 2 < len(textlist):
            if textlist[j].lower() == 'c' and textlist[j + 1].lower() == 'r' and textlist[j + 2].lower() == 'c':
                textlist[j] = textlist[j].upper()
                textlist[j + 1] = textlist[j + 1].upper()
                textlist[j + 2] = textlist[j + 2].upper()
    
    textlist = ''.join(item for item in textlist)
    

    return textlist


print(solve('Faute de Grand-mère!'))
