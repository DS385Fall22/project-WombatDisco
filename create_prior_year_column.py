import pandas as pd
import numpy as np
 
# filename of player data
filename = 'All_Player_Stats_All_Years.csv'

all_player_data_df = pd.read_csv(filename)

# Let's see if we can calculate a column labelled 'ALL_NBA_PY' for All NBA in the Prior Year, and then use that data to get a fit

# first define a special function for manipulating the year column so we can find the prior year
# input string format is 20XX-20YY
def get_prior_season(current_year):
    split_result = current_year.split('-')
    starting_year = int(split_result[0])
    ending_year = int(split_result[1])

    prior_starting_year = starting_year - 1
    prior_ending_year = starting_year

    return(str(prior_starting_year) + "-" + str(prior_ending_year))

# We're going to iterate over the dataframe and collect an array, one element for each row, that contains a 0 or a 1 based on if that current player-year was All NBA in the prior year
# After collecting that array, we'll create a new column in the dataframe and set it equal to that

# first create the array so we can append to it.
all_nba_py_array = []

for index, row in all_player_data_df.iterrows():
    if(index != len(all_nba_py_array)):
        print("Index where divergence happened: " + str(index))
        exit

    if(row['YEAR'] != "2013-2014"):
        prior_season = get_prior_season(row['YEAR'])
        #print("Prior season: " + str(prior_season))
        prior_season_rows = all_player_data_df.loc[((all_player_data_df['YEAR'] == prior_season) & (all_player_data_df['NAME'] == row['NAME']))]
        # if the returned dataframe is empty, we couldn't find that player in the previous year
        if(prior_season_rows.empty):
            all_nba_py_array.append(0)
            next
        elif(len(prior_season_rows) > 1):
            # somehow we matched more than one row.. should be unique.  No idea what is going on here.  Assume the player was not all nba in a previous year
            all_nba_py_array.append(0)
            next            
        else:
            # because the loc function returned a dataframe but we know it has one row, loop through it to get at the elements.
            for season_index, prior_season_row in prior_season_rows.iterrows():
                if(prior_season_row['ALL_NBA']):
                    all_nba_py_array.append(1)
                else:
                    all_nba_py_array.append(0)

                #print("Was " + str(prior_season_row['NAME'])) + " an all NBA player in season " + str(prior_season_row['YEAR']) + "?  Answer: " + str(prior_season_row['ALL_NBA'])

    else:
        # if we're looking at data from year 2013-2014, there is no way to calculate it because we don't have prior year data, so set it equal to 0 and go to the next row
        all_nba_py_array.append(0)
        next

all_nba_py_array

# Put new column into dataframe
all_player_data_df['ALL_NBA_PY'] = all_nba_py_array

all_player_data_df.to_csv('All_Player_Stats_All_Years_With_Prior_Year.csv', index = False)