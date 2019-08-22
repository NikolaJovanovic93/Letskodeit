import csv


def get_csv_data(filename):
    rows = []
    datafile = open(filename, "r")
    reader = csv.reader(datafile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
























