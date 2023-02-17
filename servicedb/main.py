from database import db
from fastapi import FastAPI, Request
import subprocess
import time 

time.sleep(10)


app = FastAPI()

@app.on_event("startup")
async def startup():
    subprocess.Popen(['python3', 'worker.py'])
    await db.connect()
    query = '''CREATE TABLE IF NOT EXISTS `appeals_db`.`appeals_table` (
                `author_id` INT NOT NULL AUTO_INCREMENT ,
                `last_name` VARCHAR(255) NOT NULL ,
                `first_name` VARCHAR(255) NOT NULL ,
                `patronymic_name` VARCHAR(255) NOT NULL ,
                `phone_number` VARCHAR(255) NOT NULL ,
                `text_area` TEXT NOT NULL ,
                PRIMARY KEY (`author_id`)) ENGINE = InnoDB; 
        '''
    await db.execute(query=query)

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.get('/')
async def index():
    query = 'SELECT * FROM appeals_table'
    res = await db.fetch_all(query=query)
    return res

@app.post("/appeal")
async def getInformation(info : Request):
    req_info = await info.json()
    query = notes.insert()
    values = {  "last_name": req_info['lname'],
                "first_name": req_info['fname'],
                "patronymic_name": req_info['pname'],
                "phone_number": req_info['phone'],
                "text_area": req_info['message']
            }
    await db.execute(query=query, values=values)

    return {
        "status" : "SUCCESS",
        "data" : req_info
    }
