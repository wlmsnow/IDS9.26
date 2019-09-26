import numpy as np
import csv
import pandas as pd
from sklearn.model_selection import  StratifiedKFold

def writeInFile(Train, Test, i,data):
    newTrainFilePath = "datasetSKF\\train-%s.csv" % i
    newTestFilePath = "datasetSKF\\test-%s.csv" % i
    #newTrainlabelFilePath = "datasetSKF\\trainlabel-%s.csv" % i
   # newTestlabelFilePath = "datasetSKF\\testlabel-%s.csv" % i
    print(data[0])

    newTrainFile = open(newTrainFilePath, "w",newline='')  # wb 为防止空行
    newTestFile = open(newTestFilePath, "w",newline='')
   # newTrainlabelFile = open(newTrainlabelFilePath, "w", newline='')  # wb 为防止空行
   # newTestlabelFile = open(newTestlabelFilePath, "w", newline='')
    writerTrain = csv.writer(newTrainFile)
    writerTest = csv.writer(newTestFile)
  #  writerTrainlabel = csv.writer(newTrainlabelFile)
  #  writerTestlabel = csv.writer(newTestlabelFile)

    for index in Train:
        writerTrain.writerow(data[index])
    # for index in Train:
    #     writerTrainlabel.writerow(datalabel[index])
    for index in Test:
        writerTest.writerow(data[index])
    # for index in Test:
    #     writerTestlabel.writerow(datalabel[index])


    newTrainFile.close()
    newTestFile.close()
    # newTrainlabelFile.close()
    # newTestlabelFile.close()


def getKFoldDataSet():
    data = pd.read_csv("result.csv")
    Train = []
    Test = []

    sfolder = StratifiedKFold(n_splits=3, random_state=0, shuffle=False)

    for train, test in sfolder.split(data):
        Train.append(train)
        Test.append(test)
       # print('Train: %s | test: %s' % (train, test))
        #print(" ")
    data = data.values
    for i in range(3):

        writeInFile(Train[i], Test[i], i,data)




if __name__ == "__main__":
    getKFoldDataSet()