def equality_check(a, b, c):
    if a == b or a == c or b == c:
        return True
    elif (a == int(b) or b == int(a)) or (a == int(c) or c == int(a)) or (b == int(c) or c == int(b)):
        return True
    else:
        return False


# Display equality results
print(equality_check(1, 2, "1"))  # True
print(equality_check(5, "6", "6"))  # True
print(equality_check("77", 4, 77))  # True
print(equality_check(3, 4, 5))  # False
