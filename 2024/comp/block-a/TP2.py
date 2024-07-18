import string

def solve(s1: str, s2: str):
    reconstructed = ''
    strs = [s1, s2]
    if len(s1) != len(s2):
        pointer_first = 0
        pointer_second = 0

        first = strs[strs.index(max(strs))]
        second = strs[strs.index(min(strs))]

        count = 0

        while True:
            if count % 2 == 0 and pointer_first != len(first):
                reconstructed += first[pointer_first]
                pointer_first += 1
            else:
                if pointer_second != len(second):
                    reconstructed += second[pointer_second]
                    pointer_second += 1

            count += 1
            if pointer_first == len(first) and pointer_second == len(second):
                break
    elif strs[0][-1] in string.punctuation:
        reconstructed = ''

        pointer_first = 0
        pointer_second = 0

        first = strs[1]
        second = strs[0]

        count = 0

        while True:
            if count % 2 == 0 and pointer_first != len(first):
                reconstructed += first[pointer_first]
                pointer_first += 1
            else:
                if pointer_second != len(second):
                    reconstructed += second[pointer_second]
                    pointer_second += 1

            count += 1
            if pointer_first == len(first) and pointer_second == len(second):
                break
    
    return reconstructed


print(solve('l optto epormaind accetvamn u!',
            'acmeiind rgamto el r s rietfn'))
