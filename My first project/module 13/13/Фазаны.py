# В клетке находятся фазаны и кролики.
# Известно, что у них 35 голов и 94 ноги.
# Узнайте число фазанов и число кроликов.

heads = 35
legs = 94

for rabbits in range(heads+1):
    for phazans in range(heads+1):
        if (rabbits+phazans) > heads or \
            (rabbits*4+phazans*2) > legs:
            continue
        if (rabbits + phazans) == heads and \
                (rabbits*4+phazans*2) == legs:
            print('Rabbits: ', rabbits)
            print('Phazans: ', phazans)
            print('---')
