import csv
from collections import defaultdict

def pymain():
    # filenames to process
    files = [
        '2013-2014_Player_Stats.csv',
        '2014-2015_Player_Stats.csv',
        '2015-2016_Player_Stats.csv',
        '2016-2017_Player_Stats.csv',
        '2017-2018_Player_Stats.csv',
        '2018-2019_Player_Stats.csv',
        '2019-2020_Player_Stats.csv',
        '2020-2021_Player_Stats.csv',
        '2021-2022_Player_Stats.csv',
    ]
    # csv fields to consider
    fields = [
        'NAME',
        'POS',
        'AGE',
        'GP',
        'MPG',
        'MIN',
        'USG',
        'TOr',  # don't use this
        'FTA',
        'FTP',
        '2PA',
        '2PP',
        '3PA',
        '3PP',
        'TS',
        'PPG',
        'RPG',
        'TRB',
        'APG',
        'AST',
        'SPG',
        'BPG',
        'VI',
        'ALL_NBA',
    ]

    # for each filename
    for input_fn in files:
        # open a filehandle to the datafile
        fh_in = open(input_fn)
        # read in the CSV data
        csv_file_data = csv.DictReader(fh_in)
        # declare a dict of dicts to hold player stats with format
            # key - Player Name, value -  dictionary with keys for each entry in the 'fields' variable, minus NAME, and value of each being the associated stat for that player in that season
        calc_dict = {}
        print("Loading filename: " + input_fn)
        # loop through each row
        for row in csv_file_data:
            # if playername is not found as a key, build dict of player stats for that season and add key of playername with value of the dict just created
            if(calc_dict.get(row['NAME']) == None):
                # fix up the ALL_NBA column with a 0
                row['ALL_NBA'] = 0
                # this player was not found, so create a new dictionary entry with key = player name and value being the row of data loaded from the CSV file
                calc_dict[row['NAME']] = row
            else:
                # It looks like we have a player who was already processed, so let's process each field as appropriate and make a new dictionary with the calculated values
                # Most of the time this is going to be a weighted average with weights being games played
                
                # grab our weights to simplify calculation syntax below.  Cast to float for upcoming division
                w1 = float(calc_dict[row['NAME']]['GP'])
                w2 = float(row['GP'])
                wtotal = w1 + w2

                # declare new dictionary and calculate each value as appropriate.  Most are just weighted averages.
                new_row = {
                    'NAME': row['NAME'],
                    'POS': row['POS'],
                    'AGE': float(row['AGE']),
                    'GP': int(calc_dict[row['NAME']]['GP']) + int(row['GP']),
                    'MPG': round((w1 * float(calc_dict[row['NAME']]['MPG']) + w2 * float(row['MPG'])) / wtotal, 1), 
                    'MIN': round((w1 * float(calc_dict[row['NAME']]['MIN']) + w2 * float(row['MIN'])) / wtotal, 1),
                    'USG': round((w1 * float(calc_dict[row['NAME']]['USG']) + w2 * float(row['USG'])) / wtotal, 1),
                    'TOr': round((w1 * float(calc_dict[row['NAME']]['TOr']) + w2 * float(row['TOr'])) / wtotal, 3),
                    'FTA': int(calc_dict[row['NAME']]['FTA']) + int(row['FTA']),
                    'FTP': round((w1 * float(calc_dict[row['NAME']]['FTP']) + w2 * float(row['FTP'])) / wtotal, 3),
                    '2PA': int(calc_dict[row['NAME']]['2PA']) + int(row['2PA']),
                    '2PP': round((w1 * float(calc_dict[row['NAME']]['2PP']) + w2 * float(row['2PP'])) / wtotal, 3),
                    '3PA': int(calc_dict[row['NAME']]['3PA']) + int(row['3PA']),
                    '3PP': round((w1 * float(calc_dict[row['NAME']]['3PP']) + w2 * float(row['3PP'])) / wtotal, 3),
                    'TS': round((w1 * float(calc_dict[row['NAME']]['TS']) + w2 * float(row['TS'])) / wtotal, 3),
                    'PPG': round((w1 * float(calc_dict[row['NAME']]['PPG']) + w2 * float(row['PPG'])) / wtotal, 1),
                    'RPG': round((w1 * float(calc_dict[row['NAME']]['RPG']) + w2 * float(row['RPG'])) / wtotal, 1),
                    'TRB': round((w1 * float(calc_dict[row['NAME']]['TRB']) + w2 * float(row['TRB'])) / wtotal, 1),
                    'APG': round((w1 * float(calc_dict[row['NAME']]['APG']) + w2 * float(row['APG'])) / wtotal, 1),
                    'AST': round((w1 * float(calc_dict[row['NAME']]['AST']) + w2 * float(row['AST'])) / wtotal, 1),
                    'SPG': round((w1 * float(calc_dict[row['NAME']]['SPG']) + w2 * float(row['SPG'])) / wtotal, 2),
                    'BPG': round((w1 * float(calc_dict[row['NAME']]['BPG']) + w2 * float(row['BPG'])) / wtotal, 2),
                    'VI': round((w1 * float(calc_dict[row['NAME']]['VI']) + w2 * float(row['VI'])) / wtotal, 1),
                    'ALL_NBA': 0
                }

                # Take our newly calculated values and overwrite the old entry
                calc_dict[row['NAME']] = new_row

        # close the read filehande
        fh_in.close()

        print(calc_dict)

        # now write the output to a new CSV file
        splitname = input_fn.split('.')
        output_fn = splitname[0] + '_Clean.csv'
        #print(output_fn)
        
        # Open the file an init the dict writer
        fn_out = open(output_fn, "w")
        csv_output_writer = csv.DictWriter(fn_out, fieldnames=fields)
        
        # write out the header values
        csv_output_writer.writeheader()
        for key in calc_dict.keys():
            csv_output_writer.writerow(calc_dict[key])
        
        fn_out.close()

# start the party
pymain()