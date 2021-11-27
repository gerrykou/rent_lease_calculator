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
    #returns date object from string 
    try:
        date_obj = datetime.datetime.strptime(date_string, format)
    except:
        print(f"ERROR: Date {date_string} is not in a correct date format or not a valid date. It should be in ISO 8601 format YYYY-MM-DD, try --help for more info")
        exit(10) 
    return date_obj.date()

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



def main():
    while True:
        try:
            args = parse_arguments()

            print("Program arguments:", args)
            
            START_DATE = args.start_date
            END_DATE = args.end_date
            FIRST_REVIEW_DATE = args.first_review_date
            REVIEW_FREQ = args.review_freq
            RENT = args.rent

            print(START_DATE, END_DATE, FIRST_REVIEW_DATE, REVIEW_FREQ ,RENT)
            exit(0)
        except ValueError:
            print("ERROR: Unsupported arguments")
            exit(10)



if __name__ == "__main__":
    main()
