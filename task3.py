import numpy as np
import pandas as pd
import tensorflow as tf
df = pd.read_csv(r"C:\Users\HP\OneDrive - kaist.ac.kr\sem4\intro to data science\train.csv\train.csv", encoding="utf-8")
factorized = ['ProcessType', 'OriginCountry','ExportationCountry', 'BorderTransportMeans', 'PaymentType', 'DeclarationOfficeID', 'TransactionNature', 'Type', 'DeclarerID', 'ImporterID', 'SellerID', 'ExpressID', 'DisplayIndicator', 'DutyRegime']
dropped = ['ID']#, 'TransactionNature', 'Type', 'DeclarerID', 'ImporterID', 'SellerID', 'ExpressID', 'DisplayIndicator', 'DutyRegime']

df['IssueDateTime'] = df['IssueDateTime'].str[5:7].astype(int)
df['ClassificationID'] = df['ClassificationID'].apply(lambda x: int(str(x)[0]) if len(str(x)) == 9 else int(str(x)[0:2]))


from sklearn.preprocessing import LabelEncoder
LE1 = LabelEncoder()

for x in factorized:
    df[x] = np.array(LE1.fit_transform(df[x]))


X = df.iloc[:,2:-1].values
Y = df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

ann = tf.keras.models.Sequential()


ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))

ann.add(tf.keras.layers.Dense(units=6,activation="sigmoid"))

ann.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

ann.fit(X_train,Y_train,batch_size=32,epochs = 100)

print("Hello World")

df2 = pd.read_csv(r"C:\Users\HP\OneDrive - kaist.ac.kr\sem4\intro to data science\test.csv\test.csv", encoding="utf-8")

#print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1,50000]])) > 0.5)
df2['IssueDateTime'] = df2['IssueDateTime'].str[5:7].astype(int)
df2['ClassificationID'] = df2['ClassificationID'].apply(lambda x: int(str(x)[0]) if len(str(x)) == 9 else int(str(x)[0:2]))

LE1 = LabelEncoder()

for x in factorized:
    df2[x] = np.array(LE1.fit_transform(df2[x]))

X2 = df2.iloc[:,2:].values

X2 = sc.transform(X2)
Y2 = ann.predict(X2)

Y2 = (Y2 > 0.7)

result = pd.DataFrame(Y2, columns = ['Predicted'])
result.to_csv("result.csv", index = 0)
