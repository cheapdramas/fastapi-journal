
from datetime import datetime
import calendar
from db_scripts import get_schedule
def get_work_days():
    curr_year = datetime.now().year

    year_previous = curr_year - 1
    year_next = curr_year +1

    curr_month = datetime.now().month

    all_dates_now = calendar.monthcalendar(curr_year,curr_month)


    prev_month = curr_month -1
    next_month = curr_month+1
    if prev_month == 0:

        prev_month = 12
        all_dates_previous = calendar.monthcalendar(year_previous,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]
    else:
        all_dates_previous = calendar.monthcalendar(curr_year,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]


    all_dates_now = calendar.monthcalendar(curr_year,curr_month)
    all_dates_now = [i[:5] for i in all_dates_now]
    if next_month >12:

        next_month = 1
        all_dates_next = calendar.monthcalendar(year_next,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]
    else:
        all_dates_next = calendar.monthcalendar(curr_year,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]

  
    days = ['Понеділок','Вівторок','Середа','Четвер',"П'ятниця"]


    days_calendar = []
    days_date = []
    c = 0

    all_days_month = []
    for a in all_dates_now:
        if a.count(0) != 5:
            all_days_month.append(days)

    for a in all_dates_now:
        if 0 in a:
            if a.count(0) != 5:
            
                if a == all_dates_now[0]:
                    
                    b = [str(i)+'.'+ str(prev_month) for i in all_dates_previous if i != 0]
                    for i in a:
                        if i != 0:
                            b.append(i)
                    all_dates_now[0] = b

                if a == all_dates_now[-1]:
                    
                    b = [str(i)+'.'+ str(next_month) for i in all_dates_next if i != 0]
                    for i in range(a.count(0)):
                        a.remove(0)
                    for i in b:
                        a.append(i)
            else:
                all_dates_now.remove(a)

    for i in all_dates_now:
        for o in i:
            if len(str(o).split('.'))==2 and int(str(o).split('.')[1]) == 1 and curr_month == 12:
                a = str(o) +'.' + str(year_next)
                i[i.index(o)] = str(datetime.strptime(a,'%d.%m.%Y').date())
            elif len(str(o).split('.'))==2 and int(str(o).split('.')[1]) == 12 and curr_month == 1:
                a = str(o) +'.' + str(year_previous)
                i[i.index(o)] =str(datetime.strptime(a,'%d.%m.%Y').date())
            else:
                if len(str(o).split('.'))==2:
                    m = str(o).split('.')[1]
                    d = str(o).split('.')[0]
                    date_ = d +'.'+m+'.' + str(curr_year)
                    i[i.index(o)] = str(datetime.strptime(date_,'%d.%m.%Y').date())
                else:
                    date_ = str(o) + '.' + str(curr_month) +'.'+ str(curr_year)
                    i[i.index(o)] = str(datetime.strptime(date_,'%d.%m.%Y').date())


    return all_dates_now



def homework_days_represent():
    curr_year = datetime.now().year

    year_previous = curr_year - 1
    year_next = curr_year +1

    curr_month = datetime.now().month

    all_dates_now = calendar.monthcalendar(curr_year,curr_month)


    prev_month = curr_month -1
    next_month = curr_month+1
    if prev_month == 0:

        prev_month = 12
        all_dates_previous = calendar.monthcalendar(year_previous,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]
    else:
        all_dates_previous = calendar.monthcalendar(curr_year,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]


    all_dates_now = calendar.monthcalendar(curr_year,curr_month)
    all_dates_now = [i[:5] for i in all_dates_now]
    if next_month >12:

        next_month = 1
        all_dates_next = calendar.monthcalendar(year_next,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]
    else:
        all_dates_next = calendar.monthcalendar(curr_year,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]

  
    days = ['Понеділок','Вівторок','Середа','Четвер',"П'ятниця"]


    days_calendar = []
    days_date = []
    c = 0

    all_days_month = []
    for a in all_dates_now:
        if a.count(0) != 5:
            all_days_month.append(days)

    for a in all_dates_now:
        if 0 in a:
            if a.count(0) != 5:
            
                if a == all_dates_now[0]:
                    
                    b = [str(i)+'.'+ str(prev_month) for i in all_dates_previous if i != 0]
                    for i in a:
                        if i != 0:
                            b.append(i)
                    all_dates_now[0] = b

                if a == all_dates_now[-1]:
                    
                    b = [str(i)+'.'+ str(next_month) for i in all_dates_next if i != 0]
                    for i in range(a.count(0)):
                        a.remove(0)
                    for i in b:
                        a.append(i)
            else:
                all_dates_now.remove(a)

    dates_represent =[]
    for i in all_dates_now:
        for o in i:
            dates_represent.append(o)

    return dates_represent


