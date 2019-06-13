# flip-json-flop
Turns CSV, XLX, and XLSX files into JSON format. Is meant for easy command line usage.

## Usage
`python flip-json-flop.py <INPUT.csv/xlsx/xls> <OUTPUT.json>`
## Necessary installations
Because this is achieved by first turning the CSV, XLSX, and XLSM files into pandas DataFrames, you may need to install pandas first:
`pip install pandas` 
 
Below are some ways of testing out the JSON conversions:
https://json-csv.com/ (for .csv)
http://www.json-xls.com/json2xls (for .xls + .xlsx). Use Plain+Hierarchy when rendering.
