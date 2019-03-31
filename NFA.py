# Neil Byrne - G00343624

# ---References--- 
# Shunting Yard Algorithm - http://www.oxfordmathcenter.com/drupal7/node/628


def shunt(infix): # Shunting Yard Algorithm - Parses infix notation to postfix notionation
    
    specials = {'*': 50, 
				'+': 45,
				'?': 40, 
				'.': 35, 
				'|': 30}   #Operators
    pofix = ""
    stack = ""

    for c in infix: # Read infix char at a time
        if c == '(':	# If open bracket push to the stack
            stack = stack + c
        elif c == ")":	# If closing bracket, pop from the stack
            while stack[-1] != '(':	# Keep poping from stack until open bracket then  pop
                pofix = pofix + stack [-1]
                stack = stack[:-1]
            stack = stack [:-1]
        elif c in specials:	# If special char pop the operators of lower precedence and push to special char to stack
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack [:-1]
            stack = stack + c
        else:	# Regular chars are pushed normaly 
            pofix = pofix + c

    while stack:	# Add symbol from top of stack to the pofix string 
        pofix, stack = pofix + stack[-1], stack [:-1]
    return pofix
##print (shunt("(a.b)|(c*.d)"))



class state: # Thompson's Constuction - Turn regular expressions into non deterministic finite automata
    label = None 
    edge1 = None
    edge2 = None

class nfa:	# NFA's will be created from this
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
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)	
			
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
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)

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
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)

		elif c == '+':
			# Pop a single NFA from the stack
			nfa1 = nfastack.pop()
			# Create new initial and accept states
			initial = state()
			accept = state()
			# Join the new initial state to nfa1's initial state and the new accept state
			initial.edge1 = nfa.initial
			# Join the old state to the new accept state and the new nfa1's initial state
			nfa.accept.edge1 = nfa.initial
			nfa.accept.edge2 = accept
			# Push new NFA to the stack
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)

		elif c == '?':
			# Pop only one NFA off the stack for the '?' operator
			nfa = nfaStack.pop()
			# Create new initial and accept state
			initial, accept = state(), state()
			# Connect the new initial state to the nfa initial state
			# Connect the nfa accept state to the new accept state
			initial.edge1 = nfa.initial
			initial.edge2 = accept
			# Connect the nfa accept state to the new accept state
			nfa.accept.edge1 = accept
			# Create and push a new '?' NFA to the nfaStack
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)

		else:
			# Create new initial accept states
			accept = state()
			initial = state()
			# Join the initial state to the accept state using an arrow labeled c
			initial.label = c
			initial.edge1 = accept
			# Push new NFA to the stack
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)

	return nfastack.pop()	# Only one state should be left to pop at this point

"""Returns the set of states that can be reached from the current state following its edges"""
def followEdges(state):
	state = set()	# Create new set with state as its only element
	states.add(state)
	
	if state.label is None:	# If states label is special
		if state.edge1 is not None:	# If edge1 is pointing at a state
			states |= followEdges(state.edge1)	# Follow this edge
		if state.edge2 is not None:	# If edge2 is poiting at a state
			states |= followEdges(state.edge2)	# Follow this edge
	return states
	
"""Matches output string to infix regualr expression"""
def match(infix, string):
	postfix = shunt(infix)	# Shunt the regular expression
	nfa = compile(postfix)
	# Sets to save the states
	current = set()
	next = set()
	
	current |= followEdges(nfa.initial)	# Concat the initial and current state
	
	for s in string:	# Loop through each char of string
		for c in current:	# Loop through current set of states
			if c.label == s
				next |= followEdges(c.edge1)	# Concat edge1 to the next set
		current = next	# Set the current set to the next set
		next = set()	# Clear the next set
		
	return(nfa.accept in current)	# Check if accept state is in the set of current set
		
	
	
##	Testing	##	
print('TESTING - SHUNTING YARD ALGORITHM - TESTING')
print(shunt('A+B+C'))
print(shunt('A+B*C'))
print(shunt('A*(B+C)'))
print(shunt('A+B-C'))
print(shunt('A.B|C'))









