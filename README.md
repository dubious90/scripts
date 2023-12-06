# scripts

A dropping point for scripts that I use to solve quick problems.

## wedding_addresses_from_csv

A quick script I wrote to create envelope format addresses (.txt) from a csv. To use, enter a command like:

```
./wedding_addresses_from_csv.py --input input.csv --output output.csv
```

The program requires a title row, and for that title row to be conformed to the names listed below.
Your columns may be in any order, and the program uses the title row to determine that order. Any
columns you include that do not match these header names will be omitted from the end result. Headers
with an * are considered optional.

```
name
street1
city
state
zipcode
street2*
guest1*
guest2*
guest3*
guest4*
```
