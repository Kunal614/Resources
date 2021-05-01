
import requests
# url = 'https://oauth2.googleapis.com/token'
# data = {
#     "client_id": "1091937598228-5aan4ts4lm6u28r38q29926b81jatcts.apps.googleusercontent.com",
#     "client_secret": "ZkzCCfgnau4hEhaH__PYflke",
#     "refresh_token": "1//04vfemCPfDdMICgYIARAAGAQSNwF-L9IrHy8vb_Pzgf6eV6wZyf7mVaHDkZCF_AJnsGFDgyjtwuv28D34Z7TcJW7YK2uZzIQSusU",
#     "grant_type": "refresh_token"
# }

# res  = requests.post(url ,  data=data)
# print(res.json()['access_token'])

'''
Refrence
https://stackoverflow.com/questions/10631042/how-to-generate-access-token-using-refresh-token-through-google-drive-api
https://stackoverflow.com/questions/13871982/unable-to-refresh-access-token-response-is-unauthorized-client
https://stackoverflow.com/questions/13871982/unable-to-refresh-access-token-response-is-unauthorized-client


for token
https://developers.google.com/oauthplayground/?code=4/0AY0e-g6optOZBEIdTUNcWc7hTEUREJcaO1AjtTWpdoHs3WfC6ipHnUfO_s8HawEPLUnbmg&scope=https://www.googleapis.com/auth/drive
'''
# url = 'https://clist.by/api/v2/resource/?username=resource&api_key=431aa1f9405dea2cdf8965b6aca897557f3f4217'

# res = requests.get(url)
# print(res)
# from pytz import timezone
# from datetime import timezone as tz
# import datetime
# utcnow = datetime.datetime.utcnow()
# utcnext = utcnow + datetime.timedelta(days=10)
# url = 'https://clist.by/api/v1/json/contest/?username=resource&api_key=431aa1f9405dea2cdf8965b6aca897557f3f4217' + '&start__gt=' + utcnow.isoformat() + '&start__lt=' + utcnext.isoformat() + '&duration__lte=864000&filtered=true&order_by=start'
# res = requests.get(url)
# print(res.status_code)
# event = res.json().get('objects', [])
# name_list = ['codeforces' , 'codechef' , 'atcoder' , 'hackerearth' , 'hackerrank' , 'codingcompetitions.withgoogle' ,'topcoder' , 'binarysearch' , 'leetcode']

# duration=[]
# name=[]
# href=[]
# start_end_time=[]
# event_name = []
# icon = []

# from dateutil.parser import parse

# dta = parse("2021-04-21T15:35:00", fuzzy=True)

# strt_format = "%H:%M %m-%d"
# end_format = "%H:%M"

# for data in event:
#     platform = str(data['resource']['name']).split('.')[0]
#     # print(platform)
#     if platform  in name_list:
#         y = int(data['duration']/3600)
#         z = data['duration'] - y*3600
#         dur = str("{0:0=2d}".format(y))+':'+str("{0:0=2d}".format(z))+' hr'
#         duration.append(dur)
#         event_name.append(data['event'])
#         href.append(data['href'])
#         name.append(platform)
#         icon.append(data['resource']['icon'])
#         st = data['start']
#         ed = data['end']
#         dt_st = parse(st, fuzzy=True)
#         dt_ed = parse(ed, fuzzy=True)
#         st_utc = dt_st.replace(tzinfo=tz.utc)
#         ed_utc = dt_ed.replace(tzinfo=tz.utc)
#         st_asia = st_utc.astimezone(timezone('Asia/Kolkata'))
#         ed_asia = ed_utc.astimezone(timezone('Asia/Kolkata'))
#         time = st_asia.strftime(strt_format) + ' '+ed_asia.strftime(end_format)
#         start_end_time.append(time)



# print(event_name , duration , href , name , icon , start_end_time)

from datetime import datetime
from dateutil.parser import parse
import time
# curr = datetime.now()
# print(curr.date())
# hr  = datetime.now().time().hour
# mn = datetime.now().time().minute
# print(hr*60+mn)

y = parse(str(datetime.now()))

print(y)

t1 = datetime.now().replace(microsecond=0)
time.sleep(3)
now = datetime.now().replace(microsecond=0)
print((now - t1).total_seconds())