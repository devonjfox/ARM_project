from Population import get_population, get_client_records_by_state


def get_occurrences_of_depression_in_state(base_dataframe, state_code):
    state_df = get_client_records_by_state(base_dataframe, state_code)
    diagnosis_in_state = state_df[['MH1', 'MH2', 'MH3']].copy()
    # Get all occurances of depression code (7) in MH1, MH2 OR MH3
    depression_code = 7
    depression_in_state = diagnosis_in_state[
        (diagnosis_in_state['MH1'] == depression_code) | (diagnosis_in_state['MH2'] == depression_code) | (
                diagnosis_in_state['MH3'] == depression_code)]
    return depression_in_state


def depression_rate(census_dataframe, state_name, year, basedataframe, state_code):
    population = get_population(census_dataframe, state_name, year)
    print("Population of the Census Dataframe for " + state_name.replace('.', '')
          + " " + year + ": " + population.__str__())
    depression_in_state = get_occurrences_of_depression_in_state(basedataframe, state_code)
    print("Rates of Depression in " + state_name.replace('.', '') + "")
    total = len(depression_in_state.index)
    print("Calculating rates of depression...")
    return (total / population) * 100
