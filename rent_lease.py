#!/usr/bin/env python3
import argparse
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="An app to calculate rent review dates and review amount")
    parser.add_argument("--start_date", type=str, required=True,
                        help="lease start date, in ISO 8601 format YYYYMMDD")
    parser.add_argument("--end_date", type=str, required=True,
                        help="lease end date, in ISO 8601 format YYYYMMDD")
    parser.add_argument("--first_review_date",
                        help="optional first rent review date, in ISO 8601 format YYYYMMDD, defaults to start date if empty")
    parser.add_argument("--review_freq", type=str, required=True,
                        help="rent review frequency in years")
    parser.add_argument("--rent", type=int, required=True, help="the rent amount at the start of the lease")
    output = parser.parse_args()

    if output.first_review_date is None:
        output.first_review_date = output.start_date
    
    return output




def main():

    args = parse_arguments()

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
            print('ERROR: Unsupported arguments')
            exit(10)



if __name__ == "__main__":
    main()
