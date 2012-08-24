# DigitalContactMatron

Most important contac systems (iCloud, GMail) allow you to import contacts from a standard `.vcf` format.
Since I often work with new teams of people, I'd like to be able to generate importable contacts from a spreadsheet – faster, easier, more accurate. That's the purpose of DigitalContactMatron.

## Usage

Update the data in `sample_contacts.csv`, e.g. via Google Docs or Excel.

Use this to create `sample_contacts.csv.vcf`

    ./DigitalContactMatron.py sample_contacts.csv

Or specify the out-file:

    ./DigitalContactMatron.py sample_contacts.csv -o contacts.vcf


## The Name

At Mathcamp, systems have a tradition of ending in "-matron". Hence "DigitalContactMatron".