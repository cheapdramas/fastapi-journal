import sqlite3
import json


conn = None

curs = None
all_tables = ['History_marks','Algebra_marks','Biology_marks','Chemestry_marks','students_log','schedule','marks','homework','device_acc','teachers_log']
all_subjects= ['History','Algebra','Biology','Chemestry']
working_days = ['Понеділок','Вівторок','Середа','Четвер',"П'ятниця"]

monday_schedule = ['Українська література', 'Алгебра', 'Зарубіжна література', 'Хімія', 'Мистецтво', 'Географія', 'Історія']
tuesday_schedule= ['Українська мова', 'Зарубіжна література', 'Трудове навчання', 'Англійська мова', 'Фізкультура', 'Правознавство',None]
wednesday_schedule = ['Інформатика', 'Інформатика', 'Геометрія', 'Хімія', 'Історія', 'Фізика', 'Виховна година']
thursday_schedule = ['Українська література', 'Алгебра', 'Біологія', 'Англійська мова', 'Фізкультура', 'Фізика', 'Історія']
friday_schedule = ['Фізика', 'Українська мова', 'Геометрія', 'Англійська', 'Біологія', 'Фізкультура', 'Основи здоров’я']

schedule = [monday_schedule,tuesday_schedule,wednesday_schedule,thursday_schedule,friday_schedule]



def open_db():
    global conn,curs
    conn = sqlite3.connect('info.db',check_same_thread=False)
    curs = conn.cursor()

def close():
    curs.close()
    conn.close()

def do(request):
    open_db()   
    curs.execute(request)
    conn.commit()

def clear():
    global all_tables
    open_db()
    for i in all_tables:
        do(f'DROP TABLE IF EXISTS {i}')


    close()


def structure_create():
    do("""CREATE TABLE IF NOT EXISTS students_log(
        id INTEGER PRIMARY KEY,
        name TEXT,
        second_name TEXT,
        login TEXT,
        password TEXT,
        subgroup INTEGER)""")
    

    do('''CREATE TABLE IF NOT EXISTS teachers_log(
       id INTEGER PRIMARY KEY,
       name TEXT,
       second_name VARCHAR,
       login VARCHAR,
       password VARCHAR,
       subjects VARCHAR,
       subgroup VARCHAR,
       privilege BOOLEAN
    )''')
    
    do("""CREATE TABLE IF NOT EXISTS homework(
        
        date DATE,
        subject TEXT,
        subject_index INTEGER,
        description TEXT
        )""")

    
    do("""CREATE TABLE IF NOT EXISTS marks(
       student_id INTEGER,
       subject TEXT,
       mark INTEGER,
       reason TEXT,
       date DATE,
       time TEXT

    )""")

    
        
    

    do('''CREATE TABLE IF NOT EXISTS schedule(
       id INTEGER PRIMARY KEY,
       day TEXT,
       lesson_1 TEXT,
       lesson_2 TEXT,
       lesson_3 TEXT,
       lesson_4 TEXT,
       lesson_5 TEXT,
       lesson_6 TEXT,
       lesson_7 TEXT
    )''')
    do("""CREATE TABLE IF NOT EXISTS device_acc(
        device_id TEXT,
       log_id INTEGER,
       is_teacher_acc BOOLEAN)""")

    


    
    
    

def add_log_pass_student(name,second_name,login,password):
    open_db()
    
    curs.execute("""INSERT INTO students_log(
                name,second_name,login,password) VALUES (?,?,?,?)""",[name,second_name,login,password])
    conn.commit()
    close()

def add_log_pass_teacher(name,second_name,login,password,subjects:str,subgroup,privilege:bool=False):
    open_db()
    curs.execute('INSERT INTO teachers_log(name,second_name,login,password,subjects,subgroup,privilege) VALUES(?,?,?,?,?,?,?)',[name,second_name,login,password,subjects,subgroup,privilege])
    conn.commit()
    close()


def correcting_id_order_students():
    open_db()
    do("""SELECT name,second_name,login,password FROM students_log ORDER BY second_name""")
    

    info_by = curs.fetchall()
    
    
    curs.execute('SELECT MAX(id) FROM students_log')
    len_students = curs.fetchone()[0]
    half_len_students = int(round(len_students /2,1))
    
    
    

    do('DROP TABLE IF EXISTS students_log')
    conn.commit()
    
    do("""CREATE TABLE IF NOT EXISTS students_log(
        id INTEGER PRIMARY KEY,
        name TEXT,
        second_name TEXT,
        login TEXT,
        password TEXT,
        subgroup INTEGER)""")

    
    

    curs.executemany("""INSERT INTO students_log(name,second_name,login,password) VALUES(?,?,?,?)""",info_by)
    for i in range(1,len_students+1):
        if i <= half_len_students:
            subgroup =1
        else:
            subgroup = 2
        
        curs.execute('UPDATE students_log SET subgroup = ? WHERE id = ?',[subgroup,i])
        conn.commit()

    conn.commit()





