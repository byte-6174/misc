# Dawkin's Weasel program from The Blind Watchmaker (TBW)
# https://en.wikipedia.org/wiki/Weasel_program

import random

# destination_string = Target string that this script "evolve" towards. 
# parent.            = Randomly generated string that this "evolution" simulation begins with. 
# 
# parent ---- Evolution with random mutations ---> destination_string
# 
# It is important to note that in nature, there is no such "destination". 
# Even survival - or avoid death - is not really a goal of any entity. 
# It is just the fact that, whatever doesn't survive,
# its genes AUTOMATICALLY are not propagated further.
# What ever managed to get by - perhaps due to the little accumulated mutations - they survive
# long enough to have THEIR genes and not their dead sister's genes propaged.

# How to run this script:
# $python3 watchmaker_evolution.py

# You can modify next set of parameters and rerun to see the effects of
# different mutation rates, number of childrens.

# This is the actual string used in the Weasels program in TBW
destination_string = "METHINKS IT IS LIKE A WEASEL"

# This is the rate at which each "genetic" string in this simulation has chance of mutating.
mutation_rate = 0.01

# This is the number of children each parent have to generate the next generation.
num_children = 100

#----------------------------------------------------------------------------------------------
target = list(destination_string)
len_target = len(target)
# Generate the possible space of characters to select during mutation, in 
# world of strings its capitalized A-Z (and space) characters in this simulation.
charlist = [chr(c) for c in range(65,65+26)]
charlist.append(' ')

# Ramdomly generate first parent
parent = [charlist[random.randrange(len(charlist))] for _ in range(len_target)]
# Initialize a fitness score
max_score = 0
# Initialize generation id
generation = 1

# Evolve until our target is met - 
# In nature, there IS NO GOAL. In this simulation, we have to halt somewhere
# so we give this as a goal to evaluate the effects of mutation rate, number of children etc.
while parent != target:
    # run the same best string num_chiltren times
    for _ in range(num_children):
        ####################################### REPLICATOR ################################################
        # make a child - i.e. copy of parent - this is the gist of life on earth, 
        # replication of the string.
        child = parent.copy()
        # mutate the child with m% mutation rate [This is the next necessary ingredient for life]
        # It is introduction of "error" in replication. This introduces variability, and give organism a 
        # chance ! 
        # Try setting the mutation rate to 0.0 a see the simulation run forever, not converging :D
        for j in range(len_target):
            random_number = random.random()
            if random_number < mutation_rate:
                # mutate this character of this child
                child[j] = charlist[random.randrange(len(charlist))]
        ####################################### REPLICATOR ################################################
        
        # Evaluate how "FIT" this mutant child is, for some arbitrarily coherent string - this is done in this
        # simulation so that humans can grasp what is happening. 
        # In reality there is NO FITTING FUNCTION. There are environments and other species competing for same
        # resources etc. but its beyond scope of this simulation :)
        score = 0
        for k in range(len_target):
            # If this character "Matches" with the target character, 
            # its considered a "win" and 1 point is awarded.
            if child[k] == target[k]:
                score += 1

        # Evalute this mutant child's fitness against other children,
        # and keep track of the best child fit for the next generation.
        if score >= max_score:
            max_score = score
            curr_best_str = child 
    
    # Evaluated all the N children in this generation,
    # Now, choose the best fitting child as a starting point for the next generation.
    print(f"generation [{generation}] progeny with best score = {''.join(curr_best_str)} best score = {max_score}")
    parent = curr_best_str
    generation += 1
