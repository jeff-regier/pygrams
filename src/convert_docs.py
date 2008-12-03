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


import sys, re
import ngram_common

vocab = {}


def load_vocab(vocab_file):
    vocab_handle = open(vocab_file)
    for line in vocab_handle:
        vocab[line.rstrip()] = True


def form_ngrams(unigrams):
    start = 0
    ngrams = []
    while start < len(unigrams):
        for n in [3, 2, 1]:
            if len(unigrams) < start + n:
                continue
            candidate = "_".join(unigrams[start:start + n])
            if vocab.has_key(candidate):
                ngrams.append(candidate)
                start += n - 1
                break
        start += 1
    return ngrams


def convert_docs(doc_file, out_file):
    doc_handle = open(doc_file)
    out_handle = open(out_file, "w")

    i = 0
    for doc in doc_handle:
        if i % 1000 == 0:
            print "procesing document %s" % i
        i += 1

        id_match = re.search(r'^(.+?\t)(.*)', doc)
        doc_id = id_match.group(1) if id_match else ""
        doc = id_match.group(2) if id_match else doc

        clauses = ngram_common.extract_clauses(doc)
        doc_ngrams = []
        for cl in clauses:
            unigrams = ngram_common.to_unigrams(cl)
            cl_ngrams = form_ngrams(unigrams)
            doc_ngrams.extend(cl_ngrams)
        out_handle.write("%s%s\n" % (doc_id, " ".join(doc_ngrams)))


def main(vocab_file, doc_file, out_file):
    load_vocab(vocab_file)
    convert_docs(doc_file, out_file)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3],)
    else:
        print ("usage: %s <vocabulary-file> <doc-file> "
            "<out-file>" % sys.argv[0])

