import os

import pandas

if __name__ == '__main__':
    # Returns the absolute path for the current file location
    dirname = os.path.dirname(__file__)

    print("Load the MHCLD into a dataframe")
    mhcld_puf_2018_csv = os.path.join(dirname, 'data/MHCLD_PUF_2018.csv')
    mhcld = pandas.read_csv(mhcld_puf_2018_csv, index_col=39)
    print(mhcld.head())

    print("Clean MHCLD Dataframe")
    flg_df = mhcld.filter(regex="(.*FLG|STATEFIP)")
    print(flg_df.head())

    # Get the list of flags as a iterable to loop over it
    flags = flg_df.columns
    # Remove the Statefip from the list as we don't need to iterate over that
    flags = flags.drop("STATEFIP")

    diagnosis_by_state = {}
    for flag in flags:
        diag_flg = flg_df[flg_df[flag] == 1]
        series = diag_flg['STATEFIP'].value_counts().sort_index()
        series.rename(flag, inplace=True)
        diagnosis_by_state[series.name] = series

    # Create the dataframe from the collection of series
    # This is the numbers of occurrences of each FLG by state code
    diagnosis_by_state_dataframe = pandas.DataFrame(diagnosis_by_state)
    print(diagnosis_by_state_dataframe)

    # Load the Census data into a dataframe
    census_csv = os.path.join(dirname, 'data/Census.csv')
    census = pandas.read_csv(census_csv, index_col=0)

    # Clean Census Dataframe
    # Filter 2018 Data
    census_2018 = census.loc[:, '2018']
    print(census_2018)

    list_of_states = {'.Alabama': 1, '.Arizona': 4, '.California': 6, '.Colorado': 8, '.Connecticut': 9,
                      '.Delaware': 10, '.District of Columbia': 11, '.Florida': 12, '.Hawaii': 15, '.Idaho': 16,
                      '.Illinois': 17, '.Indiana': 18, '.Iowa': 19, '.Kentucky': 21, '.Louisiana': 22, '.Maryland': 24,
                      '.Massachusetts': 25, '.Michigan': 26, '.Minnesota': 27, '.Mississippi': 28, '.Missouri': 29,
                      '.Montana': 30, '.Nebraska': 31,
                      '.Nevada': 32, '.New Mexico': 35, '.New York': 36, '.North Carolina': 37, '.North Dakota': 38,
                      '.Ohio': 39, '.Oklahoma': 40, '.Oregon': 41, '.Pennsylvania': 42, '.Rhode Island': 44,
                      '.South Carolina': 45,
                      '.South Dakota': 46, '.Tennessee': 47, '.Texas': 48, '.Utah': 49, '.Vermont': 50, '.Virginia': 51,
                      '.Washington': 53, '.West Virginia': 54, '.Wisconsin': 55, '.Wyoming': 56}

    for name, code in list_of_states.items():
        print(code)
        print(name)
        diagnosis_by_state_dataframe.iloc[code].apply(lambda x, y: x / y, args=(code,))

    print(diagnosis_by_state_dataframe)
