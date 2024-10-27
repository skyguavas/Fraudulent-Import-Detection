import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def Q1(file):
    answer = file['ExportationCountry'].max()
    return answer

def Q2(file):
    answer = file['DeclarationOfficeID'].max()
    return answer

def Q3(file):
    answer = file.columns
    return len(answer)

def Q4(file):
    answer = len(file)
    return answer

def Q5(file):
    Prediction = 0
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for row in file.iterrows():
        row = row[1]
        if Prediction == 0:
            if row['Fake'] == 1:
                FP += 1
            else:
                TN += 1
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    return accuracy



def Q6(train_part, test_part):
    count = {}
    for j in range(1, 10):
        knn = KNeighborsClassifier(n_neighbors = j, weights='distance')
        td = train_part.iloc[:, [x for x in range(9)]]
        tl = train_part.iloc[:, [9]]
        td2 = test_part.iloc[:, [x for x in range(9)]]
        tl2 = test_part.iloc[:, [9]]
        tl = tl.values.flatten()
        tl2 = tl2.values.flatten()

        knn.fit(td, tl)
        Prediction = knn.predict(td2)

        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i in range(len(Prediction)):
            if Prediction[i] == 0:
                if tl2[i] == 1:
                    FP += 1
                else:
                    TN += 1
            else:
                if tl2[i] == 1:
                    TP += 1
                else:
                    FN += 1
        accuracy = ((TP + TN) / (TP + TN + FP + FN))
        count[j] = accuracy
    answer = max(count, key=count.get)
    return count, answer

def Q7(train_part, test_part):
    prev = Q6(train_part, test_part)
    count, value = prev[0], prev[1]
    answer = count[value]
    return round(answer, 3)

def Q8(df):
    train_part = df[df['IssueDateTime'] <= 9]
    test_part = df[df['IssueDateTime'] > 9]
    count = {}
    knn = KNeighborsClassifier(n_neighbors = 7, weights='distance')
    td = train_part.iloc[:, [x for x in range(103) if x != 8]]
    tl = train_part.iloc[:, [8]]
    td2 = test_part.iloc[:, [x for x in range(103) if x != 8]]
    tl2 = test_part.iloc[:, [8]]
    tl = tl.values.ravel()
    tl2 = tl2.values.ravel()

    knn.fit(td, tl)
    Prediction = knn.predict(td2)

    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(Prediction)):
        if Prediction[i] == 0:
            if tl2[i] == 1:
                FP += 1
            else:
                TN += 1
        else:
            if tl2[i] == 1:
                TP += 1
            else:
                FN += 1
        accuracy = ((TP + TN) / (TP + TN + FP + FN))
    return accuracy   

def func1(x):
    x = str(x)
    if len(x) == 10:
        return x[0:2]
    else:
        return x[0:1]

if __name__ == '__main__':
    file = pd.read_csv(r"C:\Users\HP\OneDrive - kaist.ac.kr\sem4\intro to data science\train.csv\train.csv", encoding="utf-8")
    
    file = file.drop(columns = [ 'ID', 'ProcessType', 'TransactionNature', 'Type', 'DeclarerID', 'ImporterID', 'SellerID', 'ExpressID', 'OriginCountry', 'DisplayIndicator', 'DutyRegime'])
    
    file['IssueDateTime'] = file['IssueDateTime'].str[5:7].astype(int)
    
    file['ClassificationID'] = file['ClassificationID'].apply(func1)
    x = pd.factorize(file['DeclarationOfficeID'], sort=True)
    file['DeclarationOfficeID'] = x[0]
    y = pd.factorize(file['PaymentType'], sort=True)
    file['PaymentType'] = y[0]
    z = pd.factorize(file['BorderTransportMeans'], sort=True)
    file['BorderTransportMeans'] = z[0]
    w = pd.factorize(file['ExportationCountry'], sort=True)
    file['ExportationCountry'] = w[0]

    print('Q1:')
    print(Q1(file))
    print('Q2:')
    print(Q2(file))

    train_part = file[file['IssueDateTime'] <= 9]
    test_part = file[file['IssueDateTime'] > 9]
    df = file
    df = pd.get_dummies(df, columns = ['ClassificationID'], drop_first=True)
    
    print('Q3:')
    print(Q3(df))
    print('Q4:')
    print(Q4(train_part))
    print('Q5:')
    print(Q5(test_part))
    print('Q6:')
    print(Q6(train_part, test_part))
    print('Q7:')
    print(Q7(train_part, test_part))
    print('Q8:')
    print(Q8(df))

