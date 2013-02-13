# Import data from a tab-separated file into a SQLite3 database.

echo "CREATE TABLE crosswikis (\
  anchor text, \
  cprob real, \
  entity text, 
  info text
);\
.separator '\t';\
.import ../../../crosswikis/lnrm.dict.tab;\
CREATE INDEX lnrmanchors ON crosswikis(anchor);"\
| ../../../data/crosswikis/crosswikis.db