def add_mark(id,subj,mark,reason,date,time):
    open_db()
    curs.execute('INSERT INTO marks(student_id,subject,mark,reason,date,time) VALUES(?,?,?,?,?,?)',[id,subj,mark,reason,date,time])
    conn.commit()
    close()
    
def get_marks(user_id):
    open_db()

    curs.execute(f'SELECT subject,mark FROM marks WHERE student_id == {user_id}')
    a = curs.fetchall()
    return a

def get_markndate(user_id):
    open_db()
    

    curs.execute(f'SELECT subject,mark,reason,date,time FROM marks WHERE student_id == {user_id}')
    
    
    a = curs.fetchall()
    
    return a




            

    


def schedule_fill():
    global working_days

    
    for i in schedule:  
        curs.executemany('INSERT INTO schedule(lesson_1,lesson_2,lesson_3,lesson_4,lesson_5,lesson_6,lesson_7) VALUES(?,?,?,?,?,?,?)',[i])
    id = curs.execute('SELECT id FROM schedule')
    id = curs.fetchall()
    for i in id:
        i = i[0]
        day = working_days[int(i)-1]
        curs.execute(f'UPDATE schedule SET day = ? WHERE id = ?',[day,i])
    conn.commit()
    
    

def get_schedule():
    open_db()
    
    curs.execute("SELECT day,lesson_1,lesson_2,lesson_3,lesson_4,lesson_5,lesson_6,lesson_7 FROM schedule")
    a = curs.fetchall()
    
    return a
    
    


    

def get_log_pass():
    open_db()
    curs.execute('SELECT id,login,password FROM students_log')
    a = curs.fetchall()
    
    return a

def get_names_by_id(id):
    
    open_db()
    curs.execute('SELECT name,second_name FROM students_log WHERE id = ?',[id])
    a = curs.fetchone()
    
    return a
def get_id_by_name(full_name):
    name = full_name.split(' ')[0]
    second_name = full_name.split(' ')[1]

    open_db()
    curs.execute('SELECT id FROM students_log WHERE name = ? AND second_name = ?',[name,second_name])
    return curs.fetchone()[0]




def prepare_student_info():
    do('SELECT id,name,second_name FROM students_log')
    res = curs.fetchall()
    
    return res

def add_homework(date,subject,subject_index,desc):

    open_db()
    curs.execute('INSERT INTO homework(date,subject,subject_index,description) VALUES(?,?,?,?)',[date,subject,subject_index,desc])

    conn.commit()
    close()
    
def get_homework():
    open_db()
    
    
    curs.execute('SELECT * FROM homework')
    b =curs.fetchall()
    
    return b


def get_id_name_second_name():
    open_db()
    curs.execute('SELECT id,name,second_name FROM students_log')

    b=curs.fetchall()
    return b    

def devices_id(mode,device_id,log_id= None,is_teacher=None):
    open_db()

    curs.execute('SELECT MAX(id) FROM students_log')
    len_students = curs.fetchone()[0]

    curs.execute('SELECT MAX(id) FROM teachers_log')
    len_teachers = curs.fetchone()[0]

    if mode == 'ADD' and is_teacher:
        
       
        if log_id in range(1,len_teachers+1):
          
            curs.execute('SELECT log_id FROM device_acc WHERE device_id = ? AND log_id = ? AND is_teacher_acc = 0',[device_id,log_id])
            if curs.fetchone() != None:
                curs.execute('UPDATE device_acc SET is_teacher_acc = 1 WHERE device_id = ? AND log_id = ?',[device_id,log_id])
                conn.commit()

            curs.execute('UPDATE device_acc SET log_id = ?, is_teacher_acc = 1 WHERE device_id = ?',[log_id,device_id])

            conn.commit()
            curs.execute('SELECT device_id FROM device_acc WHERE device_id = ?',[device_id])

            if curs.fetchone() == None:
                curs.execute('INSERT INTO device_acc(device_id,log_id,is_teacher_acc) VALUES(?,?,1)',[device_id,log_id])


            conn.commit()

            close()

    if mode == 'ADD' and not is_teacher:
        
        

        curs.execute('SELECT device_id FROM device_acc')

        device_id_list = curs.fetchall()
        
        if (device_id,) in device_id_list:
        
            curs.execute('UPDATE device_acc SET log_id = ?,is_teacher_acc =0 WHERE device_id = ?',[log_id,device_id])
            conn.commit()
            


           
        if (device_id,) not in device_id_list:
            curs.execute('INSERT INTO device_acc(device_id,log_id,is_teacher_acc) VALUES(?,?,0)',[device_id,log_id])
            conn.commit()
        close()

    if mode == 'CHECK':

        curs.execute('SELECT log_id,is_teacher_acc FROM device_acc WHERE device_id = ?',[device_id])
        a=curs.fetchone()
        if a!= None:
            
            return a
        else:
            return 'NO ACC'
        close()
            
        
            

        


