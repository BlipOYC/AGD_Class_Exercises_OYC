def discriminant(a, b, c):
    d = (b ** 2 - 4 * a * c)
    return d ** 0.5 if d >= 0 else set() #Will raise a TypeError when trying to find the discriminant

def solve_quadratic(a, b, c):
    try:
        return [-b + discriminant(a,b,c)/(2*a), (-b - discriminant(a,b,c))/(2*a),2]
    except:
        return []