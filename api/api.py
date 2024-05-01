from fastapi import APIRouter
from db_scripts import *

from config.config import config

router = APIRouter(prefix = '/{password}',tags=['get_api'])


@router.get('/students_log')
async def get_students(password:str):
	if password == config['password']:
		return get_log_pass()


@router.get('/get_marks/{id}')
async def get_marks_url(password:str,id:int):
	if password == config['password']:
		return get_marks(id)
	

@router.get('/get_news/{id}')
async def get_news(password:str,id:int):
	if password == config['password']:
		return get_news_by_id(id)


@router.get('/get_hw')
async def get_hw(password:str):
	if password == config['password']:
		return get_homework()

@router.get('/schedule')
async def get_schedule_url(password:str):
	if password == config['password']:
		return get_schedule()
	


@router.get('/get_teacher_students/{id_teacher}')
async def get_teacher_students_url(password:str,id_teacher:int):
	if password == config['password']:

		students = get_teacher_students(id_teacher)
		students_name = []
		for i in students:
			student_list = []
			i = i[0]
			student_list.append(i)
			for item in get_names_by_id(i):
				student_list.append((item))
			students_name.append(student_list)
		return students_name
	

@router.get('/get_subjects_teacher/{id_teacher}')
async def get_teacher_subjects_url(password:str,id_teacher:int):
	if password == config['password']:
		return get_teacher_subjects_by_id(id_teacher)
	

@router.get('/teachers_log_pass')
def get_teacher_log_password(password: str):
	if password ==  config['password']:
		return get_teachers_log_pass()
	
   
       
    
        



  