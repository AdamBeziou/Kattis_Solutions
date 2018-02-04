cases  = int(input())

for i in range(cases):
    name_dates = input().split()
    name = name_dates[0]
    enrolled_date = name_dates[1].split('/')
    date_of_birth = name_dates[2].split('/')
    classes = int(name_dates[3])
    
    if int(enrolled_date[0]) >= 2010:
        print(name + " eligible")
    elif int(date_of_birth[0]) >= 1991:
        print(name + " eligible")
    elif classes >= 41:
        print(name + " ineligible")
    else:
        print(name + " coach petitions")
