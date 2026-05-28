from bronze_to_silver import*
from silver_to_gold import*
from upload_to_blob import*


# Bronze → Silver
clean_claims()
clean_payments()
clean_binders()
clean_bordereaux()
clean_coverholders()
clean_policy()
clean_tpas()

# Silver → Gold
generate_claims_kpis()

# Upload to Azure
upload_files()

print("Pipeline completed successfully")