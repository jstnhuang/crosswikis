CONNECT 'jdbc:derby:crosswikis;create=true';
CREATE TABLE crosswikis (
  anchor VARCHAR(32000), 
  cprob DOUBLE,
  entity VARCHAR(32000),
  info VARCHAR(32000),
  count INTEGER
);
CALL SYSCS_UTIL.SYSCS_IMPORT_TABLE(
  null,
  'CROSSWIKIS',
  'crosswikis.tsv',
  '	',
  null,
  null,
  0
);
CREATE INDEX lnrmanchors ON crosswikis (anchor);
