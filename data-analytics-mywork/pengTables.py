import nbformat
import pandas as pd

def extract_tables(penguins):
    # Load the notebook
    with open('penguins.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Iterate through each cell in the notebook
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # Check if the code cell outputs a DataFrame (table)
            if 'outputs' in cell:
                for output in cell['outputs']:
                    if 'data' in output and 'text/html' in output['data']:
                        # Extract table from HTML output
                        html_table = output['data']['text/html']
                        # Convert HTML table to DataFrame
                        tables = pd.read_html(html_table)
                        for idx, table in enumerate(tables):
                            # Export each DataFrame to Excel
                            table.to_excel(f'table_{idx}.xlsx', index=False)

extract_tables('penguins.ipynb')