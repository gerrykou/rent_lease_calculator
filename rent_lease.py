#!/usr/bin/env python3
import argparse
import datetime

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
RENT_INCREASE_FACTOR = 1 + N
RENT_ROUND_DECIMAL = 0


def parse_arguments():
    parser = argparse.ArgumentParser(description="An app to calculate rent review dates and review amount.")
    parser.add_argument("--start_date",
                        type=str,
                        required=True,
                        help="lease start date, in ISO 8601 format YYYY-MM-DD")
    parser.add_argument("--end_date", type=str, required=True,
                        help="lease end date, in ISO 8601 format YYYY-MM-DD")
    parser.add_argument("--first_review_date",
                        help="optional first rent review date, in ISO 8601 format YYYY-MM-DD, defaults to start date if empty")
    parser.add_argument("--review_freq", type=int , required=True,
                        help="rent review frequency in years")
    parser.add_argument("--rent", type=int, required=True, help="the rent amount at the start of the lease")
   
    output = parser.parse_args()

    if not output.first_review_date :
        output.first_review_date = output.start_date

    output.start_date_obj = _date_str2obj(output.start_date, FORMAT)
    output.end_date_obj = _date_str2obj(output.end_date, FORMAT)
    output.first_review_date_obj = _date_str2obj(output.first_review_date, FORMAT)

    _validate_end_date_greater_than_start_date(output.start_date, output.end_date)

    for v in [output.review_freq, output.rent]:
        _check_positive_integer(v)

    return output


def _date_str2obj(date_string, format):

    try:
        date_obj = datetime.datetime.strptime(date_string, format)
    except:
        raise argparse.ArgumentTypeError(f"""Date {date_string} is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info""") 
    return date_obj.date()

def _datetime_obj2string(input_date, format):
    date_obj = datetime.datetime.strftime(input_date, format)
    return date_obj


def _validate_end_date_greater_than_start_date(start_date, end_date):
    if start_date > end_date :
        raise argparse.ArgumentTypeError(f"End date must be greater than start_date")


def _check_positive_integer(input_number):
    if input_number < 1:
        raise argparse.ArgumentTypeError(f"Must be a positive integer number, not {input_number}")
    return input_number

def calculate_rent_review_dates(start_date_obj, end_date_obj, rev_freq):
    #   requires input date object, output in date string
    output = []
    for date in _iter_dates(start_date_obj, end_date_obj, rev_freq):
        output.append(_datetime_obj2string(date, FORMAT))
    return output

def _iter_dates(start_date_obj, end_date_obj, rev_freq):
    next_date = start_date_obj
    while next_date < end_date_obj :
        new_date_obj = datetime.date(next_date.year + rev_freq, next_date.month, next_date.day)
        yield next_date
        next_date = new_date_obj

def calculate_increasing_rent(start_date_str,
                            end_date_obj,
                            first_review_day_obj,
                            review_frequency,
                            initial_rent,
                            rent_increase_factor,
                            rent_round_decimal):
    """Function that calculates how much the rent will increase per review date
    from a start date
    
    """
    review_dates_list = calculate_rent_review_dates(first_review_day_obj, end_date_obj, review_frequency)
    rent_increase_dict = {f'{start_date_str}': initial_rent}  # initialize dictionary with current rent, if review date == start date: overrides
    increasing_rent = initial_rent
    for date in review_dates_list:
        rent_increase_dict[date] = round(increasing_rent * rent_increase_factor, rent_round_decimal)
        increasing_rent = rent_increase_dict[date]
    return rent_increase_dict


def main():
    try:
        args = parse_arguments()

        print("Program arguments:", args)

        START_DATE = args.start_date
        REVIEW_FREQUENCY = args.review_freq
        RENT = args.rent
        END_DATE_OBJ = args.end_date_obj
        FIRST_REVIEW_DATE_OBJ = args.first_review_date_obj

    except ValueError:
        print("ERROR: Unsupported arguments")
        exit(10)


    rent_increase_dict = calculate_increasing_rent(START_DATE,
                                                END_DATE_OBJ,
                                                FIRST_REVIEW_DATE_OBJ,
                                                REVIEW_FREQUENCY,
                                                RENT,
                                                RENT_INCREASE_FACTOR,
                                                RENT_ROUND_DECIMAL)
    print(rent_increase_dict)
        

if __name__ == "__main__":
    main()
