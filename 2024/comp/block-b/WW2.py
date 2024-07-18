### Babylone's gardens (15 points) ###

def solve(flowers):
    calendar = ['', '', '', '', '', '', '', '', '', '', '', '']
    for i in range(len(flowers)):
        bloomtime = 12 - int(flowers[i][1])
        if calendar[bloomtime] == '':
            calendar[bloomtime] += flowers[i][0]
        else:
            calendar[bloomtime] += f' {flowers[i][0]}'
        
        callist = calendar[bloomtime].split(' ')
        callist.sort()
        calendar[bloomtime] = ' '.join(callist)

    return calendar


print(solve([['rose', '8'],
       ['tulip', '6'],
       ['petunia', '4'],
       ['sunflower', '5'],
       ['orchid', '4'],
       ['lily', '11'],
       ['iris', '8']]
      ))
