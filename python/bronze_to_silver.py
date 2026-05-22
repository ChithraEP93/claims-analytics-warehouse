import pandas as pd

#claims file
def clean_claims():
    #Read raw clims data
    df=pd.read_csv("data/sample_claims.csv")

    #Remove Duplicates
    df=df.drop_duplicates()

    #Convert date columns
    df["claim_date"]=pd.to_datetime(df["claim_date"])
    df["reported_date"]=pd.to_datetime(df["reported_date"])
    df["settled_date"]=pd.to_datetime(df["settled_date"])

    #Remove invalid claim amounts
    df=df[df["claim_amount"]>0]

    #Fill missing settlement amounts
    df["settlement_amount"]=df["settlement_amount"].fillna(0)

    #save cleaned file
    df.to_csv("data/silver/cleaned_claims.csv",index=False)

    print("Claims cleaned sucessfully")
    print(df.head())
    print(df["claim_amount"].sum())

#payments file

def clean_payments():
    #Read payments data
    df=pd.read_csv("data/sample_payments.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #Convert  date
    df["payment_date"]=pd.to_datetime(df["payment_date"])
    df["approval_date"]=pd.to_datetime(df["approval_date"])

    #Remove invalid payments
    df=df[df["payment_amount"]>0]


    # Fill missing settlement percentages
    df["settlement_percentage"] = df["settlement_percentage"].fillna(0)

    #Save cleaned payments
    df.to_csv("data/silver/cleaned_payments.csv",index=False)
    print("Payments cleaned successfully")

def clean_binders():

    #Read binders data
    df=pd.read_csv("data/sample_binders.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #convert dates
    df["effective_date"]=pd.to_datetime(df["effective_date"])
    df["expiry_date"]=pd.to_datetime(df["expiry_date"])

    # Remove invalid authorization limits
    df = df[df["authorization_limit"] > 0]

    # Remove invalid quota share percentages
    df = df[
        (df["quota_share_percent"] >= 0) &
        (df["quota_share_percent"] <= 100)
    ]

    # Save cleaned binders
    df.to_csv("data/silver/cleaned_binders.csv", index=False)

    print("Binders cleaned successfully")

def clean_bordereaux():
    #Read bordereaux file
    df=pd.read_csv("data/sample_bordereaux.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #convert dates
    df["period_start"]=pd.to_datetime(df["period_start"])
    df["period_end"]=pd.to_datetime(df["period_end"])
    df["submission_date"]=pd.to_datetime(df["submission_date"])

      # Remove invalid bordereaux amounts
    df=df[df["bordereaux_amount"]>0]  

    # Remove invalid claim counts
    df = df[df["number_of_claims"] >= 0]

    # Standardize submission status
    df["submission_status"] = df["submission_status"].str.title()

    # Save cleaned bordereaux
    df.to_csv("data/silver/cleaned_bordereaux.csv", index=False)

    print("Bordereaux cleaned successfully") 


def clean_coverholders():
    #Read coverholder data
    df=pd.read_csv("data/sample_coverholders.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #convert dates
    df["join_date"]=pd.to_datetime(df["join_date"])

    #remove records with annual premium zero
    df=df[df["annual_premium"]>0]

    #standardise the coverholder type
    df["coverholder_type"]=df["coverholder_type"].str.title()

    # Standardize risk rating
    df["risk_rating"] = df["risk_rating"].str.title()

    # Save cleaned coverholders
    df.to_csv("data/silver/cleaned_coverholders.csv", index=False)

    print("Coverholders cleaned successfully")

def clean_policy():
    #Read coverholder data
    df=pd.read_csv("data/sample_policies.csv")

    #Remove duplicates
    df=df.drop_duplicates()

    #convert dates
    df["inception_date"]=pd.to_datetime(df["inception_date"])
    df["expiry_date"]=pd.to_datetime(df["expiry_date"])

    #remove records with coverage limit and annual limit zero
    df=df[df["coverage_limit"]>0]
    df = df[df["annual_premium"] > 0]

    #standardise the policy status
    df["policy_status"]=df["policy_status"].str.title()

    # Standardize policy type
    df["policy_type"] = df["policy_type"].str.title()

    # Save cleaned policy
    df.to_csv("data/silver/cleaned_policies.csv", index=False)

    print("Policy file cleaned successfully")

def clean_tpas():
    #Read tpas data
    df=pd.read_csv("data/sample_tpas.csv")

    #Remove duplicates
    df=df.drop_duplicates()

      #standardise the tpa name
    df["tpa_name"]=df["tpa_name"].str.title()

    # Standardize tpa type and specialization
    df["tpa_type"] = df["tpa_type"].str.title()
    df["specialization"] = df["specialization"].str.title()
     #remove extra spaces
    df=df.apply(lambda x:x.str.strip() if x.dtype=="object" else x)

    # Save cleaned tpas
    df.to_csv("data/silver/cleaned_tpas.csv", index=False)
    print("tpas file cleaned successfully")

   

clean_claims()
clean_payments()
clean_binders()
clean_bordereaux()
clean_coverholders()
clean_policy()
clean_tpas()