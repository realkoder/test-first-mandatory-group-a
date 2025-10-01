from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TEST TEST TEST"}


@app.get("/cpr")
async def generate_cpr():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/name-gender")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/name-gender-dob")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/cpr-name-gender")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/cpr-name-gender-dob")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/address")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/phone")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/person")
async def get_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/person&n={number_of_fake_persons}")
async def get_person(number_of_fake_persons: int):
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")