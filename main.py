import pandas as pd
import termcolor 

df_capitals = pd.DataFrame([['England', 'London'], ['Austria','Vienna'],['France','Paris'],['Italy','Rome'],['Germany','Berlin'],['Switzerland','Bern'],['Belgium','Brussels']], columns=['Country', 'Capital '])

df_capitals.to_csv(r"C:\Sharing\Capitals.csv")