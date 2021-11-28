python3 rent_lease.py --start_date=2019-09-07 --end_date=2040-09-07 --first_review_date=2020-09-07 --review_freq=10  --rent=1200
python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
python3 rent_lease.py --help


raise error

python3 rent_lease.py --start_date=2019/09/07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
ERROR: Date 2019/09/07 is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info

python3 rent_lease.py --start_date=20190907 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
ERROR: Date 20190907 is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info

python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-15-07 --review_freq=1  --rent=1200
ERROR: Date 2020-15-07 is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info

python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-09-32 --review_freq=1  --rent=1200
ERROR: Date 2020-09-32 is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info

python3 rent_lease.py --start_date=2019-09-07 --end_date=2018-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
ERROR: End date must be greater than start_date

python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1.5  --rent=1200
