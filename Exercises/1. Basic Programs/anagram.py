from collections import Counter


def isAnagram(w1: str, w2: str) -> bool:
    print(Counter(w1), Counter(w2))
    return Counter(w1) == Counter(w2)


print(isAnagram("THE MORSE CODE", "HERE COME DOTS"))
