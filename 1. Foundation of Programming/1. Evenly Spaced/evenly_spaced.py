"""
Given three ints, a b c, one of them is small, one is medium and one is large. 
Return true if the three values are evenly spaced, 
so the difference between small and medium is the same as the difference between medium and large.

evenlySpaced(2, 4, 6) → true
evenlySpaced(4, 6, 2) → true
evenlySpaced(4, 6, 3) → false

"""

def evenlySpaced(a,b,c):
    small = medium = large = 0
    small = min(min(a,b),c)
    large = max(max(a,b),c)
    
    if a != small and a!= large:
        medium = a
    elif b != small and b != large:
        medium = b
    else:
        medium = c
        
    space1 = medium - small
    space2 = large - medium
    
    if space1 == space2:
        return True
    else:
        return False
        

def main():
    a = evenlySpaced(2, 4, 6)
    b = evenlySpaced(4, 6, 2)
    c = evenlySpaced(4, 6, 3)
    print(a)
    print(b)
    print(c)
    
if __name__ == "__main__":
    main()
