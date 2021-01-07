def correct_braces(braces):
    # get rid of all initial closing braces
    i = 0
    while i < len(braces) and braces[i] == ')':
        i += 1
    braces = braces[i:]

    # base case for recursion
    if not braces:
        return ''

    # check for the first balanced group of braces
    open_braces = 0
    for i, brace in enumerate(braces):
        if brace == '(':
            open_braces += 1
        elif brace == ')':
            open_braces -= 1

        if not open_braces:
            break

    print(braces[open_braces:]," or ",braces[:i+1] + correct_braces(braces[i+1:]))
    # if there is one, process the rest separately, else truncate the excess opening braces
    return braces[open_braces:] if open_braces else braces[:i+1] + correct_braces(braces[i+1:])


# Tests
assert correct_braces("()(()") == "()()"
assert correct_braces("()(()))") == "()(())"
assert correct_braces(")(())") == "(())"
assert correct_braces("())(") == "()"
# assert correct_braces("))()(") == "()()()()"


"""

Aother way
"""

def correct_braces1(string):

    new_string=[]
    counter=0

    for char in string:
        if char=='(':
            new_string.append(char)
            counter +=1
        else:
            if counter ==0:
                new_string.append('(')
            else:
                counter -=1
            
            new_string.append(')')

    while counter>0:
        new_string.append(')')
        counter -=1


    return "".join(new_string)

print(correct_braces1("))()("))