#!/bin/bash
cat ../data/lnrm.dict | sed -r 's/(.*)	([0-9\.e-]+) (\S*)( .*)*/\1	\2	\3	\4/' > ../data/lnrm.dict.tab
