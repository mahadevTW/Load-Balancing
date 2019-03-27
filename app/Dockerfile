FROM python:2.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENV ASPNETCORE_URLS http://+:5000
EXPOSE 5000
CMD ["python", "result.py"]
