
## Способ 1
alpha = 10
k = 1

gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=lgb_eval,
    
    ###
    callbacks=[lgb.reset_parameter(learning_rate = lambda current_round: alpha * e**(-k*current_round))]
    ###
)


## Способ 2
lambda_0 = 0.2
delta = 0.01

gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=lgb_eval,
    
    ###
    callbacks=[lgb.reset_parameter(learning_rate = lambda current_round: 
                                   lambda_0 - delta if current_round % 100 == 0 else lambda_0)]
    ###
)
