from .models import *
import requests
from datetime import datetime

def problem_of_the_Day(request):  # every day night 12'0 clock 
    obj = problemofday.objects.all()[0]
    tag = obj.tags
    url = "https://codeforces.com/api/problemset.problems?tags="+str(tag)
    res = requests.get(url).json()
    res = res['result']['problems']
    old = obj.old_questions.split(',')
    print(type(res[0]['rating']) ,int(obj.ratings))
    for result in res:
        new = str(result['contestId']) + '/'+result['index']
        try:
            if result['rating'] == int(obj.ratings) and str(new) not in old:
                print(result['name'] , result['rating'])
                question = "https://codeforces.com/problemset/problem/"+new
                obj.problem_of_the_day = question
                old_prblmset = obj.old_questions + ','+new
                print(old_prblmset)
                obj.old_questions = old_prblmset
                obj.save()
                prblm_tag = ''
                for tags in result['tags']:
                    prblm_tag+=tags+','
                # print(question , datetime.today() , prblm_tag , result['rating'] , result['name'])
                problem_data = problemset(url= question , date_of_problem = datetime.today() , tags = prblm_tag , ratings = str(result['rating']) , name = str(result['name']))
                problem_data.save()
                # print(question)
        except:
            continue