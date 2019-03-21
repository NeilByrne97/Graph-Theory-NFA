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



class state: # Thompson's Constuction - Turn regular expressions into non deterministic finite automata
    label = None 
    edge1 = None
    edge2 = None

class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept): # Constuctor
        self.initial = initial
        self.accept = accept

def compile(postfix):
    nfastack = []

    for c in postfix:
        if c == '.':
            #Pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connect first NFA's accept state to the seconds initial
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            nfastack.append(nfa(nfa1.initial, nfa2.accept))

        elif c == '|':
            # Pop two NFA's off the stack'
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.intial 
            # Create a new initial state, connect the accept states
            # of the two NFA's popped from the stack
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))

        elif c == '*':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Create new initial and accept states
            initial = state()
            accept = state()
            # Join the new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa.initial
            initial.edge2 = accept
            # Join the old state to the new accept state and the new nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial,accept))

        else:
            # Create new initial accept states
            accept = state()
            initial = state()
            # Join the initial state to the accept state using an arrow labeled c
            initial.label = c
            initial.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept))

    return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))

