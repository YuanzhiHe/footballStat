import csv
import statistics
name = "BIELEFELD"
with open("archive/german bundesliga data.csv", 'r') as file:
    csvreader = csv.reader(file)
    with open("德甲数据统计/%s"%name, 'w') as f:
        year = '2016'
        f.write(year)
        for row in csv.DictReader(file):
            if row['year'] != year:
                year = row['year']
                f.write('\n'+year)
            if row['Home Team'] == name or row['Away Team'] == name:
                tmp = row['Score'].split('-')
                if (int(tmp[0]) + int(tmp[1])) % 2 == 0:
                    f.write(','+'双')
                else:
                    f.write(','+'单')
statistics.stat(name)