# json_data = { "periodStart": "15/02/11",
# "periodEnd": "34/08/21",
# "monthlyPostingDay": 11,
# "comments" : [ ["2/3/21", "Justin Bieber", 5], ["5/4/21", "Lady Gaga", 6], ], ["5/4/21","Snoop Dog",2] , ["13/5/21","Justin Bieber", 3]]
#  }

# The scraper should
#     1. not return out of range dates 
#     2. return dates with specific format - "%d/%m/%y"
#     3. validated structure lists

import json
import datetime

PERIOD_FORMAT = "%d/%m/%y"
DAILY_FORMAT = "%d/%m/%y"

json_string = '''{
    "periodStart" : "15/02/11",
    "periodEnd" : "31/08/21",
    "monthlyPostingDay" : 11,
    "comments" :[["2/3/21","Justin Bieber",5], ["5/4/21", "Lady Gaga", 6],["5/4/21", "Snoop Dog", 2], ["13/5/21","Justin Bieber", 3] ]
}'''


def parse_data():
    "loads data from json string, output is dictionary"
    output = json.loads(json_string)
    return output

class Daily_sum:
    def __init__(self,
                # post_no,
                # comment_no,
                date_day
                ):

        # self.post_no = post_no
        # self.comment = comment_no
        self.date_day = date_day


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

def main():
    data = parse_data()

    start_date_obj = _date_str2obj(data['periodStart'],  PERIOD_FORMAT)
    end_date_obj = _date_str2obj(data['periodEnd'], PERIOD_FORMAT)
    print(f'Start date: {start_date_obj}, End_date: {end_date_obj}')

    dates_list =[i for i in iter_dates(start_date_obj, end_date_obj) ]

    post_date_list =[]
    for post in data['comments']:
        post_date_obj = _date_str2obj(post[0], DAILY_FORMAT)
        comment_no = post[2]
        post_date_list.append(post_date_obj)

    posts_obj_dict = {}
    for post_date in post_date_list:
        if post_date in dates_list:
            posts_obj_dict[post_date] = Daily_sum(comment_no, post_date)
            # posts_obj_list.append(Daily_sum(post_date))

    for i in posts_obj_dict.values():
        print(i.date_day)


    # for i in posts_obj_list:
    #     print(i.date_day)


        # print(posts_obj_list[0].date_day)
    
    
    




    # for i in iter_dates(start_date_obj, end_date_obj):
    #     if i in post_date_list:
    #         print(i)



    # for i in data['comments']:
    #     print(i)

    # a0 = Daily_sum( day = '2/3/21', comment_no = 'Justin Bieber',  post_no = 5) 
    # print(a0.posts) 

    # a0 = Dataclass(data['comments'][0])
    # a =[]
    # for d in data['comments']:
    #     a[d] = Dataclass()
    # print(a0)



if __name__ == '__main__':
    main()