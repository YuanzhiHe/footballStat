import csv
with open("archive/german bundesliga data.csv", 'r') as file:
    csvreader = csv.reader(file)
    with open('tmp', 'w') as f:
        year = '2016'
        countList = []
        for row in csv.DictReader(file):
            tmp = row['Score'].split('-')
            if (int(tmp[0]) + int(tmp[1])) % 2 == 0:
                countList.append(0)
            else:
                countList.append(1)
            if row['year'] != year:
                last = countList[0]
                odd = 1
                even = 1
                diff = 0
                oddList = []
                evenList = []
                diffList = []
                for i in countList[1:]:
                    if i == last:
                        if i == 1:
                            odd += 1
                        else:
                            even += 1
                        if diff != 0:
                            diffList.append(diff)
                            diff = 0
                    else:
                        diff += 1
                    if odd != 1 and i != 1:
                        oddList.append(odd)
                        odd = 1
                    if even != 1 and i != 0:
                        evenList.append(even)
                        even = 1
                    last = i
                oddListNew = [str(x) for x in oddList]
                evenListNew = [str(x) for x in evenList]
                diffListNew = [str(x) for x in diffList]
                f.write('\n' + year + '-' + str(int(year) + 1) + '赛季')
                f.write('\n' + '单顺：' + ''.join(oddListNew))
                f.write('\n' + '最大单顺：' + str(max(oddList)))
                f.write('\n' + '二连单顺：' + str(oddList.count(2)))
                f.write('\n' + '三连单顺：' + str(oddList.count(3)))
                f.write('\n' + '双顺：' + ''.join(evenListNew))
                f.write('\n' + '最大双顺：' + str(max(evenList)))
                f.write('\n' + '二连双顺：' + str(evenList.count(2)))
                f.write('\n' + '三连双顺：' + str(evenList.count(3)))
                f.write('\n' + '单跳：' + ''.join(diffListNew))
                f.write('\n' + '最大单跳：' + str(max(diffList)))
                f.write('\n' + '二连单跳：' + str(diffList.count(2)))
                f.write('\n' + '三连单跳：' + str(diffList.count(3)))
                year = row['year']
                countList = []
        last = countList[0]
        odd = 1
        even = 1
        diff = 0
        oddList = []
        evenList = []
        diffList = []
        for i in countList[1:]:
            if i == last:
                if i == 1:
                    odd += 1
                else:
                    even += 1
                if diff != 0:
                    diffList.append(diff)
                    diff = 0
            else:
                diff += 1
            if odd != 1 and i != 1:
                oddList.append(odd)
                odd = 1
            if even != 1 and i != 0:
                evenList.append(even)
                even = 1
            last = i
        oddListNew = [str(x) for x in oddList]
        evenListNew = [str(x) for x in evenList]
        diffListNew = [str(x) for x in diffList]
        f.write('\n' + year + '-' + str(int(year) + 1) + '赛季')
        f.write('\n' + '单顺：' + ''.join(oddListNew))
        f.write('\n' + '最大单顺：' + str(max(oddList)))
        f.write('\n' + '二连单顺：' + str(oddList.count(2)))
        f.write('\n' + '三连单顺：' + str(oddList.count(3)))
        f.write('\n' + '双顺：' + ''.join(evenListNew))
        f.write('\n' + '最大双顺：' + str(max(evenList)))
        f.write('\n' + '二连双顺：' + str(evenList.count(2)))
        f.write('\n' + '三连双顺：' + str(evenList.count(3)))
        f.write('\n' + '单跳：' + ''.join(diffListNew))
        f.write('\n' + '最大单跳：' + str(max(diffList)))
        f.write('\n' + '二连单跳：' + str(diffList.count(2)))
        f.write('\n' + '三连单跳：' + str(diffList.count(3)))