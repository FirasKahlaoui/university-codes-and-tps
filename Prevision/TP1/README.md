# Simple Linear Regression

This README provides an overview of interpreting the results from a simple linear regression analysis, focusing on key metrics such as p-values and R-squared.

## Key Metrics

### 1. Coefficient Estimates

- **Intercept**: Represents the expected value of the dependent variable when all independent variables are zero. It may not always have a practical interpretation but provides a baseline.

- **Slope Coefficient**: Indicates the change in the dependent variable for a one-unit increase in the independent variable. A negative value suggests an inverse relationship, while a positive value indicates a direct relationship.

### 2. p-value

The p-value assesses the statistical significance of each coefficient:

- **p-value < 0.05**: Indicates strong evidence against the null hypothesis, suggesting that the independent variable significantly affects the dependent variable.

- **p-value >= 0.05**: Indicates weak evidence against the null hypothesis, suggesting that the independent variable may not significantly affect the dependent variable.

### 3. R-squared (R²)

- R-squared measures the proportion of variance in the dependent variable explained by the independent variable(s):
  - **0 <= R² < 0.5**: Indicates a weak relationship; the model explains little of the variance.
  - **0.5 <= R² < 0.8**: Indicates a moderate relationship; the model explains a fair amount of variance.
  - **R² >= 0.8**: Indicates a strong relationship; the model explains a large portion of the variance.

### 4. Residual Standard Error

- This metric indicates the average distance that the observed values fall from the regression line. A smaller value suggests a better fit of the model to the data.

## Conclusion

In summary, when interpreting results from a simple linear regression:

- A significant p-value (typically < 0.05) suggests that the independent variable has a meaningful impact on the dependent variable.
- R-squared values help assess how well the model fits the data and can indicate the strength of the relationship.
- Always consider the context and domain knowledge when making interpretations.
