import pandas


def load_csv_into_dataframe(location_of_csv):
    return pandas.read_csv(location_of_csv)



if __name__ == '__main__':
    df = load_csv_into_dataframe("MHCLD_PUF_2018.csv")


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
