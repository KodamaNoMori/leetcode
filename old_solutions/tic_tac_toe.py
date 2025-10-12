import pytest

def find_winner(ttt_state):
    for i in range(len(ttt_state)):

        # Iterate through each row
        first_row_val = ttt_state[i][0]
        print(first_row_val)
        for j in range(len(ttt_state)):
            if first_row_val != ttt_state[i][j]:
                break
        else:
            return first_row_val
    for i in range(len(ttt_state)):

        # Iterate through each column
        first_row_val = ttt_state[0][i]
        print(first_row_val)
        for j in range(len(ttt_state)):
            if first_row_val != ttt_state[j][i]:
                break
        else:
            return first_row_val

    # L-R diagonal
    for i in range(len(ttt_state)):
        first_row_first_col = ttt_state[0][0]
        if first_row_first_col != ttt_state[i][i]:
            break
    else:
        return first_row_first_col

    # R-L diagonal
    for i in range(len(ttt_state)):
        first_row_last_col = ttt_state[len(ttt_state)-1][0]
        if first_row_last_col != ttt_state[i][len(ttt_state)-i-1]:
            break
    else:
        return first_row_last_col


def test_get_winner():
    ttt_state = [
       ["x", "o", "x"]
     , ["o", "x", "o"]
     , ["o", "o", "x"]
     ]
    assert find_winner(ttt_state) == "x"
    ttt_state = [
       ["o", "o", "x"]
     , ["o", "x", "o"]
     , ["x", "o", "x"]
     ]
    assert find_winner(ttt_state) == "x"
    ttt_state = [
       ["x", "o", "o"]
     , ["x", "x", None]
     , ["x", "o", None]
     ]
    assert find_winner(ttt_state) == "x"
    ttt_state = [
       ["x", "o", "o"]
     , ["o", "x", "o"]
     , ["x", "x", "x"]
     ]
    assert find_winner(ttt_state) == "x"
    ttt_state = [
       ["x", "o", "x"]
     , ["o", "o", "o"]
     , ["x", "o", "x"]
     ]
    assert find_winner(ttt_state) == "o"
    ttt_state = [
       ["x", "o", "x"]
     , ["o", None, "o"]
     , ["x", "o", "x"]
     ]
    assert find_winner(ttt_state) is None
