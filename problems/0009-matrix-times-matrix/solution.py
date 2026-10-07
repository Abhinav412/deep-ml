def matrixmul(a:list[list[int|float]],  b:list[list[int|float]])-> list[list[int|float]]:    
    if not a or not b or len(a[0]) != len(b):
        return -1
    else:
        return [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)]for a_row in a]