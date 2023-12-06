#!/usr/bin/python3

import argparse
import csv
from functools import partial

def write_optional_field_as_line(column_positions, output, row, field_name):
    if (column_positions[field_name]):
        field = row[column_positions[field_name]]
        if (field):
            output.write(field + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "wedding_addresses_from_csv",
        "Takes in a csv file for a list of addresses and creates a txt file with those addresses in envelope format.",
        "See README.md for more usage information.")
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    column_positions = {
        "name": None,
        "guest1": None,
        "guest2": None,
        "guest3": None,
        "guest4": None,
        "street1": None,
        "street2": None,
        "city": None,
        "state": None,
        "zipcode": None,
    }

    with open(args.input, newline="") as input, open(args.output, "w", newline="") as output:
        csvreader = csv.reader(input)
        title = True
        for row in csvreader:
            if title:
                for i, header in enumerate(row):
                    column_positions[header] = i
                title = False
                print(column_positions)
            else:
                write_if_exists = partial(write_optional_field_as_line,column_positions, output, row)
                output.write(row[column_positions["name"]] + "\n")
                write_if_exists("guest1")
                write_if_exists("guest2")
                write_if_exists("guest3")
                write_if_exists("guest4")
                write_if_exists("street1")
                write_if_exists("street2")

                city = row[column_positions["city"]]
                state = row[column_positions["state"]]
                zip = row[column_positions["zipcode"]]
                output.write(city + ", " + state + " " + zip)
                output.write("\n\n")
