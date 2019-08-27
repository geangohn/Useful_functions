
alpha = 10
k = 1

gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=lgb_eval,
    
    ###
    callbacks=[lgb.reset_parameter(learning_rate = lambda current_round: alpha * e**(k*current_round)
    ###
)
