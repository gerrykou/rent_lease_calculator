# json_data = { "periodStart": "15/02/11",
# "periodEnd": "34/08/21",
# "monthlyPostingDay": 11,
# "comments" : [ ["2/3/21", "Justin Bieber", 5], ["5/4/21", "Lady Gaga", 6], ], ["5/4/21","Snoop Dog",2] , ["13/5/21","Justin Bieber", 3]]
#  }

# The scraper should
#     1. not return out of range dates 
#     2. return dates with consistent specific format - "%d/%m/%y"
#     3. validated structure lists

import json
import datetime
import csv

PERIOD_FORMAT = "%d/%m/%y"
DAILY_FORMAT = "%d/%m/%y"
MONTH_YEAR_FORMAT = "%m/%y"

json_string = '''{
    "periodStart" : "15/02/11",
    "periodEnd" : "31/08/21",
    "monthlyPostingDay" : 11,
    "comments" :[["2/3/21","Justin Bieber",5], ["5/4/21", "Lady Gaga", 6],["5/4/21", "Snoop Dog", 2], ["13/5/21","Justin Bieber", 3]]
}'''


def parse_data():
    "loads data from json string, output is dictionary"
    output = json.loads(json_string)
    return output

class Daily_sum:
    def __init__(self,
                post_no,
                comment_no,
                date_day
                ):

        self.post_no = post_no
        self.comment_no = comment_no
        self.date_day = date_day
    
    def add_post(self):
        self.post_no += 1

    def add_comment(self, comment_number):
        self.comment_no += comment_number


def iter_dates(start_date_obj, end_date_obj):
    next_date = start_date_obj
    while next_date < end_date_obj :
        new_date_obj=(next_date + datetime.timedelta(days=1))
        next_date = new_date_obj
        yield next_date

def _date_str2obj(date_string, format):
    try:
        date_obj = datetime.datetime.strptime(date_string, format)
    except:
        print(f'ERROR: Date {date_string} out of range')
        exit(10) 
    return date_obj.date()

def _datetime_obj2string(input_date, format):
    date_obj=datetime.datetime.strftime(input_date, format)
    return date_obj

def store_data_in_class_objects(data , dates_list):
    posts_obj_dict = {}
    for post in data['comments']:
        post_date_obj = _date_str2obj(post[0], DAILY_FORMAT)
        comment_no = post[2]
        if post_date_obj in dates_list:
            if post_date_obj in posts_obj_dict.keys() :
                posts_obj_dict[post_date_obj].add_comment(comment_no)
                posts_obj_dict[post_date_obj].add_post()
            else:
                posts_obj_dict[post_date_obj] = Daily_sum(1, comment_no, post_date_obj)
    return posts_obj_dict


def monthly_and_daily_sum(posts_obj_dict):
    monthly_sum_dict ={}
    for i in posts_obj_dict.values():
        sum_of_posts_daily = i.post_no
        sum_of_comments_daily = i.comment_no
        print(f'Daily sum for {i.date_day} is, posts: {sum_of_posts_daily} , comments: {sum_of_comments_daily}')
        month_year_str = _datetime_obj2string(i.date_day, MONTH_YEAR_FORMAT)
        if month_year_str in monthly_sum_dict.keys():
            monthly_sum_dict[month_year_str]['monthly_post_sum'] += sum_of_posts_daily
            monthly_sum_dict[month_year_str]['monthly_comments_sum'] += sum_of_comments_daily
        else:
            monthly_sum_dict[month_year_str] = {'monthly_post_sum' : sum_of_posts_daily, 'monthly_comments_sum' : sum_of_comments_daily }
    print(monthly_sum_dict)
    return monthly_sum_dict

def export_to_csv(filename, data):
    with open(filename , mode='w') as csv_file:
        fieldnames = ['month', 'posts_sum', 'comments_sum']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for date, sum in data.items():
            writer.writerow({ 'month' : date , 'posts_sum': sum['monthly_post_sum'], 'comments_sum': sum['monthly_comments_sum']})
    return None


def main():
    data = parse_data()

    start_date_obj = _date_str2obj(data['periodStart'],  PERIOD_FORMAT)
    end_date_obj = _date_str2obj(data['periodEnd'], PERIOD_FORMAT)

    print(f'Start date: {start_date_obj}, End_date: {end_date_obj}')

    dates_list =[i for i in iter_dates(start_date_obj, end_date_obj)]

    posts_obj_dict = store_data_in_class_objects(data , dates_list)

    monthly_sum_dict = monthly_and_daily_sum(posts_obj_dict)

    export_to_csv('social_media_data.csv', monthly_sum_dict)


if __name__ == '__main__':
    main()