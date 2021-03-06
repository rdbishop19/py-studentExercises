def format_list(arr, oxford=True, conj="and"):
    '''
    formats an array of items to be comma-separated

    parameters:
    arr = array item to be iterated
    oxford = boolean to include/exclude Oxford Comma
    conj = string to choose different coordinating conjuction than default "and"
    '''
    
    if len(arr) == 2:
        return f'{arr[0]} {conj} {arr[1]}'
    else:
        formatted_list = ''
        for i in range(0, len(arr)):
            if i == 0:
                formatted_list = arr[i]
            elif i == len(arr)-1:
                if oxford:
                    formatted_list += f', {conj} {arr[i]}'
                else:
                    formatted_list += f' {conj} {arr[i]}'
            else:
                formatted_list += f', {arr[i]}'

        return formatted_list

if __name__ == '__main__':
    ## EXAMPLES WITH OXFORD COMMA
    # output: "one, two, three, and four"
    arr = ['one', 'two', 'three', 'four']
    print('array length', len(arr))
    print(format_list(arr))
    print()

    # output: "one, two, and three"
    arr = ['one', 'two', 'three']
    print('array length', len(arr))
    print(format_list(arr))
    print()

    # output: "one and two"
    arr = ['one', 'two']
    print('array length', len(arr))
    print(format_list(arr))
    print()

    # output: "one"
    arr = ['one']
    print('array length', len(arr))
    print(format_list(arr))
    print()

    ## EXAMPLES W/O OXFORD
    print('---Oxford comma omitted---')
    # output: "one, two and three"
    arr = ['one', 'two', 'three']
    print('array length', len(arr))
    print(format_list(arr, oxford=False))
    print()

    # output: "one, two, three and four"
    arr = ['one', 'two', 'three', 'four']
    print('array length', len(arr))
    print(format_list(arr, oxford=False))
    print()
