#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# In[2]:


df= pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Excel\Campusx\train.csv")


# In[3]:


df.head()


# Why do EDA
# . Model building
# . Validate assumption
# . Analysis and reporting
# . Handling missing values
# . feature enginerring
# . detecting outlier
Column Types
. numercial = PassengerId,Age,Fare
.Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
. Mixed - Name,Ticket,CabinAge=
-- Conclusions- 
1. there is around 20 percent missing value in the age column
2. there are some outlier 
# In[4]:


df["Age"].describe()


# In[8]:


df['Age'].plot(kind='hist',bins=20)


# In[9]:


df['Age'].plot(kind='kde')


# In[10]:


df['Age'].skew()


# In[11]:


df['Age'].plot(kind='box')


# In[12]:


df[df['Age']>65]


# In[13]:


df['Age'].isnull().sum()/len(df['Age'])


# In[14]:


len(df['Age'])

Fare-
-Conclusion-
- The data is highly skew
- there is no missing value in it 
- This column contain group fare not individual fare
- for that we need create a columns in which we enter the individual score in it

# In[15]:


df['Fare'].describe()


# In[16]:


df['Fare'].plot(kind='hist',bins=20)


# In[17]:


df['Fare'].plot(kind='bar')


# In[18]:


df['Fare'].plot(kind='kde')


# In[19]:


df['Fare'].skew()


# In[20]:


df['Fare'].plot(kind='box')


# In[21]:


df[df['Fare']>250]


# In[22]:


df[df['Fare']>100].count()


# In[23]:


