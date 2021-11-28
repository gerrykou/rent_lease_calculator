# rent_lease.py
To run:
```
python3 rent_lease.py --start_date=2019-09-07 --end_date=2040-09-07 --first_review_date=2020-09-07 --review_freq=10  --rent=1200
```
```
python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --review_freq=1  --rent=1200
```
```
python3 rent_lease.py --help
```

These commands should return ERROR:

```
python3 rent_lease.py --start_date=2019/09/07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
```
returns: argparse.ArgumentTypeError: Date 2019/09/07 is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info
```
python3 rent_lease.py --start_date=2019-09-07 --end_date=2018-09-07 --first_review_date=2020-09-07 --review_freq=1  --rent=1200
```
returns: argparse.ArgumentTypeError: End date must be greater than start_date
```
python3 rent_lease.py --start_date=2019-09-07 --end_date=2021-09-07 --first_review_date=2020-09-07 --review_freq=1.5  --rent=1200
```
returns: rent_lease.py: error: argument --review_freq: invalid int value: '1.5'