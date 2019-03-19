#coding=utf-8
import uuid
def getUuid():
    uuid_str=str(uuid.uuid4()).replace("-","")
    return uuid_str


if __name__=="__main__":
    for i in range(10):
        print(getUuid())