df['Fare'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
1. Survived-
- Conclusion-;
- More than 60% person was died in that accident
- only 39% count surived from that accident
- And there is no null value inside survived column

# In[24]:


df['Survived'].value_counts()


# In[25]:


df['Survived'].value_counts().plot(kind='bar')


# In[26]:


df['Survived'].value_counts().plot(kind='pie',autopct='%0.1f%%')


# In[27]:


df['Survived'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
2. Pclass-
- Conclusion-;
- in the data in 2 class passeenger are lower than other two class we have to find out why
- No Null value

# In[28]:


df['Pclass'].value_counts()


# In[29]:


df['Pclass'].value_counts().plot(kind='bar')


# In[30]:


df['Pclass'].value_counts().plot(kind='pie',autopct='%0.1f%%')


# In[31]:


df['Pclass'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
3. Sex-
- Conclusion-;
- No Null value
- Female passage is lower than male passage
# In[32]:


df['Sex'].value_counts()


# In[33]:


df['Sex'].value_counts().plot(kind='bar')


# In[34]:


df['Sex'].value_counts().plot(kind='pie',autopct='%0.01f%%')


# In[35]:


df['Sex'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
4. Sibsp-
- Conclusion-;
- Single person list is high compare 1 and 2 sibling 
- no Null Value
# In[36]:


df['SibSp'].value_counts()


# In[37]:


df['SibSp'].value_counts().plot(kind='bar')


# In[38]:


df['SibSp'].value_counts().plot(kind='pie',autopct='%0.01f%%')


# In[39]:


df['SibSp'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
4. Parch-
- conclusion-
- No missing value 
- Create a new col called is_alone
-Parch and SibSp can be merge and make new col family_size
# In[40]:


df['Parch'].value_counts()


# In[41]:


df['Parch'].value_counts().plot(kind='bar')


# In[42]:


df['Parch'].value_counts().plot(kind='pie',autopct='%0.01f%%')


# In[43]:


df['Parch'].isnull().sum()

Categorical- Survived,Pclass, Sex, Sibsp,Parch,Embarked
4. Embarked-
- conclusion-
- 2 Missing value in this Embarked
# In[44]:


df['Embarked'].value_counts()


# In[45]:


df['Embarked'].value_counts().plot(kind='bar')


# In[102]:


df['Embarked'].value_counts().plot(kind='pie',autopct='%0.01f%%')


# In[46]:


df['Embarked'].isnull().sum()

Mixed Column we are not going to do anything Categorical to Categorical data

Conclusion-
- As per this 1 class people had previlega because of their money 64% people surived from 1class and from 3class 64% people loss thier life

# In[47]:


pd.crosstab(df['Pclass'],df['Survived'],normalize='index')*100


# In[48]:


sns.heatmap(pd.crosstab(df['Pclass'],df['Survived'],normalize='index')*100)


# Check Surived and gender bivariate or relation
Categorical to Categorical data
Survived and Sex

Conclusion-
-74% female surived by this accident
# In[49]:


pd.crosstab(df['Survived'],df['Sex'],normalize='columns')*100


# In[50]:


sns.heatmap(pd.crosstab(df['Survived'],df['Sex'],normalize='columns')*100)

Categorical to Categorical data
Survived and Embarked

Conclusion-
- According to this because most of
# In[51]:


pd.crosstab(df['Survived'],df['Embarked'],normalize='columns')*100


# In[52]:


sns.heatmap(pd.crosstab(df['Survived'],df['Embarked'],normalize='columns')*100)


# In[53]:


pd.crosstab(df['Sex'],df['Embarked'],normalize='columns')*100


# In[54]:


pd.crosstab(df['Pclass'],df['Embarked'],normalize='columns')*100

let find out realtion between age and survived
remember that survived is categorical data nad age is a Numercial data
# In[55]:


df[df['Survived']==1]['Age'].plot(kind='kde',label='Survived')
df[df['Survived']==0]['Age'].plot(kind='kde',label='Not Survived')
plt.legend(loc='upper right')
plt.show()


# In[56]:


df[df['Pclass']==1]['Age'].mean()


# In[57]:


## Feature eneginerring on Fare col


# In[58]:


df[df['SibSp']==8]


# In[59]:


df1=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Excel\Campusx\test.csv")


# In[60]:


df1


# In[61]:


df=pd.concat([df,df1])


# In[62]:


df


# In[63]:


df[df['Ticket']=='CA. 2343']


# In[64]:


df['Ticket'].value_counts()


# In[65]:


df[df['Ticket']=='CA 2144']


# In[66]:


df['Individual_fare']=df['Fare']/(df['SibSp'] + df['Parch']+1)


# In[67]:


df


# In[68]:


df[df['Ticket']=='CA. 2343']


# In[69]:


df[df['Ticket']=='CA 2144']


# In[70]:


df[['Individual_fare','Fare']].describe()


# In[71]:


df['Total_member']=(df['SibSp'] + df['Parch']+1)


# In[72]:


df

## Let create a Numerical to Category type
# 1-> alone
# 2-4-> small 
# >5 -> large
# In[73]:


def transform_family_size(num):
    if(num==1):
        return 'Alone'
    elif(num>1 and num<5):
        return 'Small'
    else:
        return 'Large'


# In[74]:


df['Family_type']=df['Total_member'].apply(transform_family_size)


# In[77]:


df


# In[78]:


pd.crosstab(df['Survived'],df['Family_type'],normalize='columns')*100


# In[79]:


df['Surname']=df['Name'].str.split(',').str.get(0)


# In[80]:


df


# In[81]:


df['title']=df['Name'].str.split(',').str.get(1).str.strip().str.split(' ').str.get(0)


# In[82]:


df


# In[83]:


df['title'].value_counts()


# In[84]:


df['title']=df['title'].str.replace('Rev.','other')
df['title']=df['title'].str.replace('Dr.','other')
df['title']=df['title'].str.replace('Col.','other')
df['title']=df['title'].str.replace('Mlle.','other')
df['title']=df['title'].str.replace('Don.','other')
df['title']=df['title'].str.replace('the','other')
df['title']=df['title'].str.replace('Jonkheer.','other')
df['title']=df['title'].str.replace('Dona.','other')
df['title']=df['title'].str.replace('Capt.','other')
df['title']=df['title'].str.replace('Sir.','other')
df['title']=df['title'].str.replace('Lady.','other')
df['title']=df['title'].str.replace('Major.','other')
df['title']=df['title'].str.replace('ootherr.','other')


# In[85]:


df['title'].value_counts()


# In[86]:


df


# In[87]:


pd.crosstab(df['Survived'],df['title'],normalize='columns')*100


# In[88]:


df['title'].describe()


# In[89]:


df['title'].value_counts()


# In[90]:


df['title'].unique()


# In[91]:


df['title']=df['title'].str.replace('ootherr','OTH')
df['title']=df['title'].str.replace('other','OTH')


# In[92]:


df['title'].value_counts()


# In[93]:



pd.crosstab(df['Survived'],df['title'],normalize='columns')*100


# In[94]:


sns.heatmap(pd.crosstab(df['Survived'],df['title'],normalize='columns')*100)


# In[95]:


df


# In[96]:


pd.crosstab(df['Surname'],df['Survived'],normalize='index')*100


# So Survived chance of "Mrs" is More than other as per this data and is she belong the Pclass 1 so she will 100% survived this.
