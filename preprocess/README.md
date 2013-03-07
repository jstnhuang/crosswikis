Preprocessing files
===================
<dl>
  <dt>dict-to-tab.sh</dt>
  <dd>Run this on the raw, uncompressed Crosswikis data to turn it into a
  tab-separated format.</dd>

  <dt>addcols-mapper.py</dt>
  <dd>Hadoop mapper to add the counts to a new column in the raw data.</dd>

  <dt>quotecols-mapper.py</dt>
  <dd>Hadoop mapper which puts text fields in quotes, and escapes existing
  quotes with double-quotes. Used to get the data in a format that can be
  imported into Apache Derby.</dd>

  <dt>remove-disambiguation-mapper.py</dt>
  <dd>Hadoop mapper that removes pages ending in "_(disambiguation)". This
  doesn't get every case, but it's as good as we can get without using the
  Wikipedia API.</dd>

  <dt>remove-disambiguation-reducer.py</dt>
  <dd>Hadoop reducer that recomputes the conditional probabilities after
  removing disambiguation pages.</dd>

  <dt>import-derby.sql</dt>
  <dd>SQL script for Apache Derby to import the data from a file called
  'crosswikis.tsv' into a table called 'crosswikis' in a database called
  'crosswikis'. Assumes that the .tsv file is well formed, namely that it is
  tab-separated, text fields are in quotes, and quotes that are part of the text
  are double-quoted.</dd>
</dl>
