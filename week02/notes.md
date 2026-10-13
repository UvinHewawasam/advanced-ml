# Week 02 (2026/09/01)

## Key concepts

- Variable Types
- EDA (Exploratory Data Analysis)

## What I learnt

- Variable types
    1. Quantitative variables (weight,height)
        1.1 Continuous veriable (eg: 12.256)
        1.2 Descrete variable (eg: 12)
    2. Qualitative Variable (name,gender)
        2.1 Ordinal
        2.2 Nominal

- EDA
    1. Univariable Analysis
    2. Bi-variate Analysis
    3. Multi variate Analysis
    4. Correlation Analysis

## Practical / code

Yes

## Assignment / homework

1. Univariate Findings:
    - Y1 is Right-skewed

2. Bivariate Findings:
    - Sharp, clean split: at X5=3.5 the Y1 violin is tight and low (median around 13, IQR roughly 10–15); at X5=7.0 the violin shifts up and widens.
    - Y1 is fairly similar and high across X4 = 110.25, 122.5, 147.0 (medians ≈28–33), then drops sharply at X4 = 220.5 (median around 13, tight low-spread violin).

3. Correlation Findings:
    - X2 and X1 have an extremely strong negative correlation (r = -0.99), while X4 and X5 also show a very strong negative correlation (r = -0.97). These indicate substantial redundancy among these predictors.
    - X2 and X4 have a strong positive correlation (r = 0.88), while X1 and X5 have a strong positive correlation (r = 0.83). This further confirms that the predictors form highly correlated groups.
    - X3 has relatively weak relationships with the other predictors (correlations range from -0.29 to 0.28)
    - X7 has no linear correlation with the other predictors (r = 0.00), indicating that it is largely independent of the remaining predictors.

Dataset      RMSE       MAE        R²
0   Train  2.920239  2.023600  0.915034
1    Test  2.989397  2.147063  0.914980

## Questions / things to revisit

N/A

