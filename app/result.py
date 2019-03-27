#!/usr/bin/env python
import sys
print(sys.argv)
import time
from flask import Flask, render_template, request
import MySQLdb

from dataPopulation.populate_script import migrate

time.sleep(5)
app = Flask(__name__)
con = MySQLdb.connect('mysql', 'root', 'tiger', 'Student_Result')
cursor = con.cursor()

migrate(con)
@app.route('/')
def student():
    return render_template('result.html')


@app.route('/result', methods=['POST'])
def result():
    request_data = request.form

    prn_no = request_data['prnNo']

    cur = con.cursor()

    cur.execute(
        "SELECT * FROM student INNER JOIN college ON student.collegeCode=college.collegeCode where prnNo=%s;",
        [prn_no])

    rows = cur.fetchall()
    # print rows


    if not rows:
        return render_template('wrongPRN.html')

    # print rows

    data_list = []

    for o in rows:
        # print o
        data = {}
        data['prnNo'] = o[0]
        data['seatNo'] = o[1]
        data['name'] = o[2]
        data['motherName'] = o[3]
        data['collegeCode'] = o[4]
        data['collegeName'] = o[6]
        data['collegeAdd'] = o[7]

        data_list.append(data)
    print data_list

    cur.execute("select * from subMarks as re RIGHT JOIN subject as s on re.subCode=s.subCode where prnNo=%s;",
                [prn_no])


    row = cur.fetchall()
    sub_list = []
    for i in row:
        # print i
        sub_data = {}
        sub_data['subjectCode'] = i[5]
        sub_data['subjectName'] = i[6]
        sub_data['obtainedMarks'] = i[3]
        sub_data['totalMarks'] = i[4]
        sub_list.append(sub_data)
        # print sub_list

    cur.execute("select * from result where prnNo=%s;", [prn_no])

    res = cur.fetchall()
    res_list = []
    for x in res:
        # print x
        res_data = {}
        res_data['totalMarks'] = x[3]
        res_data['obtainedMarks'] = x[2]
        res_data['sem'] = x[4]
        res_list.append(res_data)

    return render_template("result1.html", rows=data_list, row=sub_list, res=res_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)

