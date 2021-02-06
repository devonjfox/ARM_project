def get_population(census_dataframe, state_name, year):
    """
    Get population value as int given a census dataframe a state and a year
    :rtype: int
    """
    population_by_state = census_dataframe.loc[state_name]
    population_by_year = population_by_state.loc[year]
    return int(population_by_year.replace(',', ''))


def get_client_records_by_state(df, state):
    return df.loc[df['STATEFIP'] == int(state)]
