class Person:
    def __init__(self, name, id, row, col_headers, list1, list2, list3):
        self.name = name
        self.id = id

        self.col_headers = col_headers
        self.interest_cols = self.get_interest_cols(row)
        self.classes = self.correlate_classes(row)

        self.list1 = list1
        self.list2 = list2
        self.list3 = list3

        self.l1 = self.l2 = self.l3 = 0


    def add_points(self, l, grade):
        if grade == 'A':
            l += 3
        elif grade == 'B':
            l += 1
        return l

# return the total points for each list
    def calc_points(self):
        l1 = l2 = l3 = 0

        for name, grade in self.classes.items():
            # A is 3 points
            # B is 1 point
            try:
                 self.list1.index(name)
                 l1 = self.add_points(l1, grade)
            except:
                try:
                    self.list2.index(name)
                    l2 = self.add_points(l2, grade)
                except:
                    try:
                        self.list3.index(name)
                        l3 = self.add_points(l3, grade)
                    except:
                        print("ERROR: SOMETHING WENT REALLY F***ING WRONG")
                        print(name)

        return l1, l2, l3


# RETURNS: boolean for whether or not they are eligible
    def iseligible(self):
        self.l1, self.l2, self.l3 = self.calc_points()
        total = self.l1 + self.l2 + self.l3

        return total >= 10 and self.l1 >= 4 and self.l1 + self.l2 >= 7# 4 points are from list 1, and first 7 are from list 1 and 2


# RETURNS: dictionary with class title and name
    def correlate_classes(self, row):
        classes = {}
        for col in self.interest_cols:
            classes[self.col_headers[col]] = row[col]

        return classes


# RETURNS: an array wiht the columns that were filled out
    def get_interest_cols(self, row):
        interest = [] # interest rows are rowss that are not blank (they have a grade))
        for i in range(4, len(row)): # 0-3 are static fields
            if row[i] != "":
                interest.append(i)

        return interest
