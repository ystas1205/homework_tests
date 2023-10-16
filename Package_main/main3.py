def vote(votes):
    d = {}
    for i in votes:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return max(d, key=d.get)


if __name__ == "__main__":
    vote([1, 1, 1, 2, 3])
    vote([1, 2, 3, 2, 2])
