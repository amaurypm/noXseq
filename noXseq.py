#!/usr/bin/env python3
## Remove duplicated protein/nucleic acid sequences, keeping the first occurrence. 
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
from Bio import SeqIO

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Given a set of protein sequences filters out those with non-standard residues. If not input file given it reads from the standard input and if not output file given it writes to standard output.")
    parser.add_argument('inseqfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input sequence file [default: stdin].')
    parser.add_argument('outseqfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Output sequence file [default: stdout].')
    parser.add_argument('-f', '--format', choices=['fasta','clustal', 'embl', 'genbank', 'imgt', 'phd', 'pir', 'tab'], default='fasta', help='Sequence format [default: %(default)s]. WARNING: This program check for sequence only, any other data is ignored during the comparison, although the output sequences have all their original data.')
    parser.add_argument('-v', '--version', action='version', version='0.9.0', help="Show program's version number and exit.")

    args=parser.parse_args()

    no_X_seqs = []
    standard_aas = set("ACDEFGHIKLMNPQRSTUVWY")

    try:
        for record in SeqIO.parse(args.inseqfile, args.format):
            if standard_aas.issuperset(set(record.seq)):
                no_X_seqs.append(record)

    except ValueError:
        sys.stderr.write("ERROR: Input has not a valid {} format.".format(args.format))
        sys.exit(1)

    SeqIO.write(no_X_seqs, args.outseqfile, args.format)

## Running the script
if __name__ == "__main__":
        main()

