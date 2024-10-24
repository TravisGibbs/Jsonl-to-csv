import script
import argparse

parser = argparse.ArgumentParser(
    description='Queries Aeroleads for people in a project and propagates new external profiles.'
)

parser.add_argument(
    '--file-path',
    type=str,
    help='Print operations but do not execute them, only applies to propagation here will still write ext_profiles',
)

_args = script.parse_args(parser)

import glob
import json
import csv

import time


start = time.time()
#import pandas as pd
from flatten_json import flatten

#Path of jsonl file
File_path = _args.file_path

with open(f, 'r') as read_file, open('path-to-csv-file.csv', 'a' , newline='') as write_file:
    csv_writer = csv.writer(f)

    # Write header
    
    for line in read_file:
        #flatten json files 
        json_data = json.loads(line)
        json_data_flat = flatten(json_data)
        
        #creating csv file
        csv_writer.
        thewriter.writerow([data_1['header1'],data_1['header2']])
