from fastapi import APIRouter,Form,status,Depends
from db_scripts import *
from schemas.get_name_by_id import NameById
from typing import Optional
from fastapi.responses import RedirectResponse
from datetime import date,datetime
import pytz
from config.config import config

from schemas.device_schema import Check_device,Add_device
from ..componentCode import get_work_days,get_schedule_day,get_totaldate
IST = pytz.timezone('Europe/Kiev')
from typing import Annotated
from schemas.id_teacher_schema import IdScheme
from schemas.add_mark_journal_scheme import AddMarkScheme
from schemas.add_hw_journal_scheme import AddHwJournalScheme
from schemas.add_device_schema import AddDeviceScheme


router = APIRouter()

@router.post('/{password}/get_names_id/{id}')
async def get_names_by_id_api(id: int):
    return get_names_by_id(id)


    



@router.post('/add_marks_post')
async def send_info_to_db(
    student:Annotated[int,Form()],
    subject:Annotated[int,Form()],
    mark:Annotated[int,Form()],
    reason:Annotated[str,Form()] = None
):
    try:
        if int(reason):
            reason = None

    except:
        pass
    all_subjects = ['Алгебра','Англійська мова','Біологія','Географія','Геометрія','Зарубіжна література','Інформатика','Історія України','Мистецтво',"Основи здоров'я",'Правознавство','Трудове навчання','Українська література','Українська мова','Фізика','Фізична культура','Хімія']
    date_ = datetime.now(IST).date()
    time = str(datetime.now(IST)).split(' ')[1].split('.')[0].split(':')[0]+':'+ str(datetime.now(IST)).split(' ')[1].split('.')[0].split(':')[1]
    subject = all_subjects[int(subject)]
    add_mark(student,subject,mark,reason,date_,time)

    return RedirectResponse('/add_marks',status_code=status.HTTP_303_SEE_OTHER)
    


@router.post('/add_marks_journal')
async def add_marks_journal(
    info_mark :AddMarkScheme
):
    info_mark.student = get_id_by_name(info_mark.student)
    date_ = datetime.now(IST).date()
    time = str(datetime.now(IST)).split(' ')[1].split('.')[0].split(':')[0]+':'+ str(datetime.now(IST)).split(' ')[1].split('.')[0].split(':')[1]
    add_mark(info_mark.student,info_mark.subject,info_mark.mark,info_mark.reason,date=date_,time=time)

@router.post('/schedule_day')
async def schedule_day(option=Form()):


    return get_schedule_day(option)



@router.post('/add_homework_done',response_class=RedirectResponse)
async def homework_done(
    date: Annotated[str,Form()],
    subjects: Annotated[str,Form()],
    hw_input:Annotated[str,Form()] = None
    
    ):
   
    is_there_hw(total_date=get_totaldate(date),subj=get_schedule_day(date)[int(subjects)-1]['text'],subj_index=subjects,desc=hw_input)
    return RedirectResponse('/add_homework',status_code = status.HTTP_303_SEE_OTHER)

@router.post('/add_homework_journal')
async def homework_done_journal(
    hw: AddHwJournalScheme
):
    total_date = get_totaldate(hw.date)

    subject_index = hw.subject
    
    index_subj = [i['text'] ==hw.subject for i in get_schedule_day(int(hw.date))].index(True) +1
    is_there_hw(total_date=total_date,subj=hw.subject,subj_index=index_subj,desc=hw.homework)
    

    # except Exception as exception:
    #     print('asd')

   

    
    
    


@router.post('/check_device')
async def check_device_url(device: Check_device):
    a = devices_id('CHECK',device.device)
    if bool(a[1]):
        a = (a[0],a[1],get_teacher_privelege(a[0]))
    return a

@router.post('/{password}/add_device')
async def add_device_url(password:str,device:AddDeviceScheme):
    if password == config['password']:
        devices_id('ADD',device.device_id,device.log_id,device.is_teacher)







@router.post('/teacher_name')
async def get_teacher_name_url(password:str,id:IdScheme):
    if password == config['password']:
        return get_teacher_name_by_id(id.id)






    