def get_schedule_day(day):
    curr_year = datetime.now().year

    year_previous = curr_year - 1
    year_next = curr_year +1

    curr_month =datetime.now().month

    all_dates_now = calendar.monthcalendar(curr_year,curr_month)


    prev_month = curr_month -1
    next_month = curr_month+1
    if prev_month == 0:

        prev_month = 12
        all_dates_previous = calendar.monthcalendar(year_previous,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]
    else:
        all_dates_previous = calendar.monthcalendar(curr_year,prev_month)
        all_dates_previous = [i[:5] for i in all_dates_previous][-1]


    all_dates_now = calendar.monthcalendar(curr_year,curr_month)
    all_dates_now = [i[:5] for i in all_dates_now]
    if next_month >12:

        next_month = 1
        all_dates_next = calendar.monthcalendar(year_next,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]
    else:
        all_dates_next = calendar.monthcalendar(curr_year,next_month)
        all_dates_next = [i[:5] for i in all_dates_next][0]


    days = ['Понеділок','Вівторок','Середа','Четвер',"П'ятниця"]


    days_calendar = []
    days_date = []
    c = 0

    all_days_month = []
    for a in all_dates_now:
        if a.count(0) != 5:
            all_days_month.append(days)

    for a in all_dates_now:
        if 0 in a:
            if a.count(0) != 5:
            
                if a == all_dates_now[0]:
                    
                    b = [str(i)+'.'+ str(prev_month) for i in all_dates_previous if i != 0]
                    for i in a:
                        if i != 0:
                            b.append(i)
                    all_dates_now[0] = b

                if a == all_dates_now[-1]:
                    
                    b = [str(i)+'.'+ str(next_month) for i in all_dates_next if i != 0]
                    for i in range(a.count(0)):
                        a.remove(0)
                    for i in b:
                        a.append(i)
            else:
                all_dates_now.remove(a)


    for i in all_dates_now:
        try:
            int_day = int(day)
            if int_day in i:
                day_index = i.index(int_day)
        except:
            if day in i:
                day_index = i.index(day)
    
    
        
    schedule_get = get_schedule()[day_index][1:]
    schedule_ = []
    c = 1
    #schedule_ = [{'index': c+1,'text': i}for i in schedule_get ]
    for i in schedule_get:
        schedule_.append({'index': c,'text':i})
        c+=1


    return schedule_

print(get_schedule_day(3))
curr_year = datetime.now().year

year_previous = curr_year - 1
year_next = curr_year +1

curr_month = datetime.now().month


def get_totaldate(date):
    global curr_year,year_previous,year_next,curr_month
    if len(date.split('.')) == 1:
        total_date = date +'.'+str(curr_month) +'.'+ str(curr_year)
    if len(date.split('.')) == 2:
        month = int(date.split('.')[1])
        if curr_month == 12 and month == 1:
            total_date = date +'.'+str(year_next)
        
        elif curr_month == 1 and month == 12:
            total_date = date +'.'+ str(year_previous)
        else:
            total_date = date +'.'+ str(curr_year)

    
    total_date = datetime.strptime(total_date,'%d.%m.%Y').date()
    return total_date


all_subjects = ['Алгебра','Англійська мова','Біологія','Географія','Геометрія','Зарубіжна література','Інформатика','Історія України','Мистецтво',"Основи здоров'я",'Правознавство','Трудове навчання','Українська література','Українська мова','Фізика','Фізична культура','Хімія']