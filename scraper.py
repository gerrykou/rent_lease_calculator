# json_data = { "periodStart": "15/02/11",
# "periodEnd": "34/08/21",
# "monthlyPostingDay": 11,
# "comments" : [ ["2/3/21", "Justin Bieber", 5], ["5/4/21", "Lady Gaga", 6], ], ["5/4/21","Snoop Dog",2] , ["13/5/21","Justin Bieber", 3]]
#  }
import json

json_string = '''{
    "periodStart" : "15/02/11",
    "periodEnd" : "34/08/21",
    "monthlyPostingDay" : 11,
    "comments" :[["2/3/21","Justin Bieber",5], ["5/4/21", "Lady Gaga", 6],["5/4/21", "Snoop Dog", 2], ["13/5/21","Justin Bieber", 3] ]
}'''

data = json.loads(json_string)


print(data["periodStart"], data['comments'])