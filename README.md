# Marketing Sales Data Analysis

This repository contains a Python data analysis assignment completed as part of my Data Analytics coursework.

## Topics Covered
- Data loading and inspection using Pandas
- Descriptive statistics
- Linear algebra concepts (scalar, vector, matrix)
- Weighted business score using dot product
- Revenue and profit change analysis
- Log transformation
- Cumulative calculations
- Principal Component Analysis (PCA)
- Data visualization using Matplotlib

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Tools Used
- Python
- Jupyter Notebook

## Dataset
Marketing sales dataset used for academic purposes.

import pandas as pd

## Task A: Load and inspect data
### Open the notebook, load the CSV, check shape, columns, data types, and missing values.

```python
df = pd.read_csv("marketing_sales_math.csv") 
df.shape
df.columns
print(type(df))
df.isnull().sum()
```


## Task B: Descriptive statistics recap
### Calculate mean, median, mode, range, and standard deviation for selected variables.
```python
### mean, median, standard deviation
print(df[['advertising_spend','website_visits','profit']].agg(['mean', 'median', 'std']))

### mode
print("Mode of performance segment:", df['performance_segment'].mode()[0])

### Range
print("Range of profit:",df['profit'].max()-df['profit'].min())
```

## Task C: Linear algebra view
### Represent one row as a vector and select numerical columns as a matrix.
```python
### Representing one row as a Vector
vector_day1=df.loc[0,['advertising_spend','website_visits','price','units_sold','revenue']].values
print(vector_day1)

### Representing selected numerical columns as a Matrix
matrix= df[['advertising_spend','website_visits','price','units_sold','revenue']].values
print(matrix)

### Shape of the matrix
matrix.shape  

### Display a scaler
scaler_advertising_spend_day1= df.loc[0, 'advertising_spend']
print('Advertising Spend on Day 1:',scaler_advertising_spend_day1)
```

## Task D: Weighted score
### Use a dot product to create a simple business score from standardized variables.
```python
### Selected Variables
features = ['advertising_spend',
            'website_visits',
            'units_sold',
            'revenue']

### Standardise the data
from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
x_scaled=scaler. fit_transform (df[features]) # Now every column has: mean≈ 0, std ≈ 1

### Assigned weights based on business importance
weights= [0.2,0.2,0.3,0.3] # Meaning: advertising_spend = 20%,website_visits = 20%,units_sold = 30%,revenue = 30%
#Weights should add up to 1

### calculated business score
import numpy as np
business_score=np.dot(x_scaled,weights)

### Add the business_score to the DataFrame as a new column
df['business_score'] = business_score
df[['business_score']].head()
```

## Task E: Change and derivatives
### Use .diff() to calculate daily change in revenue and profit.
```python
### calculated the day to day change in revenue 
df['revenue_change']= df['revenue'].diff()
print(df[['revenue','revenue_change']].head())

###Day-to-day change in profit
df['profit_change']= df['profit'].diff()
print(df[['profit','profit_change']].head(6))

### To find the strongest increase and the strongest decrease in revenue
best_revenue_day= df.loc[df['revenue_change'].idxmax()]
print("Largest revenue increase:")
print(best_revenue_day[['day','revenue','revenue_change']])

worst_revenue_day= df.loc[df['revenue_change'].idxmin()]
print("Largest revenue decrease:")
print(worst_revenue_day[['day','revenue','revenue_change']])
```

## Task F: Functions and transformations
### Use log transformation for website visits and interpret why it is useful.
```python
df['log_webiste_visits']= np.log(df['website_visits'])
df[['website_visits','log_webiste_visits']].head()
```

## Task G: Integration as accumulation
### Use cumulative sum to calculate cumulative revenue and cumulative profit.
```python
df['cumulative_revenue'] = df['revenue'].cumsum()
df['cumulative_profit'] = df['profit'].cumsum()
df[['revenue','cumulative_revenue','profit', 'cumulative_profit']].head()
```

## Task H: PCA
### Standardize numerical features, apply PCA, visualize PC1 and PC2, and interpret explained variance.
```python
### Select numerical features
features = ['advertising_spend','website_visits','price','units_sold','revenue', 'cost', 'profit']
X = df[features]

### Standardize the Data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

### Apply PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)  # This creates: PC1 (Principal Component 1),PC2 (Principal Component 2)

### Create a New DataFrame
pca_df= pd.DataFrame(principal_components,columns=['PC1','PC2'])
pca_df.head()

### Add PC1 and PC2 to original DataFrame
df['PC1'] = pca_df['PC1']
df['PC2'] = pca_df['PC2']

### Visualize PCA result
import matplotlib.pyplot as plt

for segment in ['Low profit', 'Medium profit', 'High profit']:
    subset = df[df['performance_segment']== segment]
    plt.scatter(subset['PC1'],subset['PC2'], label = segment, alpha=0.8,)
    
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Principal Component Analysis of Marketing Data')
plt.legend(title='Profit Segment')
plt.grid(True)
plt.show()  
```
![PCA Chart](pchart.PNG)
```python
### Explained Variance
print(pca.explained_variance_ratio_)
print("Explained variance ratio:")
print("PC1:", round(pca.explained_variance_ratio_[0], 3))
print("PC2:", round(pca.explained_variance_ratio_[1], 3))
print("Total:", round(pca.explained_variance_ratio_.sum(), 3))

### PCA loadings: which original features contribute to each component?
loadings = pd.DataFrame(pca.components_.T, columns=['PC1_loading','PC2_loading'],index=features)
loadings
```

