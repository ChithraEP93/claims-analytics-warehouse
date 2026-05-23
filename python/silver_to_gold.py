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

generate_claims_kpis()