# PRODIGY_DS_02

This repository contains an Exploratory Data Analysis (EDA) of the Titanic dataset.

Key Findings:

- Age:
    - 20% missing values
    - Outliers present
- Fare:
    - Highly skewed data
    - No missing values
    - Contains group fare, not individual fare
- Survived:
    - 60% of passengers died, 39% survived
    - No missing values
- Pclass:
    - Class 2 passengers are lower than other two classes
    - No missing values
- Sex:
    - Female passengers are lower than male passengers
    - No missing values
- Sibsp:
    - Single persons are higher than those with 1 or 2 siblings
    - No missing values
- Parch:
    - No missing values
    - Can be merged with Sibsp to create a new column "family_size"
- Categorical Analysis:
    - 1st class passengers had a higher survival rate (64%)
    - 3rd class passengers had a lower survival rate (36%)
    - Female passengers (74%) had a higher survival rate than males
    - Survived chance of "Mrs" (female, Pclass 1) is higher than others

This analysis provides insights into the distribution of passenger characteristics and their relationship with survival rates.
