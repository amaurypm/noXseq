# noXseq
Given a set of protein sequences filters out these with non-standard residues. If not input file given it reads from the standard input and if not output file given it writes to standard output.

## Usage
`usage: noXseq [-h] [-f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}] [-v] [inseqfile] [outseqfile]`

It can be inserted in command pipes.

## Installation
This is a Python script, so, you can just run the uniqseq.py file or put a symbolic link in any directory of your PATH. The second option is recommend.

## Dependencies
* Python3
* Biopython
* argparse

## OSs
It runs in Linux, probably in Mac OS too, but not tested.

## Examples

`noXseq multiple_sequences_and_some_with_non_standard_aas.fasta only_sequences_without_non_standard_aas.fasta`

`noXseq multiple_sequences_and_some_with_non_standard_aas.pir only_sequences_without_non_standard_aas.pir -f pir`

`cat multiple_sequences_and_some_with_non_standard_aas.fasta | noXseq > only_sequences_without_non_standard_aas.fasta`
