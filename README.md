# Good practices

## 1. Use [dask](https://dask.org/) for multiprocessing  
- A great tool
- Multiprocessing for df, models, GridSearchCV
- Can be used with cluster

## 2. Write the whole model as *pipeline*  
### 2.1 Visualizing data
- [Panel](https://panel.pyviz.org/)

### 2.2 Data cleansing  
..

### 2.3 Feature engineering 
- [featuretools](https://github.com/Featuretools/featuretools)
- [tsfresh](https://tsfresh.readthedocs.io/en/latest/)  

### 2.4 Train-test split

### 2.5 GridSearchCV 
- custom CV is usually better. Use dask to parallelize this step  

### 2.6 Calculating metrics on test
