#!/usr/bin/python

# Copyright 2008, Jeffrey Regier, jeff [at] stat [dot] berkeley [dot] edu

# This file is part of PyGrams.
#
# PyGrams is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyGrams is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with PyGrams.  If not, see <http://www.gnu.org/licenses/>.


import sys
import re
import math

MIN_COUNT = 10
PRIOR_GRAM_COUNT = 100
BIGRAM_THESHHOLD = 0.005
TRIGRAM_THESHHOLD = 0.004

candidates = {}


def load_candidates(cand_file):
    cand_handle = open(cand_file)
 
    for line in cand_handle:
        token, count = re.split(r'\t', line.rstrip())
        candidates[token] = int(count)


def output_ngrams(vocab_file):
    vocab_handle = open(vocab_file, "w")
    bigram_handle = open(vocab_file + ".bi", "w")
    trigram_handle = open(vocab_file + ".tri", "w")

    for token, count in candidates.iteritems():
        if count < MIN_COUNT:
            continue

        w = float(count) / (count + PRIOR_GRAM_COUNT)

        parts = re.split('_', token)
        pt = [candidates[p] for p in parts]

        if len(parts) == 2:
            psi = w * (count / math.pow(pt[0] * pt[1], 1/2.))
            bigram_handle.write("%s\t%s\t%s\n" % (psi, token, count))
            if psi < BIGRAM_THESHHOLD:
                continue

        if len(parts) == 3:
            psi = w * (count / math.pow(pt[0] * pt[1] * pt[2], 1/3.))
            trigram_handle.write("%s\t%s\t%s\n" % (psi, token, count))
            if psi < TRIGRAM_THESHHOLD:
                continue

        vocab_handle.write("%s\n" % token)


def main(cand_file, vocab_file):
    load_candidates(cand_file)
    output_ngrams(vocab_file)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print ("usage: ./filter_candidates.py "
            "<candidates-in-file> <vocabulary-out-file>")

