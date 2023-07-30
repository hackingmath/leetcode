score = 0

def minimax(state,maximizing=True):
    if not state:
        return score

    tmp = state[::]
    possible_new_states = []
    for num in tmp:
        state.remove(num)
        print(state)
        possible_new_states.append((state,num))
        print("new_states:", possible_new_states)
        state.append(num)
    # possible_new_states = [
    #     (choices.remove(num),num) for num in state
    # ]
    print("new_states:",possible_new_states)
    if maximizing:
        scores = [new_state[1] - minimax(new_state[0],False)
            for new_state in possible_new_states
        ]
        print("maximizing scores:",scores)
        return score + max(scores)
    else:
        scores = [new_state[1] +
        minimax(new_state, True)
        for new_state in possible_new_states
        ]
        print("minimizing scores:", scores)
        return score + min(scores)

print(minimax([1,5,2]))