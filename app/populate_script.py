# importing csv module
import csv
import MySQLdb
import time
# csv file name
filename = "dataPopulation/data.csv"

fields = []
rows = []
time.sleep(5)
con = MySQLdb.connect('mysql', 'root', 'root', 'Student_Result')


def create_tables(con):
    drop_tables(con)
    student = "create table if not exists student (prnNo int(20) primary key, seatNo int(20), name varchar(30), motherName varchar(30)," \
              "collegeCode int(20) )"
    college = "create table if not exists college(collegeCode int(20) primary key, collegeName varchar(30), address varchar(30))"
    subject = "create table if not exists subject(subCode int(20) primary key, subName varchar(30))"
    submarks = "create table if not exists subMarks(id int(20) primary key AUTO_INCREMENT , subCode int(20), prnNo int(20), obtainMarks int(20), " \
               "totalMarks int(20))"
    result = "create table if not exists result (id int(20) primary key AUTO_INCREMENT, prnNo int(20), obtainMarks int(20), totalMarks int(20), sem int(20))"
    resultSubMarks = "create table if not exists result_subMarks(resultId int(20), subMarksId int(20))"

    fkstudent = "alter table student add foreign key(collegeCode) references college(collegeCode)"
    fksubMarks = "alter table subMarks add foreign key(subCode) references subject(subCode)"
    fksubMarks1 = "alter table subMarks add foreign key(prnNo) references student(prnNo)"
    fkresult = "alter table result add foreign key(prnNo) references student(prnNo)"
    fkresultSubMarks = "alter table result_subMarks add foreign key(resultId) references result(id)"
    fkresultSubMarks1 = "alter table result_subMarks add foreign key(subMarksId) references subMarks(id)"

    print ("Migrations started")
    migrations = [student, college, subject, submarks, result, resultSubMarks, fkstudent,
                  fksubMarks, fksubMarks1, fkresult, fkresultSubMarks, fkresultSubMarks1]
    cursor = con.cursor()
    for query in migrations:
        print (query)
        cursor.execute(query)
    con.commit()
    print ("Migrations done!!")


tables = ["college", "result", "result_subMarks", "student", "subMarks", "subject"]


def truncate_table(con):
    print ("Truncating tables")
    cursor = con.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS = 0')

    for t in tables:
        q = "TRUNCATE TABLE " + t
        print (cursor.execute(q))
    cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
    print ("Truncating tables done!!")


def drop_tables(con):
    print ("Drop tables")
    cursor = con.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
    for t in tables:
        q = "DROP TABLE IF EXISTS  " + t
        print (cursor.execute(q))
    cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
    print ("Truncating tables done!!")


def populate_subjects(con):
    sub_name = [{"name": "ML", "code": 10}, {"name": "ICS", "code": 20},
                {"name": "COMPILER", "code": 30}, {"name": "BD", "code": 40}]
    cursor = con.cursor()
    for s in sub_name:
        print (s)
        try:
            cursor.execute("insert into subject values(%s,%s)", (s['code'], s['name'],))
        except:
            pass
    con.commit()
    print ("Subject populated !!")

def populate_college(con):
    college= [{"name": "JSPM ICOR", "code": 1, "address": "Wagholi"},{"name": "JSPM BSICOR", "code": 2, "address": "Wagholi"}]
    cursor = con.cursor()
    for s in college:
        print (s)
        try:
            cursor.execute("insert into college values(%s,%s,%s)", (s['code'], s['name'],s['address'],))
        except:
            pass
    con.commit()
    print ("College populated !!")

def populate_data(con):
    cursor = con.cursor()

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
        id = 10000
        truncate_table(con)
        populate_subjects(con)
        populate_college(con)
        try:
            for row in csvreader:
                subject_data = row[:19]
                id = id + 1

                # print (row)
                # clg_data = [row[4]]
                # clg_data.extend(row[5:7])
                # print ("college: ", clg_data)
                #
                # query1 = "insert into college values(%s, %s, %s)"
                # res1 = cursor.execute(query1, clg_data)
                # con.commit()
                # # print (res1)



                # print (row[:5])
                student_data = row[:5]
                print ("student:", student_data)
                query = "insert into student values(%s, %s, %s, %s, %s)"
                res = cursor.execute(query, student_data)
                con.commit()
                # print (res)
                print (row)
                subject_data = [row[5]]
                subject_data.append(row[0])
                subject_data.extend(row[6:8])
                print ("subject1:", subject_data)
                query2 = "insert into subMarks(subCode,prnNo,obtainMarks,totalMarks) values (%s,%s,%s,%s)"
                res = cursor.execute(query2, subject_data)
                con.commit()

                # subject_data1.append(id)
                # print (subject_data1)

                subject_data2 = [row[8]]
                subject_data2.append(row[0])
                subject_data2.extend(row[9:11])

                print ("subject2", subject_data2)
                query3 = "insert into subMarks (subCode,prnNo,obtainMarks,totalMarks) value(%s, %s, %s,%s)"
                res = cursor.execute(query3, subject_data2)
                con.commit()

                subject_data3 = [row[11]]
                subject_data3.append(row[0])
                subject_data3.extend(row[12:14])
                print ("subject3", subject_data3)
                query4 = "insert into subMarks (subCode,prnNo,obtainMarks,totalMarks) value(%s, %s, %s,%s)"
                res = cursor.execute(query4, subject_data3)
                con.commit()

                subject_data4 = [row[14]]
                subject_data4.append(row[0])
                subject_data4.extend(row[15:17])
                print ("subject4", subject_data4)
                query5 = "insert into subMarks (subCode,prnNo,obtainMarks,totalMarks) value(%s, %s, %s,%s)"
                res = cursor.execute(query5, subject_data4)
                con.commit()


                result_data = [row[0]]
                result_data.append(row[17])
                result_data.extend(row[18:20])
                # result_data.append(id)
                print ("result", result_data)
                query6 = "insert into result (prnNo, totalMarks, obtainMarks, sem) value(%s, %s, %s,%s )"
                res = cursor.execute(query6, result_data)
                con.commit()


                # query = "insert into subject value(%s, %s, %s, %s, %s)"
                # res = cursor.execute(query, subject_data)
                # con.commit()
                # print (res)
                #
                # college_data = row[4:7]
                # query = "insert into college value(%s, %s, %s)"
                # res = cursor.execute(query, college_data)
                # con.commit()
                # print (res)
                #
                # subject_data = row[7:9]
                # query = "insert into subject value(%s, %s)"
                # res = cursor.execute(query, subject_data)
                # con.commit()
                # print (res)
                #
                # _data = row[7:9]
                # query = "insert into subject value(%s, %s)"
                # res = cursor.execute(query, subject_data)
                # con.commit()
                # print (res)

                # break

                # extracting each data row one by one
                # for row in csvreader:
                # print (row[7:19])



                #  student_data = row[:12]
                # query = "insert into student value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                # res = cursor.execute(query, student_data)
                # con.commit()
                # print (res)

                # break

                # get total number of rows
            student_data = row[5]
            # clg_data=row[3]

            # print("Total no. of rows: %d" % (csvreader.line_num))
        except:
            pass
    cursor.close()

def migrate(con):
    drop_tables(con)
    # truncate_table()

    create_tables(con)
    populate_data(con)

if __name__ == '__main__':
    migrate(con)