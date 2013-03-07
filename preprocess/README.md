Preprocessing files
===================
dict-to-tab.sh
  Run this on the raw, uncompressed Crosswikis data to turn it into a
  tab-separated format.

addcols-mapper.py
  Hadoop mapper to add the counts to a new column in the raw data.

quotecols-mapper.py
  Hadoop mapper which puts text fields in quotes, and escapes existing quotes
  with double-quotes. Used to get the data in a format that can be imported into
  Apache Derby.

remove-disambiguation-mapper.py
  Hadoop mapper that removes pages ending in "_(disambiguation)". This doesn't
  get every case, but it's as good as we can get without using the Wikipedia
  API.

remove-disambiguation-reducer.py
  Hadoop reducer that recomputes the conditional probabilities after removing
  disambiguation pages.
