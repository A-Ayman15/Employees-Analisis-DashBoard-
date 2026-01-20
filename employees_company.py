import numpy as np
import pandas as pd

df=pd.read_excel('employees_company.xlsx')
#print(df)
#df.info()
df.drop('No',axis=1,inplace=True)
df.drop('Office',axis=1,inplace=True)
df=df.rename(columns={'Ge':'Gender'})
df=df.rename(columns={'First Name2':'First Name'})
df.dropna(subset='First Name',inplace=True)
df.dropna(subset='Last Name',inplace=True)
df['Years of Experience']=df['Years of Experience'].fillna(df['Years of Experience'].mean()).astype('int')
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
df['Monthly Salary']=df['Monthly Salary'].fillna(df['Monthly Salary'].mean())
df['Annual Salary']=df['Annual Salary'].fillna(df['Annual Salary'].mean())
df['Job Rate']=df['Job Rate'].fillna(df['Job Rate'].median())
df['Overtime Hours']=df['Overtime Hours'].fillna(df['Overtime Hours'].mean()).astype('int')
df['Full Name']=(df['First Name']+' '+df['Last Name']).str.title()
df.drop(['First Name','Last Name'],axis=1,inplace=True)
df['total Monthly salary']=(df['Monthly Salary']+(df['Overtime Hours']*(df['Monthly Salary']/(30*8)))).astype('float64')

overlair_calc = ['Years of Experience', 'Monthly Salary', 'Annual Salary', 'Job Rate', 'Sick Leaves','Unpaid Leaves','Overtime Hours','total Monthly salary']
for col in overlair_calc:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]
    
# print(df.isna().sum())
# print(df.duplicated().sum())
df.info()
print(df)
df.to_csv('Cleaned_Employee_Data.csv', index=False)