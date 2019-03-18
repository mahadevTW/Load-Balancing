import threading
import requests

def make_request():
    for i in range(1000):
        url = 'http://localhost:5000/'
        res = requests.get(url)
        print res.content
        print "Thread1", i


def make_request1():
    for i in range(1000):
        url = 'http://localhost:5000/result'
        res = requests.post(url,data={'prnNO':1000})
        print res.content
        print "Thread2", i


if __name__ == "__main__":

    t1 = threading.Thread(target=make_request)
    t2 = threading.Thread(target=make_request1)

    t1.start()
    t2.start()
