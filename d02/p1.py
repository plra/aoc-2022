RPS_VALUES = [1, 2, 3]
CODE_VALUES = dict(zip("ABCXYZ", RPS_VALUES * 2))


def round_score(opp_val, p_val):
    round_score = p_val
    # Outcome of RPS is uniquely determined by difference in values mod 3, where R,P,S = 1,2,3
    diff_mod_3 = (p_val - opp_val) % 3
    if diff_mod_3 == 1:  # P wins
        round_score += 6
    elif diff_mod_3 == 0:  # P draws
        round_score += 3
    return round_score


total_score = 0

with open("input.txt") as f:
    for line in f:
        opp_code, p_code = line.strip().split()
        opp_val, p_val = CODE_VALUES[opp_code], CODE_VALUES[p_code]
        score = round_score(opp_val, p_val)
        total_score += score

if __name__ == "__main__":
    print(total_score)
