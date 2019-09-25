# Date: JUN 13 2019
''' Cleans csv, xlx, and xlsx files and turns them into json files through pandas.'''
import pandas as pd
import sys
# Checks for correct arguments.
if len(sys.argv) != 3:
    print("Error! Usage: flip_json_flop.py <input file.csv/xls/xlms> <output file.json>")
    exit(1)

# Checks file extension.
file_extension = sys.argv[1].split(".")[-1]
if file_extension != 'csv' and file_extension != 'xls' and file_extension != 'xlms' and file_extension != 'xlsx':
    print("Error! Unknown format. Please provide .csv, .xls, or .xlms input.")
    exit(1)


# Converts from csv
def convert_csv(input_file, output_file):
    csv_file = pd.DataFrame(pd.read_csv(input_file, sep=",", header=0, index_col=False))
    csv_file.to_json(output_file, orient="records", date_format="epoch", double_precision=10,
                     force_ascii=True, date_unit="ms", default_handler=None)


# Converts from xls, xlsm, and xlsx.
def convert_xls_xlsx(input_file, output_file):
    excel_file = pd.DataFrame(pd.read_excel(input_file, header=0))
    excel_file.to_json(output_file, orient="records", date_format="epoch", double_precision=10,
                       force_ascii=True, date_unit="ms", default_handler=None)


if file_extension == 'csv':
    convert_csv(sys.argv[1], sys.argv[2])
elif file_extension == 'xls' or file_extension == 'xlsx' or file_extension == 'xlms':
    convert_xls_xlsx(sys.argv[1], sys.argv[2])
