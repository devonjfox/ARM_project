import pandas
import os


def load_csv_into_dataframe(location_of_csv):
    return pandas.read_csv(location_of_csv)


def get_client_records_by_state(df, state):
    return df.loc[df['STATEFIP'] == int(state)]


def get_occurrences_of_depression_in_state(base_dataframe, state_code):
    state_df = get_client_records_by_state(base_dataframe, state_code)
    diagnosis_in_state = state_df[['MH1', 'MH2', 'MH3']].copy()
    # Get all occurances of depression code (7) in MH1, MH2 OR MH3
    depression_code = 7
    depression_in_state = diagnosis_in_state[
        (diagnosis_in_state['MH1'] == depression_code) | (diagnosis_in_state['MH2'] == depression_code) | (
                diagnosis_in_state['MH3'] == depression_code)]
    return depression_in_state


def get_population(census_dataframe, state_name, year):
    """
    Get population value as int given a census dataframe a state and a year
    :rtype: int
    """
    population_by_state = census_dataframe.loc[state_name]
    population_by_year = population_by_state.loc[year]
    return int(population_by_year.replace(',', ''))


def depression_rate(census_dataframe, state_name, year, basedataframe, state_code):
    population = get_population(census_dataframe, state_name, year)
    print("Population of the Census Dataframe: " + population.__str__())
    depression_in_state = get_occurrences_of_depression_in_state(basedataframe, state_code)
    print("Rates of Depression in " + state_name + "")
    total = len(depression_in_state.index)
    print("Calculating rates of depression...")
    return (total / population) * 100


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

    for flag in flags:
        diag_flg = flg_df[flg_df[flag] == 1]
        series = diag_flg['STATEFIP'].value_counts().sort_index()
        series.rename(flag, inplace=True)
        print(series)

    # Load the Census data into a dataframe
    census_csv = os.path.join(dirname, 'data/Census.csv')
    census = pandas.read_csv(census_csv, index_col=0)
    print(census.head())

    # Clean Census Dataframe
    # Filter 2018 Data
    census_2018 = census.loc[:, '2018']
    print(census_2018.head())
