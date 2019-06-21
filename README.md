# Useful_functions
Good practices:

1. Use [dask](https://dask.org/) for multiprocessing
2. Write the whole model as *pipeline*
2.1 Data cleansing
2.2 Feature engineering (*featuretools, tsfresh*)
2.3 GridSearchCV (custom CV is usually better. Use dask to parallelize this step)
