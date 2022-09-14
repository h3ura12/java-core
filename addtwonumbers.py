def main(s):
    subtract_dict = {
        'I' : ['V', 'X'],
        'X':  ['L', 'C'],
        'C':  ['D', 'M'],
    }
    main_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    sum = 0
    i = 0
    while i != len(s):
        # print(s[i])
        # print(s[i+1] in subtract_dict[s[i+1]])
        if i != len(s) - 1 :
            if s[i] in subtract_dict and s[i+1] in subtract_dict[s[i]]:
                sum += main_dict[s[i+1]] - main_dict[s[i]]
                # print(main_dict[s[i+1]] - main_dict[s[i]])
                i += 2
            else:
                sum += main_dict[s[i]]
                # print(main_dict[s[i]])
                i += 1

        else:
            sum += main_dict[s[i]]
            # print(main_dict[s[i]])
            i += 1





    return sum

print(main("III"))