# importing csv module
import csv

# csv file name 
filename = "data.csv"

fields = []
rows = []
if __name__ == '__main__':

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        # fields = csvreader.next()

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

            # get total number of rows
        print rows
        # print("Total no. of rows: %d" % (csvreader.line_num))
