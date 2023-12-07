#!/usr/bin/python3

"""Converts a csv of addresses to written envelope addresses."""

import argparse
import csv
from functools import partial
import io
from typing import Optional

# _REQUIRED_FIELDS = (name, city, state, zipcode)
_OPTIONAL_FIELDS = ("guest1", "guest2", "guest3", "guest4", "street1", "street2")


def write_optional_field_as_line(
    column_positions: dict[str, Optional[int]],
    output_file: io.TextIOWrapper,
    row: dict,
    field_name: str,
) -> None:
    """If a field exists, writes it as a single line in the output."""
    if field_name in column_positions:
        field_value = row[column_positions[field_name]]
        if field_value:
            output_file.write(field_value + "\n")


def parse_args():
    """Creates an argument parser for the cli."""
    parser = argparse.ArgumentParser(
        "wedding_addresses_from_csv",
        "Takes in a csv file for a list of addresses and creates a txt file with"
        + "those addresses in envelope format.",
        "See README.md for more usage information.",
    )
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", default="./envelope_addresses.txt")
    return parser.parse_args()


def parse_column_positions(title_row):
    """Determine column positions by iterating through the title row."""
    column_positions = {}
    for i, header in enumerate(title_row):
        column_positions[header] = i
    return column_positions


def create_envelope_addresses_from_csv(args):
    """Reads in a csv input and writes a txt file in envelope format."""

    with open(args.input, newline="", encoding="UTF-8") as input_file, open(
        args.output, "w", encoding="UTF-8"
    ) as output:
        csvreader = csv.reader(input_file)
        column_positions = parse_column_positions(next(csvreader))

        # Write an address for each row of the csv.
        for row in csvreader:
            write_if_exists = partial(
                write_optional_field_as_line, column_positions, output, row
            )
            output.write(row[column_positions["name"]] + "\n")
            for optional_field in _OPTIONAL_FIELDS:
                write_if_exists(optional_field)

            city = row[column_positions["city"]]
            state = row[column_positions["state"]]
            zipcode = row[column_positions["zipcode"]]
            output.write(city + ", " + state + " " + zipcode)
            output.write("\n\n")


if __name__ == "__main__":
    parsed_args = parse_args()
    create_envelope_addresses_from_csv(parsed_args)
