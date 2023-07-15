import csv
with open("archive/german bundesliga data.csv", 'r') as file:
    csvreader = csv.reader(file)
    with open('实验/德甲/追跳/霍芬海姆', 'a') as f:
        name = 'HOFFENHEIM'
        for i in range(4):
            year = '2016'
            countList = []
            betType = 0
            betList = [100, 200, 600, 1800, 5400, 16200, 48600, 145800]
            rewardList = []
            tmpRewardList = []
            if i == 0:
                boolean = 0
                round = 6
                f.write('第七轮后按第七轮赌注跟:')
            elif i == 1:
                boolean = 1
                round = 6
                f.write('第七轮后放弃跟：')
            elif i == 2:
                boolean = 0
                round = 7
                f.write('第八轮后按第八轮赌注跟:')
            else:
                boolean = 1
                round = 7
                f.write('第八轮后放弃跟：')
            file.seek(0)
            for row in csv.DictReader(file):
                reward = 0
                if row['Home Team'] == name or row['Away Team'] == name:
                    tmp = row['Score'].split('-')
                    if (int(tmp[0]) + int(tmp[1])) % 2 == 0:
                        countList.append(0)
                    else:
                        countList.append(1)
                if row['year'] != year:
                    level = 0
                    last = countList[0]
                    if countList[0] == betType:
                        reward -= betList[level]
                    else:
                        reward += betList[level]
                        level += 1
                    tmpRewardList.append(reward)
                    for i in countList[1:]:
                        if i == last:
                            reward -= betList[level]
                            level = 0
                        else:
                            reward += betList[level]
                            if boolean == 0:
                                if level != round:
                                    level += 1
                            else:
                                if level == round:
                                    level = 0
                                else:
                                    level += 1
                        tmpRewardList.append(reward)
                        last = i
                    reward = reward * 0.95
                    rewardList.append(reward)
                    betListNew = [str(x) for x in betList]
                    betListNew = ','.join(betListNew)
                    f.write('\n' + year + '-' + str(int(year) + 1) + '赛季 ')
                    f.write('策略：' + betListNew + ' 收益：' + str(reward))
                    year = row['year']
                    countList = []
            level = 0
            last = countList[0]
            if countList[0] == betType:
                reward -= betList[level]
            else:
                reward += betList[level]
                level += 1
            tmpRewardList.append(reward)
            for i in countList[1:]:
                if i == last:
                    reward -= betList[level]
                    level = 0
                else:
                    reward += betList[level]
                    if boolean == 0:
                        if level != round:
                            level += 1
                    else:
                        if level == round:
                            level = 0
                        else:
                            level += 1
                tmpRewardList.append(reward)
                last = i
            reward = reward * 0.95
            rewardList.append(reward)
            betListNew = [str(x) for x in betList]
            betListNew = ','.join(betListNew)
            f.write('\n' + year + '-' + str(int(year) + 1) + '赛季 ')
            f.write('策略：'+betListNew+' 收益：'+str(reward))
            f.write('\n' + '五年总收益：'+str(sum(rewardList)))
            f.write('\n' + '最多投入：'+str(min(tmpRewardList)) + '\n')
        f.close()
    f.close()