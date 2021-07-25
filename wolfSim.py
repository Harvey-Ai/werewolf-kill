#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def killSim(guardMem, lastBeGuardMem, godArr, citizenArr, wolfArr, isDayTime):

    # 第几天
    dayNum = 0

    while (len(godArr) > 0 and len(wolfArr) > 0 and len(citizenArr) > 0):

        # day time vote progress
        if (isDayTime):

            isDayTime = False

            voteTime = 0
            voteeList = []

            # 把被投人假如数组，只有民和狼
            for wolfMem in wolfArr:
                voteeList.append(wolfMem)
            for citizenMem in citizenArr:
                voteeList.append(citizenMem)

            # 投票人包括所有人
            voterNum = len(godArr) + len(godArr) + len(citizenArr)

            while (voteTime < 2):

                voteeCountDict = {}
                for votee in voteeList:
                    voteeCountDict[votee] = 0

                # 投票人开始随机出票，-1表示弃票
                for i in range(voterNum):
                    voteIndex = random.randint(-1, len(voteeList) - 1)

                    if (voteIndex >= 0):
                        voterMem = voteeList[voteIndex]
                        voteeCountDict[voterMem] += 1

                # 统计每一位被投人的票数
                maxVotee = -1
                maxVote = 0
                maxVoteCount = 0
                for votee in voteeCountDict:

                    if voteeCountDict[votee] == 0:
                        continue

                    if voteeCountDict[votee] > maxVote:
                        maxVote = voteeCountDict[votee]
                        maxVoteCount = 1
                        maxVotee = votee
                    elif voteeCountDict[votee] == maxVote:
                        maxVoteCount += 1

                # 看最多得票的有几人，只有一人则出局，否则平票，再投一轮
                if maxVoteCount == 1:
                    if maxVotee in wolfArr:
                        wolfArr.remove(maxVotee)
                    elif maxVotee in citizenArr:
                        citizenArr.remove(maxVotee)

                    voteTime += 1

                voteTime += 1

        # 夜晚，守卫和狼人行动
        else:
            dayNum += 1
            isDayTime = True

            # 被刀的备选项
            beKilledList = []
            for godMem in godArr:
                beKilledList.append(godMem)
            for citizenMem in citizenArr:
                beKilledList.append(citizenMem)

            # 随机选一个刀
            beKillMemIndex = random.randint(0, len(beKilledList) - 1)
            beKillMem = beKilledList[beKillMemIndex]

            # 被守的备选项
            beGuardList = []
            # 不守神
        #    for godMem in godArr:
        #        beGuardList.append(godMem)
            for citizenMem in citizenArr:
                beGuardList.append(citizenMem)
            for wolfMem in wolfArr:
                beGuardList.append(wolfMem)

            beGuardMem = -1
            # 如果守卫还活着，守人
            if guardMem in godArr:

                # 选出守的人
                beGuardMemIndex = random.randint(-1, len(beGuardList) - 1)
                if beGuardMemIndex > -1:
                    beGuardMem = beGuardList[beGuardMemIndex]

                while (lastBeGuardMem == beGuardMem and lastBeGuardMem != -1):
                    beGuardMemIndex = random.randint(-1, len(beGuardList) - 1)
                    beGuardMem = beGuardList[beGuardMemIndex]

                # ！！这里修改程序，让守卫自守
                # 设为自守
                # beGuardMem = 1
                lastBeGuardMem = beGuardMem

            # 如果守卫对象不等于被杀的，把活人从数组里删除
            if (lastBeGuardMem != beKillMem):

                if beKillMem in citizenArr:
                    citizenArr.remove(beKillMem)
                else:
                    godArr.remove(beKillMem)


if __name__ == "__main__":

    wolfWin = 0
    godWin = 0

    for i in range(100000):

        # 上一次守的号码，-1表示空守
        lastBeGuardMem = -1
        # 守卫自己的号码
        guardMem = 1

        # 神，狼，民的号码数组
        godArr = [1, 2, 3]
        wolfArr = [4, 5]
        citizenArr = [6, 7]

        # 开始从白天还是晚上
        isDayTime = False

        killSim(guardMem, lastBeGuardMem, godArr, citizenArr, wolfArr, isDayTime)

        if len(wolfArr) > 0:
            wolfWin += 1
        else:
            godWin += 1

    print "good Win: " + str(godWin) + "\n"
    print "wolf Win: " + str(wolfWin) + "\n"
    print "win rate: " + str(godWin * 1.0 / (godWin + wolfWin) * 100) + "%"
