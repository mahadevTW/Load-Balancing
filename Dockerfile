
# our base image
FROM alpine:3.5

FROM mysql

# Install python and pip
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y python-mysqldb

# install Python modules needed by the Python app
#COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN pip install flask
RUN pip install mysql-connector
# copy files required for the app to run
COPY result.py /usr/src/app/
COPY templates/result.html /usr/src/app/templates/
COPY templates/result1.html /usr/src/app/templates/
COPY templates/result2.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/result.py"]
