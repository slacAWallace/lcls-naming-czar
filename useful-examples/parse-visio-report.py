'''
Script to parse an xml report of all the symbol names in a visio report,
looking for vacuum devices.

Start by creating a report in Visio that looks for the "Display text" of all the symbols
across all pages.
This should be a native field to all symbols, it's the text you probably used to indicate
name of the device/symbol.

Run the report selecting xml as the output.

Move the file next to this script and name it correctly.

Edit the code if you want to use a different CCC class.
'''


import czar
import xml.etree.ElementTree as et

filename="output.txt"
xmlfile="report.xml"

tree = et.parse(xmlfile)

root = tree.getroot()

functionalComponents = []

vacCCC = [
        "GCC",
        "GCT",
        "GFM",
        "GFS",
        "GHC",
        "GMP",
        "GPI",
        "GPS",
        "GSR",
        "GTC",
        "PCI",
        "PCS",
        "PCT",
        "PGT",
        "PIN",
        "PIP",
        "PMF",
        "PRO",
        "PRT",
        "PTM",
        "RGA",
        "VCN",
        "VFS",
        "VFV",
        "VGC",
        "VGM",
        "VGP",
        "VPC",
        "VRC",
        "VRM",
        "VVC",
        "VWC",
]

for item in root.findall('.//RowItem/Field/Val'):
    name = item.text
    try:
            czar.describe(name)
            for ccc in vacCCC:
                    if ccc in name:
                        functionalComponents.append(name)
                        break
    except:
            pass

with open(filename, 'w') as f:
        for item in functionalComponents:
                f.write('%s\n' % item)