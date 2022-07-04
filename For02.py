def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x=[]
    for i in range(n):
        x.append(str(i))
    return ','.join(x)
print(main(3))