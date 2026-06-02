# claims-analytics-warehouse

End-to-end insurance claims analytics platform built using Python, Azure Blob Storage, Power BI, and GitHub.

The project follows a Bronze-Silver-Gold architecture to transform raw insurance datasets into business-ready analytics outputs and interactive dashboards.

## Project Architecture

Raw Insurance Data
        ↓
Bronze Layer
        ↓
Python Data Cleaning & Validation
        ↓
Silver Layer
        ↓
KPI & Analytics Generation
        ↓
Gold Layer
        ↓
Azure Blob Storage
        ↓
Power BI Dashboard

## Technologies Used

- Python
- Pandas
- Azure Blob Storage
- Power BI
- Git & GitHub

## Gold Layer Outputs

- claims_kpis.csv
- claims_by_status.csv
- claims_by_risk_rating.csv
- claims_by_TPA.csv
- claims_by_claim_type.csv

## Dashboard Features

- Claims KPIs
- Claims by Status
- Claims by Risk Rating
- Claims by TPA
- Claims by Claim Type

## Future Enhancements

- Azure Data Factory orchestration
- Azure SQL Database integration
- Automated scheduling and monitoring
- CI/CD deployment pipeline

  ## Power BI Dashboard

![Claims Dashboard](images/dashboard.png)
