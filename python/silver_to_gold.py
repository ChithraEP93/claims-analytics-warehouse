import pandas as pd

def generate_claims_kpis():

    #Read cleaned claims data
    df=pd.read_csv("data/silver/cleaned_claims.csv")

    #KPI calculations

    total_claims=len(df)

    total_claim_amount=df["claim_amount"].sum()
    average_claim_amount=df["claim_amount"].mean()

    settled_claims=len(df[df["claim_status"]=="Settled"])

    open_claims=len(df[df["claim_status"]=="Open"])

    # create KPI dataframe
    kpi_df=pd.DataFrame({
        "metric": [
            "Total Claims",
            "Total Claim Amount",
            "Average Claim Amount",
            "Settled Claims",
            "Open Claims"],
        "value":[
            total_claims,
            total_claim_amount,
            average_claim_amount,
            settled_claims,
            open_claims
        ] 
    })
#Save gold layer
    kpi_df.to_csv("data/gold/claims_kpis.csv",index=False)
    print("Claims by kpi created")


def generate_claims_by_status():

    #Read Cleaned claims
    df=pd.read_csv(
         "data/silver/cleaned_claims.csv"
    )
    #Group by claim status
    status_df = (
        df.groupby("claim_status")
        ["claim_amount"]
        .agg(["count","sum","mean"])
        .reset_index()
    )
    status_df.columns=["claim_status","total_claims",
    "total_claim_amount",
    "average_claim_amount"]
    #save gold file
    status_df.to_csv("data/gold/claims_by_status",index=False)
    print("Claims by status created")


def generate_claims_by_risk_rating():
    #Read cleaned claims
    cl_df=pd.read_csv("data/silver/cleaned_claims.csv")
    #Read cleaned coberholders
    cv_df=pd.read_csv("data/silver/cleaned_coverholders.csv")


    #merge 
    merged_df=cl_df.merge(cv_df,on="coverholder_id")

    #Group By Coverholder's risk rating
    risk_df=(
        merged_df.groupby("risk_rating")
        ["claim_amount"].agg(["count","sum","mean"])
        .reset_index())
    
    risk_df.columns=["risk_rating",
    "total_claims",
    "total_claim_amount",
    "average_claim_amount"]
    
    #save file
    risk_df.to_csv("data/gold/claims_by_Risk.csv",index=False)
    print("Claims by risk rating created")

generate_claims_kpis()
generate_claims_by_status()
generate_claims_by_risk_rating()