import csv
from person import Person

def getclasses():
    with open('classes/classes.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        list1 = csvReader.next()
        list2 = csvReader.next()
        list3 = csvReader.next()

        return list1, list2, list3


def fix_cols(cols):
    for i in range(0, len(cols)):
        col = cols[i]
        cols[i] = col[ col.find('[') + 1 : len(col) - 1]

    return cols


def main():
    list1, list2, list3 = getclasses()

    eligible = []

    with open('dataset.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        col_headers = csvReader.next()
        col_headers = fix_cols(col_headers)

        for row in csvReader:
            name = row[1]
            id = row[2]
            person = Person(name, id, row, col_headers, list1, list2, list3)

            if person.iseligible():
                eligible.append(person)
                print(person.name)


if __name__ == "__main__":
     main()
