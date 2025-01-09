import os

# CSV data saving path
URL = "https://www.combank.lk/rates-tariff#exchange-rates"
OUTPUT_CSV = os.path.join("data", "csv", "commercial_bank_exchange_rates.csv")
Basefile_name="Commercial_exchange_rates"

# SQL connection string
# CONNECTION_STRING = 'mssql://BGL-DTS33\\MSSQLSERVER1/mydb?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'
# Commercial bank exchange rate url
container_name_for_reference_backups = 'bank-exchange-rates-reference-backups'
backup_base_filename = 'Commercial'
backup_pairs_to_keep = 28
