from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

# This script will load a list of files with NBA player stats, one file for each season
# Then, using Linear Regression with the following predictor and response variables, find
# model coefficients that will allow us to predict whether a player with certain stats is 
# likely to make the All NBA team
#
#   Predictor variables:
#       Points Per Game
#       Minutes Played
#       True Shooting %
#       Rebounds
#       Usage Rate
#
#   Response variable:
#       All NBA?
 
def pymain():
    # filenames to process
    filenames = [
        '2013-2014_Player_Stats_Clean_All_NBA_Added.csv',
        '2014-2015_Player_Stats_Clean_All_NBA_Added.csv',
        '2015-2016_Player_Stats_Clean_All_NBA_Added.csv',
        '2016-2017_Player_Stats_Clean_All_NBA_Added.csv',
        '2017-2018_Player_Stats_Clean_All_NBA_Added.csv',
        '2018-2019_Player_Stats_Clean_All_NBA_Added.csv',
        '2019-2020_Player_Stats_Clean_All_NBA_Added.csv',
        '2020-2021_Player_Stats_Clean_All_NBA_Added.csv',
        '2021-2022_Player_Stats_Clean_All_NBA_Added.csv',
    ]

    all_player_data_df = pd.DataFrame()

    for fn in filenames:
        df = pd.read_csv(fn)

        # concat the DFs together by rows, ignoring the second df index.
        all_player_data_df = pd.concat([all_player_data_df, df], axis=0, ignore_index=True)

    model_matrix_df = all_player_data_df.loc[:, ['PPG', 'USG', 'MPG']]
    model_matrix = model_matrix_df.to_numpy()
    response_variable = all_player_data_df.loc[:, 'ALL_NBA']

    fit = LinearRegression().fit(model_matrix, response_variable)

    print(fit.intercept_)
    print(fit.coef_)
        
    ppg_prediction = 30
    usg_prediction = 11
    mpg_prediction = 20

    print("Stats for hypothetical player:")
    print("PPG: " + str(ppg_prediction))
    print("USG: " + str(usg_prediction))
    print("MPG: " + str(mpg_prediction))
    
    print("Model prediction as to whether the player will be All-NBA:")
    print(fit.predict(np.asarray([[ppg_prediction, usg_prediction, mpg_prediction]])))

    #N = np.shape(df)[0]
    #x = df["beds"].to_numpy()
    #o = np.argsort(x)
    #x = x[o]
    #X = np.c_[x, x**2]
    #y = df.loc[o, "infection_risk"]

    #print(all_player_data_df)


    

# get rollin
pymain()