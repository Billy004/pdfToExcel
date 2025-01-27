import tabula
from openpyxl import Workbook
import pandas as pd

def extract_tables_from_pdf(pdf_path, excel_path):
    print(f"Extracting tables from {pdf_path}")
    
    # Extract tables from PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    print(f"Found {len(tables)} tables")

    # Create Excel writer
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for i, table in enumerate(tables, start=1):
            print(f"Processing table {i}")
            table.to_excel(writer, sheet_name=f"Table {i}", index=False)
    
    print(f"Tables saved to {excel_path}")

# Example usage
pdf_file = "/Users/zaba/Desktop/Billy Mac Data/projects/pdfToExcel/sample_table.pdf"  # Replace with your PDF file path
excel_file = "/Users/zaba/Desktop/Billy Mac Data/projects/pdfToExcel/output_tables.xlsx"

extract_tables_from_pdf(pdf_file, excel_file)