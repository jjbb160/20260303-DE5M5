import pandas as pd

# Define functions ready for cleaning
def replace_speechmarks(df, column_name):
    df[column_name] = df[column_name].str.replace('"','',regex=False)
    return df
    
def column_value_to_14(df, column_name):
    df[column_name] = 14
    return df

def books_ID_nulls(df, column_name):
    df = df.dropna(subset=[column_name])
    return df

def customers_ID_nulls(df, column_name):
    df = df.dropna(subset=[column_name])
    return df

def books_Customer_nulls(df, column_name):
    df = df.dropna(subset=[column_name])
    return df

def books_ID_Int(df, column_name):
    df[column_name] = df[column_name].astype(int)
    return df

def books_Customer_Int(df, column_name):
    df[column_name] = df[column_name].astype(int)
    return df

def customers_Customer_Int(df, column_name):
    df[column_name] = df[column_name].astype(int)
    return df

def books_incorrect_date_checkout(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name],dayfirst=True,errors='coerce')
    return df

def books_incorrect_date_returned(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name],dayfirst=True,errors='coerce')
    return df

def books_total_days(df):
    df['Total Days'] = (df['Book Returned'] - df['Book checkout']).dt.days
    return df

# Import raw data
books = pd.read_csv(r"C:\Users\Admin\Desktop\20260303-DE5M5\data\03_Library Systembook.csv")
customers = pd.read_csv(r"C:\Users\Admin\Desktop\20260303-DE5M5\data\03_Library SystemCustomers.csv")

# Call functions to clean data
books = replace_speechmarks(books, 'Book checkout')
books = column_value_to_14(books, 'Days allowed to borrow')
books = books_ID_nulls(books, 'Id')
books = books_Customer_nulls(books, 'Customer ID')
books = books_ID_Int(books, 'Id')
books = books_Customer_Int(books, 'Customer ID')
customers = customers_ID_nulls(customers, 'Customer ID')
customers = customers_Customer_Int(customers, 'Customer ID')
books = books_incorrect_date_checkout(books, 'Book checkout')
books = books_incorrect_date_returned(books, 'Book Returned')
books = books_total_days(books)

# Export Results to Output
books.to_csv('outputs/books.csv',index=False)
customers.to_csv('outputs/customers.csv',index=False)

    