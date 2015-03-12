PyGrams converts text to n-grams. Conversion is a three step process.

1) Extract all possible n-grams. Run "form\_candidates.py" to create a file containing all possible n-grams.

2) Filter possible n-grams. Run "filter\_candidates.py" to find just the n-grams which appear sufficiently frequently in relation to the frequency of their components.

3) Convert documents to n-grams. Run "convert\_docs.py" to convert documents into approved n-grams.


---


**Sample Input:** `We introduce a family of rings of symmetric functions depending on an infinite sequence of parameters.`

**Sample Output:** `introduc famili ring symmetr_function depend infinit_sequenc paramet`


---


Additional documentation appears in the README file. Note that this software depends on the porter\_stemmer.py module, which is available from http://tartarus.org/~martin/PorterStemmer/python.txt.

PyGrams has been tested with Python 2.5 on Linux.


---


_PyGrams has been developed by Jeffrey Regier with support from [The Bibliographic Knowledge Network](http://www.bibkn.org/)._