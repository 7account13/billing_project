import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('km.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()



# SQL command to create the 'products' table
create_invoices_table_query = '''
CREATE TABLE IF NOT EXISTS invoices (
    invoice_num  INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_date 
    name TEXT NOT NULL,
    billing_address TEXT NOT NULL,
    shipping_address TEXT NOT NULL,
    gst TEXT NOT NULL,
    selling_price REAL NOT NULL,
    intra_state_tax_rate REAL NOT NULL,
    inter_state_tax_rate REAL NOT NULL
)
'''

# Execute the SQL command for the 'products' table
cursor.execute(create_invoices_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("invoices table  created successfully.")