devices_id('ADD','newid',3)
devices_id('ADD','newnew',3,True)
devices_id('ADD','newnew',4)
devices_id('ADD','newid',3)

print(devices_id('CHECK','newnew'))




def idk():
    open_db()
    curs.execute('SELECT * FROM device_acc')

    return curs.fetchall()


print(idk())





    # if mode ==  'CHECK_DEVICE':
    #     curs.execute('SELECT device_id FROM device_acc')
    #     a = curs.fetchall()
    #     if (device_id,) in a:
    #         curs.execute('SELECT log_id FROM device_acc WHERE device_id = ?',[device_id])
    #         data = curs.fetchone()[0]   
    #         return data
    #         #return curs.fetchall()
    #     if (device_id,) not in a:
    #         return 'False'
    #     close()

    
def get_news_by_id(id):
    open_db()

    curs.execute('SELECT subject,mark,reason,date,time FROM marks WHERE student_id == ?',[id])

    return curs.fetchall()


def is_there_hw(total_date,subj,subj_index,desc):
    open_db()
    try:
        check = curs.execute('SELECT subject FROM homework WHERE subject = ? AND date = ? AND subject_index = ?',[subj,total_date,subj_index])

        if check.fetchall() != []:
            curs.execute('UPDATE homework SET description = ? WHERE subject = ? AND date = ? AND subject_index = ?',[desc,subj,total_date,subj_index])
            conn.commit()
        else:
            add_homework(total_date,subj,subj_index,desc)
    except:
        print(total_date,subj,subj_index,desc)


def get_teacher_students(id_teacher):
    open_db()
    curs.execute('SELECT subgroup FROM teachers_log WHERE id = ?',[id_teacher])
    teacher_subgroup = curs.fetchone()[0]

    try:
        curs.execute('SELECT id FROM students_log WHERE subgroup = ?',teacher_subgroup)
        return curs.fetchall()

    except:
        curs.execute('SELECT id FROM students_log')
        return curs.fetchall()
    

    

def get_teachers_log_pass():

    open_db()
    curs.execute('SELECT id,login,password,privilege FROM teachers_log')
    return curs.fetchall()

def get_teacher_name_by_id(id_teacher):
    open_db()
    curs.execute('SELECT name,second_name FROM teachers_log WHERE id = ?',[id_teacher])
    return curs.fetchone()

def get_teacher_subjects_by_id(id_teacher):
    open_db()
    curs.execute('SELECT subjects FROM teachers_log WHERE id = ?',[id_teacher])
    return curs.fetchone()[0]

 



def get_teacher_privelege(id):
    open_db()

    curs.execute('SELECT privilege FROM teachers_log WHERE id = ?',[id])
    return curs.fetchone()[0]
    



def main():
   
    clear()
    structure_create()
    
    add_log_pass_student('Дарина','Матвієнко','matviy69','666jesus')
    add_log_pass_student('Альона','Гринчук','alona','roblox123')
    add_log_pass_student('Даня','Брожин','danya3','445566s')
    add_log_pass_student('Софія','Вдовцова','sofavdov','ez12')
    add_log_pass_student('Ростислав','Білецький','bileckij_123','654321re')
    add_log_pass_student('Давід','Адамян','david','123456xd')
    add_log_pass_student('Влад','Витюк','messi','ronaldo')
    add_log_pass_student('Софія','Дуднік','kick','kickmeplease')
    add_log_pass_student('Арсен','Підвашецький','ars','123')
    add_log_pass_student('Артем','Поліщук','aaart2009','2009')
    add_log_pass_student('Софія','Рогатюк','rog','123')

    add_log_pass_teacher('Олена','Анатоліївна','olenazaruba','123','Зарубіжна література','All')
    add_log_pass_teacher('Людмила','Євгеніївна','evgeniy','12356','Українська мова',1)
    add_log_pass_teacher('Надія','Михайлівна','mihay','1123','Українська мова, Українська література','All')
    add_log_pass_teacher('Тетяна','Володимирівна','solodka3','123','Інформатика',1,True)
    add_log_pass_teacher('Анатолій','Миколайович','dimamihno','123','Англійська мова',2)

    
   
    
    
   

    correcting_id_order_students()

    schedule_fill()
    
    

if __name__ == "__main__":
    main()
    