#!/usr/bin/env python3
import argparse
import datetime#

#2/ Can you write another python script that takes the following input data as arguments on the
# command line:
# (i) a lease start date
# (ii) a lease end date
# (iii) an optional first rent review date (if not supplied use the lease start date as default)
# (iv) the rent review frequency (in years)
# (v) the rent amount at the start of the lease

# and calculate:
# a) the rent review dates that would apply during the lease
# b) calculate the rent review amount for each rent review if we assume that the rent grows by
# n% at each review

FORMAT = "%Y-%m-%d"
N = 0.11
RENT_INCREASE = 1 + N
RENT_ROUND_DECIMAL = 0


def parse_arguments():
    parser = argparse.ArgumentParser(description="An app to calculate rent review dates and review amount.")

    parser.add_argument("--start_date", type=str, required=True,
                        help="lease start date, in ISO 8601 format YYYY-MM-DD")
    parser.add_argument("--end_date", type=str, required=True,
                        help="lease end date, in ISO 8601 format YYYY-MM-DD")
    parser.add_argument("--first_review_date",
                        help="optional first rent review date, in ISO 8601 format YYYY-MM-DD, defaults to start date if empty")
    parser.add_argument("--review_freq", type=check_positive_integer , required=True,
                        help="rent review frequency in years")
    parser.add_argument("--rent", type=check_positive_integer, required=True, help="the rent amount at the start of the lease")
    output = parser.parse_args()

    if not output.first_review_date :
        output.first_review_date = output.start_date

    output.start_date = _date_str2obj(output.start_date, FORMAT)
    output.end_date = _date_str2obj(output.end_date, FORMAT)
    output.first_review_date = _date_str2obj(output.first_review_date, FORMAT)

    _validate_end_date_greater_than_start_date(output.start_date, output.end_date )

    for v in [output.review_freq, output.rent]:
        check_positive_integer(v)

    return output


def _date_str2obj(date_string, format):

    try:
        date_obj = datetime.datetime.strptime(date_string, format)
    except:
        raise argparse.ArgumentTypeError(f"Date {date_string} is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info") 
    return date_obj.date()

def _datetime_obj2string(input_date, format):
    date_obj=datetime.datetime.strftime(input_date, format)
    return date_obj


def _validate_end_date_greater_than_start_date(start_date, end_date):
    if start_date > end_date :
        raise argparse.ArgumentTypeError(f'End date must be greater than start_date')

def check_positive_integer(input_number):
    try :
        int_input = int(input_number)
        if int_input < 1:
            raise argparse.ArgumentTypeError(f"Must be a positive integer number, not {input_number}")
    except:
        raise argparse.ArgumentTypeError(f'Must be a positive integer number, not {input_number}')
    return input_number

def calculate_rent_review_dates(start_date_obj, end_date_obj, rev_freq):
    output =[]
    for date in _iter_dates(start_date_obj, end_date_obj, rev_freq):
        output.append(_datetime_obj2string(date, FORMAT))
    return output

def _iter_dates(start_date_obj, end_date_obj, rev_freq):
    next_date = start_date_obj
    while next_date < end_date_obj :
        new_date_obj=datetime.date(next_date.year + rev_freq, next_date.month, next_date.day)
        yield next_date
        next_date = new_date_obj

def calculate_increasing_rent(RENT, review_dates_list):
    rent_increase_dict = {}
    increasing_rent = RENT
    for i in review_dates_list:
        rent_increase_dict[i] = round(increasing_rent * RENT_INCREASE , RENT_ROUND_DECIMAL)
        increasing_rent = rent_increase_dict[i]
    return rent_increase_dict


def main():
    try:
        args = parse_arguments()

        print("Program arguments:", args)
        
        START_DATE = args.start_date
        END_DATE = args.end_date
        FIRST_REVIEW_DATE = args.first_review_date
        REVIEW_FREQ = int(args.review_freq)
        RENT = int(args.rent)

    except ValueError:
        print("ERROR: Unsupported arguments")
        exit(10)

    review_dates_list = calculate_rent_review_dates(FIRST_REVIEW_DATE, END_DATE, REVIEW_FREQ )

    rent_increase_dict = calculate_increasing_rent(RENT, review_dates_list)
    print(rent_increase_dict)
        

if __name__ == "__main__":
    main()
