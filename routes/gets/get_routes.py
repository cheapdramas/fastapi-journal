from fastapi import APIRouter,Request,Form,Depends,HTTPException
from fastapi.responses import RedirectResponse
from http_basic import HTTPBasicCredentials,HTTPBasic
from fastapi.templating import Jinja2Templates
from db_scripts import get_log_pass,get_id_name_second_name,get_marks,get_news_by_id,get_homework,get_schedule
from pathlib import Path
from ..componentCode import homework_days_represent,all_subjects
from pydantic import BaseModel
from starlette_context import context,middleware,plugins
from typing import Annotated
from config.config import config


router = APIRouter()
PATH = Path(__file__).parent.parent.parent
print(PATH)
templates = Jinja2Templates(directory=f'{PATH}/templates')


security = HTTPBasic()

@router.get('/add_marks')
async def add_marks_url(request: Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):


    
    studets_list = []
    for i in get_id_name_second_name():
       studets_list.append([i[0],i[1] +' ' + i[2]])
    marks_list = [i for i in range(1,13)]



    return templates.TemplateResponse('add_mark.html',{'request':request,'marks_list' : marks_list,'student_list' : studets_list,'subj_list': all_subjects,'name':'idk'})
   
@router.get('/add_homework')
async def add_homework_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    dates_represent = homework_days_represent()

    return templates.TemplateResponse('add_homework.html',{'request': request,'date_list':dates_represent,'name':'homework'})


@router.get('/get_dates_represent')
async def get_dates_represent_url():

    return homework_days_represent()
