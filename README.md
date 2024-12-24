# PRODIGY_DS_02: Titanic Dataset Exploratory Data Analysis (EDA)
This project involves an in-depth exploratory data analysis (EDA) of the Titanic dataset to uncover key insights and patterns related to passenger demographics, ticketing, and survival rates. The analysis sheds light on how various factors like age, class, and family size influenced survival probabilities during the Titanic disaster.

## Overview
The Titanic dataset is a well-known dataset often used for learning data analysis and predictive modeling. This project focuses on performing EDA to extract meaningful insights about the passengers and their survival rates. It identifies patterns, highlights missing data, and explores relationships between features like age, fare, gender, and class with survival outcomes.

## Project Goals
The main objectives of this project are:

Understand the Dataset: Explore the distribution of key features and identify missing values, outliers, and data inconsistencies.
Discover Survival Patterns: Analyze relationships between passenger attributes (e.g., class, gender, age) and survival rates.
Data Transformation: Identify opportunities for feature engineering, such as creating new columns (e.g., family size).
Provide Actionable Insights: Highlight findings that can help build predictive models or inform future research.

## Dataset

The Titanic dataset includes the following key columns:

Age: Age of the passenger (contains missing values and outliers).
Fare: Fare paid for the ticket (highly skewed data, includes group fares).
Survived: Binary column indicating survival (0 = No, 1 = Yes).
Pclass: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd).
Sex: Gender of the passenger.
Sibsp: Number of siblings/spouses aboard the Titanic.
Parch: Number of parents/children aboard.
Additional columns: Embarked, Ticket, Cabin, etc.
The dataset does not include individual-level fare details, and some columns have significant missing values (e.g., age).

## Data Analysis
Missing Values and Outliers
Age: Contains 20% missing values and outliers.
Fare: No missing values but highly skewed data.
Sibsp and Parch: No missing values and can be combined into a new column called family_size.
Key Insights
Survival Analysis:
60% of passengers did not survive; 39% survived.
1st class passengers had a significantly higher survival rate (64%) compared to 3rd class passengers (36%).
Female passengers had a survival rate of 74%, much higher than males.
"Mrs" passengers in 1st class had the highest survival chances.
Passenger Demographics:
The number of single passengers was higher compared to those with siblings/spouses.
Female passengers were fewer than male passengers.
Feature Relationships:
Fare distribution is highly skewed, with a few passengers paying significantly higher fares.
Age distribution shows missing data and a few extreme outliers.
## Visualization
The following visualizations are included:

Histograms for numerical variables (e.g., age, fare).
Bar charts for categorical variables (e.g., survival by class, gender).
Box plots to visualize outliers in age and fare.
Model Architecture
This project does not include machine learning modeling. Instead, it focuses on data preprocessing and exploratory data analysis using Python libraries like:

Pandas for data manipulation.
Matplotlib and Seaborn for visualizations.
Training
This project emphasizes EDA rather than predictive modeling. However, the insights from this analysis can be used as a foundation for building classification models in the future.

## Results
Key findings from the analysis:

Age:
20% of values are missing.
Outliers are present.
Fare:
Data is highly skewed, indicating a few passengers paid significantly higher fares.
Survival Rates:
60% of passengers did not survive, while 39% survived.
1st class passengers had a higher survival rate compared to 2nd and 3rd classes.
Female passengers had significantly higher survival chances than males.
Categorical Analysis:
"Mrs" passengers in 1st class had the highest survival rate.
Single passengers were more prevalent than those traveling with families.

## Conclusion
This analysis provides a clear understanding of the Titanic dataset and its key features. Insights such as the relationship between passenger class, gender, and survival can inform future predictive modeling efforts. The presence of missing values and outliers highlights the need for careful preprocessing before building machine learning models.

This EDA demonstrates the importance of exploratory analysis in uncovering patterns and relationships in data, forming the foundation for effective decision-making and predictive modeling.
