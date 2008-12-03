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


import porter_stemmer
import re
import stop_words


STEMMER = porter_stemmer.PorterStemmer()

def extract_clauses(text):
    stop_re = r'\b|\b'.join(stop_words.stop_words)
    clause_re = r'[^a-z -]+|\b%s\b' % stop_re
    clauses = re.split(clause_re, text.lower())
    clauses = [re.sub(r'^ | $', '', c) for c in clauses]
    return [c for c in clauses if c]

def to_unigrams(text):
    text = re.sub(r'[^a-z]+', ' ', text.lower())
    text = re.sub(r'(^ | $)+', '', text)
    words = re.split(r' ', text)
    long_words = (w for w in words if len(w) > 3) 
    stems = [STEMMER.stem(w, 0, len(w) - 1) for w in long_words]
    return stems

