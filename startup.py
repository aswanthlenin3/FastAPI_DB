from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/home_page")
def welcome_home():
    return {"message": "Hello World"}

@app.get("/get-data/{_id}")
def get_data(_id: int):
    with open("sample_db.json", "r") as f:
        _data = json.load(f)
    for rec in _data:
        if rec["_id"] == _id:
            return {"record_found": rec}
    return {"message": "Not Found"}


@app.put("/insert-data/")
async def insert_data(request: Request):
    payload = await request.json()
    with open('sample_db.json' , 'r') as f:
        _data = json.load(f)
    for rec in _data:
        if rec['_id'] == payload['_id']:
            return "Record already Exists"
        _data.append(payload)
        with open('sample_db.json' , 'w') as f:
            json.dump(_data , f , indent = 2)
        return 'Data Has been Updated'
@app.post('/update-data')
async def update_data(request : Request):
    payload = await request.json()
    with open('sample.json()' , 'r') as f:
        _data = json.load(f)
        for res in _data:
            if res['_id'] == payload['_id']:
                res['name'] = payload['name']
                res['age'] = payload['age']
                res['city'] = payload['city']
                return "Data Updated Successfully"
        return 'Unsuccessful Update' 



if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8000,
    debug = True)
