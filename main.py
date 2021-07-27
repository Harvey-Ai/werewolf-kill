#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

## get random position
def getRandomPosition(count):

    wolfPosition = []
    while (len(wolfPosition) < count):

        position = random.randint(1, 12)
        exist = False

        for i in range(len(wolfPosition)):
            if position == wolfPosition[i]:
                exist = True

        if exist is False:
            wolfPosition.append(position)

    return wolfPosition

def shuffle(raw_list):

    begin = 0
    end = len(raw_list) - 1
    for i in range(5000):
        p1 = random.randint(begin, end)
        p2 = random.randint(begin, end)

        raw_list[p1], raw_list[p2] = raw_list[p2], raw_list[p1]

    return raw_list


if __name__ == "__main__":

    ## 随机猜6个位置
    ## 可以随便修改个数
    randomGuessPostion = getRandomPosition(4)

    cornerPartPostion = [1,6,7,12]
    leftPartPostion = [1,2,3,4,5,6]
    rightPartPostion = [7, 8, 9, 10, 11, 12]

    randomGuessPostion.sort()
    randomGuessOkCount = 0
    cornerOKCount = 0
    leftOKCount = 0
    rightOKCount = 0

    for i in range(10000):

        # 生成四张狼人
        raw_list = [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]
        shuffle_list = shuffle(raw_list)
        wolfPosition = []
        for i in range(len(shuffle_list)):
            if shuffle_list[i] == 0:
                wolfPosition.append(i + 1)

        cornerOK = False
        randomGuessOK = False
        leftOK = False
        rightOK = False
        for wolfPos in wolfPosition:

            # 随机猜中
            for randomPos in randomGuessPostion:
                if wolfPos == randomPos:
                    randomGuessOK = True

            #边角位中狼
            for cornerPartPos in cornerPartPostion:
                if wolfPos == cornerPartPos:
                    cornerOK = True

            # 左边中狼
            for leftPartPos in leftPartPostion:
                if wolfPos == leftPartPos:
                    leftOK = True

            # 右边中狼
            for rightPartPos in rightPartPostion:
                if wolfPos == rightPartPos:
                    rightOK = True

        if randomGuessOK is True:
            randomGuessOkCount += 1
        if cornerOK is True:
            cornerOKCount += 1
        if leftOK is True:
            leftOKCount += 1
        if rightOK is True:
            rightOKCount += 1

    ## 打印随机猜中概率
    outputStr = "random guess Postion: ["
    for i in range(len(randomGuessPostion)):
        outputStr += " " + str(randomGuessPostion[i])
    print outputStr + "] rate: " + str(randomGuessOkCount * 1.0 / 10000)

    # 打印边角位猜中概率
    outputStr = "corner  Postion: ["
    for i in range(len(cornerPartPostion)):
        outputStr += " " + str(cornerPartPostion[i])
    print outputStr + "] rate: " + str(cornerOKCount * 1.0 / 10000)

    # 打印左边位猜中概率
    outputStr = "left  Postion: ["
    for i in range(len(leftPartPostion)):
        outputStr += " " + str(leftPartPostion[i])
    print outputStr + "] rate: " + str(leftOKCount * 1.0 / 10000)

    # 打印右边位猜中概率
    outputStr = "right  Postion: ["
    for i in range(len(rightPartPostion)):
        outputStr += " " + str(rightPartPostion[i])
    print outputStr + "] rate: " + str(rightOKCount * 1.0 / 10000)