# DigitalContactMatron

Most important contac systems (iCloud, GMail) allow you to import contacts from a standard `.vcf` format.
Since I often work with new teams of people, I'd like to be able to generate importable contacts from a spreadsheet – faster, easier, more accurate. That's the purpose of DigitalContactMatron.

## Usage

Prepare a spreadsheet (exported to CSV) with the following first row: First Name,Last Name,Email,Phone,Organization,Title
You can import `sample_contacts.csv` into Google Docs or Excel and export to CSV again to make this easier. Alternately, you could adapt an existing spreadsheet to have the same format and export it to CSV.

Use this to create `sample_contacts.csv.vcf`:

    ./DigitalContactMatron.py sample_contacts.csv

Or specify the out-file:

    ./DigitalContactMatron.py sample_contacts.csv -o contacts.vcf


## The Name

At Mathcamp, systems have a tradition of ending in "-matron". Hence "DigitalContactMatron".