def evaluate_model(xtrain,ytrain,xtest,ytest,model):
    from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
    # predict the data fom trainig and testing
    ypred_tr=model.predict(xtrain)
    ypred_ts=model.predict(xtest)
     # Calculate metrics for training data
    tr_mse = mean_squared_error(ytrain, ypred_tr)
    tr_rmse = tr_mse**(1/2)
    tr_mae = mean_absolute_error(ytrain, ypred_tr)
    tr_r2 = r2_score(ytrain, ypred_tr)
    
    # Calculate metrics for testing
    ts_mse = mean_squared_error(ytest, ypred_ts)
    ts_rmse = ts_mse**(1/2)
    ts_mae = mean_absolute_error(ytest, ypred_ts)
    ts_r2 = r2_score(ytest, ypred_ts)
    
    # Print all the results
    print('Training Results :\n')
    print(f'Mean Squared Error (MSE) : {tr_mse:.2f}')
    print(f'Root Mean Squared Error (RMSE) : {tr_rmse:.2f}')
    print(f'Mean Absolute Error (MAE) : {tr_mae:.2f}')
    print(f'R2 Score : {tr_r2:.4f}')
    
    print('\n=================================================\n')
    
    print('Testing Results :\n')
    print(f'Mean Squared Error (MSE) : {ts_mse:.2f}')
    print(f'Root Mean Squared Error (RMSE) : {ts_rmse:.2f}')
    print(f'Mean Absolute Error (MAE) : {ts_mae:.2f}')
    print(f'R2 Score : {ts_r2:.4f}')