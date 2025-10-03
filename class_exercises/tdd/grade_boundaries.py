import warnings

GRADE_BOUNDARIES= {
    264 : "A*",
    229 : "A",
    189 : "B",
    150 : "C",
    111 : "D",
    72 : "E",
    0 : "U"
    }

def calc_grade(p_mark, p_boundaries=GRADE_BOUNDARIES):
    if not isinstance(p_mark, int):
        raise TypeError("p_mark must be an integer")
    if p_mark > 350 or p_mark < 0:
        raise ValueError("The mark must be between 350 and 0")
    for boundary_mark in p_boundaries.keys():
        if p_mark >= boundary_mark:
            return p_boundaries[boundary_mark]

def make_user_boundaries():
    r_dict = {}
    if input("Would you like to enter your own grade boundaries? [Y for yes and anything else for no] ").upper() != "Y":
        return
    user_boundaries = input("Enter the grade boundaries from A* to E (U is always 0), separated by a space: ").split(" ")
    for idx, boundary in enumerate(user_boundaries):
        r_dict[int(boundary)] = ["A*", "A", "B", "C", "D", "E"][idx]
    return r_dict

        
if __name__ == "__main__":
    print(calc_grade(34))