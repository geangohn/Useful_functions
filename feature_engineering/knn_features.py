# knn = KnnFeatureExtractor(features_to_find_neighbors = ['lat', 'lon'],
#                           target = 'price',
#                           features = ['total_floors', 'build_year', 'total_area'])
# knn.calculation_of_aggregates(df)
# df = knn.do_extract(df)
# knn.save_artefact('outputs/')

from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np

class KnnFeatureExtractor:
    
    def __init__(self, features_to_find_neighbors, target, features):
        self.features_to_find_neighbors = features_to_find_neighbors   # ex: lat,lon
        self.target = target  # ex:   price
        self.features = features  # ex:  build_year, total_floors
        self._model = None

    def calculation_of_aggregates(self, df):
        knn = KNeighborsRegressor(n_neighbors=30,
                                      weights='uniform', # Некая регуляризация
                                      metric='minkowski',
                                      p=1,
                                      n_jobs=-1)
        X = df[self.features_to_find_neighbors]
        y = df[target]
        knn.fit(X, y)
        self._model = knn

    def do_extract(self, df):
        
        # Найти k ближайших соседей
        neighbors = self._model.kneighbors(df[self.features_to_find_neighbors], 
                                           n_neighbors=30, return_distance=False)
        
        # Выбрать столбцы, по которым будут считаться агрегаты
        _df = np.array(df[self.features].copy())
        
        # Посчитать агрегаты
        aggregates = np.concatenate([
                                     np.mean(_df[neig], axis=1), 
                                     np.std(_df[neig], axis=1), 
                                     np.quantile(_df[neig], q=0.5, axis=1), 
                                     np.quantile(_df[neig], q=0.1, axis=1), 
                                     np.quantile(_df[neig], q=0.9, axis=1), 
                                     np.min(_df[neig], axis=1), 
                                     np.max(_df[neig], axis=1)
                                    ], 
                                    axis = 1)
        
        # Добавить имена агрегатов
        func_names = ['mean', 'std', 'median', 'q_10', 'q_90', 'min', 'max']
        new_column_names = []
        for func in func_names:
            for col in self.features:
                new_column_names.append(f"knn_{func}_{col}")
         
        # Вставить агрегаты в исходный датафрейм
        aggregates = pd.DataFrame(aggregates, columns = new_column_names)
        df = pd.concat([df, aggregates], axis = 1)
        
        # Удалить все агрегаты кроме 'median' для таргета
        for col in new_column_names:
            if (target in col) & ('median' not in col):
                df.drop(col, axis=1, inplace=True)
        
        # Рассчитать разность между признаком объекта и агрегатами
        for col in self.features:
            for aggregate in new_column_names:
                if col == target:
                    continue  # Не считать разности по таргету
                elif col in aggregate:
                    df[f"{aggregate}_diff"] = np.round(df[col] - df[aggregate], 0) 
                    
        # Округлить агрегаты: это работает как регуляризация
        for aggregate in new_column_names:
            df[aggregate] = np.round(df[aggregate], 0)
            
        return df

    def save_artefact(self, dir):
        self._model.to_pickle(f"{dir}/knn_enc_lat_lon.pkl")
