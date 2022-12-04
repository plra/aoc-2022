from p1 import round_score, RPS_VALUES

OPP_CODE_VALUES = dict(zip("ABC", RPS_VALUES))


total_score = 0

with open("input.txt") as f:
    for line in f:
        opp_code, p_code = line.strip().split()
        opp_val = OPP_CODE_VALUES[opp_code]
        # To determine P's response, we rotate "rps" right, left or not at all if P must lose, draw
        # or win, respectively. E.g. if p_code == "X", P loses, and R/P/S is met with S/R/P
        # (rotate right 1).
        rotation_index = ord(p_code) - ord("Y")
        responses = RPS_VALUES[rotation_index:] + RPS_VALUES[:rotation_index]
        p_val = responses[RPS_VALUES.index(opp_val)]
        score = round_score(opp_val, p_val)
        total_score += score

if __name__ == "__main__":
    print(total_score)
