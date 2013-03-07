Preprocessing files
===================
<dl>
  <dt>dict-to-tab.sh</dt>
  <dd>Run this on the raw, uncompressed Crosswikis data to turn it into a
  tab-separated format.</dd>

  <dt>addcols-mapper.py</dt>
  <dd>Hadoop mapper to add the counts to a new column in the raw data.</dd>

  <dt>quotecols-mapper.py</dt>
  <dd>Hadoop mapper which puts text fields in quotes, and escapes existing quotes
  with double-quotes. Used to get the data in a format that can be imported into
  Apache Derby.</dd>

  <dt>remove-disambiguation-mapper.py</dt>
  <dd>Hadoop mapper that removes pages ending in "_(disambiguation)". This doesn't
  get every case, but it's as good as we can get without using the Wikipedia
  API.</dd>

  <dt>remove-disambiguation-reducer.py</dt>
  <dd>Hadoop reducer that recomputes the conditional probabilities after removing
  disambiguation pages.</dd>
</dl>
