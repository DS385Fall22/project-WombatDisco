import pandas as pd
 
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

    # Append the year to the dataframe so we have record of it in our combined data
    df['YEAR'] = fn[0:9]

    # concat the DFs together by rows, ignoring the second df index.
    all_player_data_df = pd.concat([all_player_data_df, df], axis=0, ignore_index=True)

# make sure all blank values are filled with 0.
all_player_data_df.fillna(0, inplace = True)

# write output to single file we're gonna use from here out
all_player_data_df.to_csv('All_Player_Stats_All_Years.csv')
