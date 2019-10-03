import pandas as pd


df = pd.read_csv("a.csv")



df.sort_values('ID', ascending=True, inplace=True)


# output duplicates to a file for further analysis
df_dups = df[df.duplicated(keep='first')]
df_dups.to_csv("a2.csv")


df.drop_duplicates(subset='ID', keep='first', inplace=True)


df2 = pd.read_csv("b.csv")


df_join_left = pd.merge(df, df2, how="left", on=['ID'])


df_join_left.drop(['Full_Name'], axis=1, inplace=True)
df_join_left.drop(['City_y'], axis=1, inplace=True)

df_join_left.to_csv("c.csv")

