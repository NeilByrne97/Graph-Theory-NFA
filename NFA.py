# Neil Byrne - G00343624

# ---References--- 
# Shunting Yard Algorithm - http://www.oxfordmathcenter.com/drupal7/node/628


def shunt(infix): # Shunting Yard Algorithm - Parses infix notation to postfix notionation
    
    specials = {'*': 50, '.': 40,'|': 30}   #Operators
    pofix = ""
    stack = ""

    for c in infix: # Read infix char at a time
        if c == '(':
            stack = stack + c
        elif c == ")":
            while stack[-1] != '(':
                pofix = pofix + stack [-1]
                stack = stack[:-1]
            stack = stack [:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack [:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1], stack [:-1]
    return pofix



print (shunt("(a.b)|(c*.d)"))