#!/usr/bin/python

import csv
import argparse
from string import Template

parser = argparse.ArgumentParser(description='Convert CSV file of contacts to an importable .vcf.')

# I would use type=argparse.FileType('rt'), but I can't figure out how to get a string of the file name for a default out file.
parser.add_argument('inFile', action="store", metavar='in-file', type=str)
parser.add_argument('-o', action="store", required=False, metavar='out-file', type=argparse.FileType('wt'))

args = parser.parse_args()

# Since I can't figure out how to get argparse to handle an optional out-file with a default name based on the in-file, I have to do this manually...
inFile = open(args.inFile, "r")
reader = csv.reader(inFile)
if not args.o:
  args.o = open(args.inFile + ".vcf", "w")

## Check the format.

firstRow = reader.next()

correctFormat = ['First Name', 'Last Name', 'Email', 'Phone', 'Organization', 'Title']
if firstRow == correctFormat:
  print "Passed format check. Data header (the first row) is in the correct format."
else:
  print "[WARNING] Data is NOT in the correct format."
  print "[WARNING]        Correct format: ", correctFormat
  print "[WARNING] First row of the data: ", firstRow
  print "[WARNING] Proceeding anyhow."

## Process each row as a contact.

print "Processing..."

vCardTemplate = Template("""BEGIN:VCARD
VERSION:3.0
N:${LastName};${FirstName};;;
FN:${FirstName} ${LastName}
ORG:${Organization};
TITLE:${Title}
EMAIL;type=INTERNET;type=HOME;type=pref:${Email}
TEL;type=CELL;type=VOICE;type=pref:${Phone}
END:VCARD""")

for row in reader:

  # Is there a better way to make this match up with correctFormat?
  FirstName    = row[0]
  LastName     = row[1]
  Email        = row[2]
  Phone        = row[3]
  Organization = row[4]
  Title        = row[5]

  print "Converting:", FirstName, LastName

  vCard = vCardTemplate.substitute(
    FirstName=FirstName,
    LastName=LastName,
    Email=Email,
    Phone=Phone,
    Organization=Organization,
    Title=Title
    )
  args.o.write(vCard)

print "Done."