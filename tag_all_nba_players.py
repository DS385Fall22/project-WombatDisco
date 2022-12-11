import csv

# builds a dictionary with key = season (2013-2014, etc), value = array of names of all nba players
def build_all_nba_dict():
    all_nba_fn = 'All-NBA_Players_2013-2022.csv'

    fh_in = open(all_nba_fn)

    csv_file_data = csv.DictReader(fh_in)

    # declare all_nba_dict to return to caller
    all_nba_dict = {}

    for row in csv_file_data:
        if(all_nba_dict.get(row['SEASON']) == None):
            # Declare array to use as value for that season
            all_nba_dict[row['SEASON']] = []

        # Append current name to list of all nba player names for that season
        all_nba_dict[row['SEASON']].append(row['NAME'])
    
    fh_in.close()

    return(all_nba_dict)

def pymain():
    # define fields for output file.  Use this variable rather than dynamically generating so we can get a predictable output column order
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
    # filenames to process
    filenames = [
        '2013-2014_Player_Stats_Clean.csv',
        '2014-2015_Player_Stats_Clean.csv',
        '2015-2016_Player_Stats_Clean.csv',
        '2016-2017_Player_Stats_Clean.csv',
        '2017-2018_Player_Stats_Clean.csv',
        '2018-2019_Player_Stats_Clean.csv',
        '2019-2020_Player_Stats_Clean.csv',
        '2020-2021_Player_Stats_Clean.csv',
        '2021-2022_Player_Stats_Clean.csv',
    ]

    all_nba_dict = build_all_nba_dict()

    # check to make sure it's loaded correctly.  debug code only.
    #for key,value in all_nba_dict.items():
    #    print(key)
    #    for item in value:
    #        print(item)

    for fn in filenames:
        # get season ID to use as lookup in all_nba dict
        season = fn.split('_')[0]
        
        # open a filehandle to the datafile
        fh_in = open(fn)
        # read in the CSV data
        csv_file_data = csv.DictReader(fh_in)

        output_fn = fn.split('.')[0] + "_All_NBA_Added." + fn.split('.')[1]
        print(output_fn)
        
        # Open the file, init the dict writer, and write out the header
        fn_out = open(output_fn, "w")
        csv_output_writer = csv.DictWriter(fn_out, fieldnames=fields)
        csv_output_writer.writeheader()

        # get the list of all nba players in the year we're currently processing
        current_year_all_nba_players = all_nba_dict[season]

        for row in csv_file_data:
            if(row['NAME'] in current_year_all_nba_players):
                # found that player in the list of all-nba players for that season, so flag it as True
                row['ALL_NBA'] = 1
            
            csv_output_writer.writerow(row)

        fn_out.close()

# start it up
pymain()