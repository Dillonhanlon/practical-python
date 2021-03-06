# fileparse.py
#
# Exercise 3.3 - 3.18

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',',Silence_errors=False):
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        
        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []


        records = []
        for rowno,row in enumerate(rows,1):
            if not row:    # Skip rows with no data
                continue

            if indices:
                row = [ row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not Silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
            if has_headers:
               record = dict(zip(headers,row))
            else: 
                record = tuple(row)

            records.append(record)

    return records
