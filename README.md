# Good practices

## 0. Set random seeds

```
def set_seed(gpu=False):
    random.seed(42)
    np.random.seed(42)
    torch.manual_seed(42)
    if gpu:
        torch.cuda.manual_seed_all(42)
```

## 1. Keep all files in database. Read and write files directly in it
- Postgre SQL  
- Hive  

## 2. Use [dask](https://dask.org/) for multiprocessing  
- A great tool
- Multiprocessing for df, models, GridSearchCV
- Can be used with cluster

## 3. Write the whole model as *pipeline*  
### 2.1 Visualizing data
- [Panel](https://panel.pyviz.org/)

### 3.2 Data cleansing  
..

### 3.3 Feature engineering 
- [featuretools](https://github.com/Featuretools/featuretools)
- [tsfresh](https://tsfresh.readthedocs.io/en/latest/)  

### 3.4 Train-test split

### 3.5 GridSearchCV 
- custom CV is usually better. Use dask to parallelize this step  

### 3.6 Calculating metrics on test
