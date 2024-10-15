import pandas as pd
from datetime import datetime

def process_data(data):
    currency_code_mapping = {
        "US DOLLARS": "USD",
        "EURO": "EUR",
        "STERLING POUNDS": "GBP",
        "JAPANESE YEN": "JPY",
        "SINGAPORE DOLLARS": "SGD",
        "AUSTRALIAN DOLLARS": "AUD",
        "SWISS FRANCS": "CHF",
        "KUWAITI DINARS": "KWD",
        "OMANI RIYALS": "OMR",
        "SAUDI ARABIAN RIYALS": "SAR",
        "UAE DIRHAMS": "AED",
        "QATAR RIYALS": "QAR",
        "JORDANIAN DINARS": "JOD",
        "BAHRAIN DINARS": "BHD",
        "INDIAN RUPEES": "INR",
        "CANADIAN DOLLAR": "CAD",
        "NEW ZEALAND DOLLARS": "NZD"
    }
    
    new_column_names = [
        "Currency", 
        "Currency Buying Rate", 
        "Currency Selling Rate", 
        "Cheques Buying Rate", 
        "Cheques Selling Rate", 
        "Telegraphic Buying Rate", 
        "Telegraphic Selling Rate",
    ]
    
    # Ensure all rows have the same number of columns
    max_columns = max(len(row) for row in data)
    data = [row + [''] * (max_columns - len(row)) for row in data]
    
    # Insert column names as the first row
    data.insert(0, new_column_names)
    
    # Create a DataFrame
    df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(columns=new_column_names)
    
    # Get the current date and time
    now = datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M:%S')
    
    # Add the columns
    df['Date'] = current_date
    df['Time'] = current_time
    df['Bank'] = 'Commercial'
    df['ST BANK CODE'] = '7056'
    
    # Remove commas and handle '-' in numeric columns
    numeric_columns = [
        "Currency Buying Rate", 
        "Currency Selling Rate", 
        "Cheques Buying Rate", 
        "Cheques Selling Rate", 
        "Telegraphic Buying Rate", 
        "Telegraphic Selling Rate",
    ]
    
    for col in numeric_columns:
        df[col] = df[col].str.replace(',', '').replace('-', '0')
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Map currency codes
    df['Code'] = df['Currency'].str.upper().map(currency_code_mapping)
    
    return df
