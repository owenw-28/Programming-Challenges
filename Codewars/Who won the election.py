def get_winner(ballots):
    candidates = {candidate:ballots.count(candidate) for candidate in set(ballots)}
    for candidate in candidates:
        if candidates[candidate]>len(ballots)/2:
            return candidate

if __name__ == '__main__':
    print(get_winner(["A", "A", "A", "B", "B"]))
    print(get_winner(["A", "A", "A", "B", "B", "C"]))
