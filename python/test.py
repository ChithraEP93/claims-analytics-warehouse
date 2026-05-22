import pandas as pd

def clean_coverholders():
    #Read coverholder data
    df=pd.read_csv("data/sample_coverholders.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #convert dates
    df["join_date"]=pd.to_datetime(df["join_date"])

    #remove records with annual premium zero
    df=df[df["annual_premium"]>0]

    df["coverholder_type"]=df["coverholder_type"].str.title()


clean_coverholders()