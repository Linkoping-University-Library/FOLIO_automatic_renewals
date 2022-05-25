# FOLIO_automatic_renewals

python-skript för automatiska omlån

Körs på folioscript som cron-jobb:

0 7 * * * /usr/local/bin/python_scripts/automaticrenewals.sh > /dev/null 2>&1

automaticrenewals.sh:

cd /usr/local/bin/python_scripts

source bin/activate

cd automaticrenewals

python automaticRenewals.py
