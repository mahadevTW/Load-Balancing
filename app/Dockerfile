FROM python:3.6
Add requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "result.py"]
