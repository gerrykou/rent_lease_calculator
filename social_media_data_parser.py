import json
import datetime
import csv

# 1/ Can you write a python script, a self-contained .py file to pass to your teammates, to
# (a) parse the json script (below) from the scraper
# (b) store the number of (i) posts and (ii)comments on a daily basis across the time period in a python
# class
# (c) calculate the sum of posts and comments on a daily basis
# (d) calculate the aggregate number of posts and comments on a monthly basis
# (e) store the monthly totals for the whole period for (i) posts and (ii) comments in a csv file
# { “periodStart”: “15/02/11”,
# “periodEnd”: “34/08/21”,
# “monthlyPostingDay”: 11,
# “comments” : [ [“2/3/21”, “Justin Bieber”, 5], [“5/4/21”, “Lady Gaga”, 6], ], [“5/4/21”, “Snoop Dog”,
# 2] , [“13/5/21”,”Justin Bieber", 3]]
# }

# The scraper should
#     1. not return out of range dates 
#     2. return dates with consistent specific format - "%Y-%m-%d"
#     3. validated structure lists



INPUT_FORMAT = "%d/%m/%y"
OUTPUT_FORMAT = "%Y-%m-%d"
YM_OUTPUT_FORMAT = "%Y-%m"
FILENAME = "social_media_data.csv"

json_string = """{
    "periodStart" : "15/02/11",
    "periodEnd" : "31/08/21",
    "monthlyPostingDay" : 11,
    "comments" :[["2/3/21","Justin Bieber",5], ["5/4/21", "Lady Gaga", 6],["5/4/21", "Snoop Dog", 2], ["13/5/21","Justin Bieber", 3]]
}"""


class Social_media_data:
    def __init__(self, input_data):
        self._data = json.loads(input_data)
        self.period_start_date_obj = self._date_str2obj(self._data["periodStart"], INPUT_FORMAT)
        self.period_end_date_obj = self._date_str2obj(self._data["periodEnd"], INPUT_FORMAT)
        self.posts = self._data["comments"]
        self.posts_dates_set = self._posts_dates_set(self.posts, INPUT_FORMAT)
        self.intersection_dates_set = self._intersection_dates_set(self.period_start_date_obj, self.period_end_date_obj, self.posts_dates_set)
        self.daily_stats_dict = self.calculate_stats(self.posts, self.intersection_dates_set, INPUT_FORMAT, OUTPUT_FORMAT)
        self.monthly_stats_dict = self.calculate_stats(self.posts, self.intersection_dates_set, INPUT_FORMAT, YM_OUTPUT_FORMAT)
    

    def _posts_dates_set(self, posts, input_format):
        posts_dates_set = set()
        for post in posts: 
            posts_dates_set.add(self._date_str2obj(post[0], input_format))
        return posts_dates_set
    
    def _intersection_dates_set(self, period_start_date_obj, period_end_date_obj, posts_dates_set):
        intersection_dates_set ={i for i in self._iter_dates(period_start_date_obj, period_end_date_obj) if i in posts_dates_set}
        return intersection_dates_set

    def _iter_dates(self, start_date_obj, end_date_obj):
        next_date = start_date_obj
        while next_date < end_date_obj :
            new_date_obj=(next_date + datetime.timedelta(days=1))
            next_date = new_date_obj
            yield next_date

    def _date_str2obj(self, date_string, format):
        try:
            date_obj = datetime.datetime.strptime(date_string, format)
        except:
            raise ValueError(f"Date {date_string} out of range")
        return date_obj.date()

    def _datetime_obj2string(self, input_date, format):
        date_obj=datetime.datetime.strftime(input_date, format)
        return date_obj

    def calculate_stats(self, posts, intersection_dates_set , input_format, output_format):
        """Function that calculates daily or monthly sum of posts and comments 
        for a specific range of dates. Daily or monthly is controlled from ouput format
        For daily stats: OUTPUT_FORMAT = "%Y-%m-%d"
        For monthly stats: YM_OUTPUT_FORMAT = "%Y-%m"

        """
        sum_dict = {}
        for post in posts:
            date_obj = self._date_str2obj(post[0], input_format)
            if date_obj in intersection_dates_set:
                date_str = self._datetime_obj2string(date_obj, output_format)
                comments_no = post[2]
                if date_str in sum_dict.keys():
                    sum_dict[date_str]['posts_sum'] += 1
                    sum_dict[date_str]['comments_sum'] += comments_no
                else:
                    sum_dict[date_str] = {'posts_sum' : 1, 'comments_sum' : comments_no }
        print(sum_dict)
        return sum_dict


    def export_to_csv(self,filename, data):
        with open(filename , mode="w") as csv_file:
            fieldnames = ["date_month", "posts_sum", "comments_sum"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for date, sum in data.items():
                writer.writerow({ "date_month" : date , "posts_sum": sum["posts_sum"], "comments_sum": sum["comments_sum"]})
        return None


def main():
    data = Social_media_data(json_string)

    start_date_str = data._datetime_obj2string(data.period_start_date_obj, OUTPUT_FORMAT)
    end_date_str = data._datetime_obj2string(data.period_end_date_obj, OUTPUT_FORMAT)
    filename = '_'.join([start_date_str, end_date_str, FILENAME])

    data.export_to_csv(filename, data.monthly_stats_dict)


if __name__ == "__main__":
    main()