def one_hot_encoder(df, ohe_cols=['store','item','dayofmonth','dayofweek','month','weekofyear']):
    '''
    One-Hot Encoder function
    '''
    print('Creating OHE features..\nOld df shape:{}'.format(df.shape))
    df = pd.get_dummies(df, columns=ohe_cols)
    print('New df shape:{}'.format(df.shape))
    return df
