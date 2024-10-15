import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "currency": row['Currency'],
            "code": row['Code'],
            "currency_buying_rate": float(row['Currency Buying Rate']) if row['Currency Buying Rate'] else None,
            "currency_selling_rate": float(row['Currency Selling Rate']) if row['Currency Selling Rate'] else None,
            "cheques_buying_rate": float(row['Cheques Buying Rate']) if row['Cheques Buying Rate'] else None,
            "cheques_selling_rate": float(row['Cheques Selling Rate']) if row['Cheques Selling Rate'] else None,
            "telegraphic_buying_rate": float(row['Telegraphic Buying Rate']) if row['Telegraphic Buying Rate'] else None,
            "telegraphic_selling_rate": float(row['Telegraphic Selling Rate']) if row['Telegraphic Selling Rate'] else None,
            "bank": row['Bank'],
            "st_bank_code": row['ST BANK CODE']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents