import numpy as np
import pandas as pd 


def delete_hard(df):
    new_df=df[df['constraint_type']!="HARD"]
    new_df.drop('constraint_type',axis=1,inplace=True)
    new_df=new_df.reset_index(drop=True)
    return new_df

