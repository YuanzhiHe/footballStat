def stat(name):
    with open('德甲数据统计/%s'%name, 'r') as f:
        odd = 1
        even = 1
        diff = 0
        row = f.readlines()
        f.close()
        with open('德甲数据统计/%s'%name, 'a') as f:
            for k in row:
                oddList = []
                evenList = []
                diffList = []
                tmp = k.split(',')
                last = tmp[1]
                for i in tmp[2:]:
                    if i == last:
                        if i == '单':
                            odd += 1
                        else:
                            even += 1
                        if diff != 0:
                            diffList.append(diff)
                            diff = 0
                    else:
                        diff += 1
                    if odd != 1 and i != '单':
                        oddList.append(odd)
                        odd = 1
                    if even != 1 and i != '双':
                        evenList.append(even)
                        even = 1
                    last = i
                oddListNew = [str(x) for x in oddList]
                evenListNew = [str(x) for x in evenList]
                diffListNew = [str(x) for x in diffList]
                f.write('\n'+tmp[0]+'-'+str(int(tmp[0])+1)+'赛季')
                f.write('\n'+'单顺：'+''.join(oddListNew))
                f.write('\n'+'最大单顺：'+str(max(oddList)))
                f.write('\n'+'二连单顺：'+str(oddList.count(2)))
                f.write('\n'+'三连单顺：'+str(oddList.count(3)))
                f.write('\n'+'双顺：'+''.join(evenListNew))
                f.write('\n'+'最大双顺：'+str(max(evenList)))
                f.write('\n'+'二连双顺：'+str(evenList.count(2)))
                f.write('\n'+'三连双顺：'+str(evenList.count(3)))
                f.write('\n'+'单跳：'+''.join(diffListNew))
                f.write('\n'+'最大单跳：'+str(max(diffList)))
                f.write('\n'+'二连单跳：'+str(diffList.count(2)))
                f.write('\n'+'三连单跳：'+str(diffList.count(3)))

            f.close()