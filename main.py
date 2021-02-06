import pandas


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
    total = total_records(depression_in_state)
    print("Calculating rates of depression...")
    return rate_of_occurrence(total=total, population=population)


def total_records(dataframe):
    return len(dataframe.index)


def rate_of_occurrence(total, population):
    return (total / population) * 100


if __name__ == '__main__':
    csv = "MHCLD_PUF_2018.csv"
    df = pandas.read_csv(csv)
    csv2 = "Census.csv"
    df2 = pandas.read_csv(csv2, index_col=0)

    # rate_of_depression = depression_rate(df2, '.Oregon', '2018', df, 41)
    # print("Rate of Depression: " + str(rate_of_depression))

    list_of_states = {'.Oregon': 41, '.Alabama': 1, '.Arizona': 4, '.California': 6}

    for state, state_code in list_of_states.items():
        rate_of_depression = depression_rate(df2, state, '2018', df, state_code)
        print("Rate of Depression in " + state + ": " + str(rate_of_depression) + "\n")

#     np_array = df.to_numpy()
#     #SE_mean = numpy.std(np_array, ddof = 1) / numpy.sqrt(numpy.size(np_array))
#     #print(SE_mean)
#     # outpatient = df.loc[df['OPISERVICE'] == 2]
#     Trauma = df.loc[df['MH1'] == 1]
#     Depression = df.loc[df['MH1'] == 7]
#     No_depression = df.loc[df['MH1'] != 7]
#     Trauma_depression = Trauma.loc[Trauma['MH2'] == 7]
#     print("Trauma: ", (len(Trauma.index)))
#     print(Trauma)
#     print("Depression: ", (len(Depression.index)))
#     print("No_depression: ", (len(No_depression.index)))
#     print("Trauma_depression: ", (len(Trauma_depression.index)))
# # Do we need to see depression/trauma in MH1, MH2 and MH3 to find odds?
# # Calculate odds of exposure (trauma) and having depression (outcome)
# # Odds for depression in total population = Those with depression/Those without depression
#     Odds_depression = (len(Depression.index))/(len(No_depression.index))
#     print("Odds_depression: ", (Odds_depression))
# # Odds for depression with trauma = those with depression and trauma/those with trauma
#     Odds_depression_trauma = (len(Trauma_depression.index))/(len(Trauma.index))
#     print("Odds_depression_trauma: ", (Odds_depression_trauma))
# # Odds Ratio for exposure (trauma) = odds of depression with trauma/odds of depression
#     Odds_ratio_depression_trauma = Odds_depression_trauma/Odds_depression
#     print("Odds_ratio_depression_trauma: ", (Odds_ratio_depression_trauma))
# # Eq 1 = Risk of depression with exposure (trauma) = Those with depression/All those with trauma
#     Risk_depression_trauma = (len(Trauma_depression.index))/(len(Trauma.index))
#     print("Risk_depression_trauma: ", (Risk_depression_trauma))
# # Eq 2 = Risk of depression in population = Those with depression/total sample
#     Risk_depression = (len(Depression.index))/(len(df.index))
#     print("Risk_depression: ", (Risk_depression))
# # Relative risk = Eq 1/Eq 2
#     Relative_risk = Risk_depression_trauma/Risk_depression
#     print("Relative_risk: ", (Relative_risk))
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
