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
import ngram_common

candidates = {}


def form_candidates(tokens, max_n): 
    candidates = [] 
    for n in range(0, max_n): 
        for i in range(len(tokens) - n): 
            phrase = "_".join(tokens[i:i + n + 1]) 
            candidates.append(phrase) 
    return candidates 


def count_candidates(doc_file):
    doc_handle = open(doc_file)
 
    i = 0   
    for doc in doc_handle:
        if i % 1000 == 0:
            print "processing document %s" % i
        i += 1
        
        clauses = ngram_common.extract_clauses(doc)
        for cl in clauses:
            tokens = ngram_common.to_unigrams(cl)
            new_candidates = form_candidates(tokens, 3)
            for can in new_candidates:
                candidates[can] = candidates.get(can, 0) + 1


def output_candidates(candidates_file):
    candidate_handle = open(candidates_file, "w")

    for token, count in candidates.iteritems():
        if count == 1:
            continue
        candidate_handle.write("%s\t%s\n" % (token, count))


def main(doc_file, candidates_file):
    count_candidates(doc_file)
    output_candidates(candidates_file)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print ("usage: ./form_candidates.py "
            "<doc-in-file> <candidates-out-file>")

