def karatsuba(x,y):
    """
    multiplying two integers with karatsuba multiplication
    """

    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y

    n1 = len(str(x))
    n2 = len(str(y))

    a = x // 10**(n1//2)
    b = x % 10**(n1//2)
    c = y // 10**(n2//2)
    d = y % 10**(n2//2)

    """
    x*y=(10^(n/2)a+b)(10^(n/2)c+d)
       =(10^(n)ac+10^(n/2)(ad+bc)+bd)
    Need to call everything on the last row recursively
    """

    ac = karatsuba(a,c)
    ad = karatsuba(a,d)
    bc = karatsuba(b,c)
    bd = karatsuba(b,d)

    return 10**(n1//2+n2//2)*ac + 10**(n1//2)*ad + 10**(n2//2)*bc + bd
