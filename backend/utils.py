def levenshtein(a: str, b: str, max_distance: int = 2) -> int:
    if abs(len(a) - len(b)) > max_distance:
        return max_distance + 1

    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        curr = [i] + [0] * len(b)
        min_row = curr[0]
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
            min_row = min(min_row, curr[j])

        if min_row > max_distance:
            return max_distance + 1  # early exit

        prev = curr

    return prev[-1]

def get_suggestions(word: str, dictionary: list[str], max_distance: int = 2, top_n: int = 3) -> list[str]:
    candidates = []

    for dict_word in dictionary:
        # 1. Filter by word length
        if abs(len(dict_word) - len(word)) > max_distance:
            continue

        # 2. Compute Levenshtein distance with early exit
        dist = levenshtein(word, dict_word, max_distance=max_distance)
        if dist <= max_distance:
            # 3. Apply prefix match bonus (smaller is better)
            score = dist - 0.1 if dict_word[0] == word[0] else dist
            candidates.append((dict_word, score))

    # 4. Sort by score then alphabetically
    candidates.sort(key=lambda x: (x[1], x[0]))

    return [word for word, _ in candidates[:top_n]]

