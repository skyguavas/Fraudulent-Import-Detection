import csv
import pandas as pd

def Q1(file):
    count = {}
    for row in file:
        for key in row:
            if row[key] == '':
                if key not in count:
                    count[key] = 1
                else:
                    count[key] += 1
    answer = max(count, key=count.get)
    value = count[answer]
    return answer, value

def Q2(file):
    air_fake = 0
    ship_fake = 0
    total_air = 0
    total_ship = 0
    for row in file:
        if row['BorderTransportMeans'] == '40':
            total_air += 1
        if row['BorderTransportMeans'] == '10':
            total_ship += 1
        if row['BorderTransportMeans'] == '40' and row['Fake'] == '1':
            air_fake += 1
        if row['BorderTransportMeans'] == '10' and row['Fake'] == '1':
            ship_fake += 1

    proportion_of_air = air_fake / total_air
    proportion_of_ship = ship_fake / total_ship
    is_air_greater = ''
    if proportion_of_air > proportion_of_ship: 
        is_air_greater = 'True'
    else:
        is_air_greater = 'False'    
    return ("Airplane:", proportion_of_air, "Ship:", proportion_of_ship, is_air_greater)

def Q3(file):
    Icn_airport_fake = 0
    Icn_airport_total = 0
    Icn_harbor_fake = 0
    Icn_harbor_total = 0
    for row in file:
        if row['DeclarationOfficeID'] == '40':
            Icn_airport_total += 1
        if row['DeclarationOfficeID'] == '20':
            Icn_harbor_total += 1
        if row['DeclarationOfficeID'] == '40' and row['Fake'] == '1':
            Icn_airport_fake += 1
        if row['DeclarationOfficeID'] == '20' and row['Fake'] == '1':
            Icn_harbor_fake += 1

    proportion_of_airport = Icn_airport_fake / Icn_airport_total
    proportion_of_harbor = Icn_harbor_fake / Icn_harbor_total
    is_airport_greater = ''
    if proportion_of_airport > proportion_of_harbor: 
        is_airport_greater = 'True'
    else:
        is_airport_greater = 'False' 
    return ("Airport:", proportion_of_airport, "Harbor:", proportion_of_harbor, is_airport_greater)

def Q4(file):
    count_fake = {}
    count_total = {}
    count_prop = {}
    for row in file:
        export_country = row['ExportationCountry']
        if export_country not in count_fake:
            count_fake[export_country] = 0
        if row['Fake'] == '1':
            count_fake[export_country] += 1
        if export_country not in count_total:
            count_total[export_country] = 1
            count_prop[export_country] = 0
        else:
            count_total[export_country] += 1
    for key in count_prop:
        count_prop[key] = count_fake[key] / count_total[key]
    del count_prop['ExportationCountry'] 

    result_dict = {}
    result_dict['HK'] = count_prop['HK']
    result_dict['GB'] = count_prop['GB']
    result_dict['US'] = count_prop['US']
    result_dict['IT'] = count_prop['IT']
    result_dict['CN'] = count_prop['CN']
    result_dict['FR'] = count_prop['FR']
    value = max(result_dict, key=result_dict.get)
    return value, result_dict[value]
    

def Q5(file):
    count_fake = {}
    count_total = {}
    count_prop = {}
    for row in file:
        export_date = row['IssueDateTime']
        export_month = export_date[5:7]
        if export_month not in count_fake:
            count_fake[export_month] = 0
        if row['Fake'] == '1':
            count_fake[export_month] += 1
        if export_month not in count_total:
            count_total[export_month] = 1
            count_prop[export_month] = 0
        else:
            count_total[export_month] += 1
    for key in count_prop:
        count_prop[key] = count_fake[key] / count_total[key]
    del count_prop['Da'] 
    value = max(count_prop, key=count_prop.get)
    return value, count_prop[value]
    # return count_prop


def Q6(file):
    tgm = []
    avtba = []
    for row in file:
        tgm.append(row['TotalGrossMassMeasure(KG)'])
        avtba.append(row['AdValoremTaxBaseAmount(Won)'])
    del tgm[0]
    del avtba[0]
    df = {'TotalGrossMassMeasure(KG)': tgm, 'AdValoremTaxBaseAmount(Won)': avtba}
    data = pd.DataFrame(df)
    corr = data.corr(method='pearson')
    return (corr.values.tolist())[0][1]
    
def Q7(file):
    fake = []
    tr = []
    for row in file:
        fake.append(row['Fake'])
        tr.append(row['TaxRate'])
    del fake[0]
    del tr[0]
    data = pd.DataFrame({'Fake': fake, 'TaxRate': tr})
    corr = data.corr(method='pearson')
    return (corr.values.tolist())[0][1]





if __name__ == '__main__':
    reader = open(r"C:\Users\HP\OneDrive - kaist.ac.kr\intro to data science\train.csv\train.csv", "r", encoding="utf-8")
    file = csv.DictReader(reader)
    print('Q1:')
    print(Q1(file))
    # print('\n')
    reader.seek(3)
    print('Q2:')
    print(Q2(file))
    # print('\n')
    reader.seek(3)
    print('Q3:')
    print(Q3(file))
    # print('\n')
    reader.seek(3)
    print('Q4:')
    print(Q4(file))
    # print('\n')
    reader.seek(3)
    print('Q5:')
    print(Q5(file))
    # print('\n')
    reader.seek(3)
    print('Q6:')
    print(Q6(file))
    # print('\n')
    reader.seek(3)
    print('Q7:')
    print(Q7(file))