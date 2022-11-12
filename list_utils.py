def permute(input, permutation):
    """Retrun input in order of permutation indices"""
    if len(permutation) != len(input):
        raise ValueError("Length of input doesn't match length of permutation")
    l = len(input)
    if set(permutation) != set(range(l)):
        raise ValueError("Invalid permutation")
    out = [None]*l
    for a,b in zip(input, permutation):
        print(a,b)
        out[b] = a
    return out

if __name__ == "__main__":
    pass