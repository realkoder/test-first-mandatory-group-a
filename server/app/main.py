from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status

from app.db import init_db
from app.models.postal_code import PostalCode
from app.services.name_service import get_random_name_gender
from app.services.cpr_service import get_random_cpr_number


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("🚀 STARTUP: initializing DB...")
    await init_db()
    yield
    print("🛑 SHUTDOWN")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "TEST TEST TEST"}


@app.get("/cpr", status_code=status.HTTP_200_OK)
async def generate_cpr():
    result = await get_random_cpr_number()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No cpr data available"
        )
    return result

@app.get("/name-gender", status_code=status.HTTP_200_OK)
async def get_name_gender():
    result = await get_random_name_gender()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No names available in dataset"
        )
    return result


@app.get("/name-gender-dob", status_code=status.HTTP_200_OK)
async def get_name_gender_dob():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/cpr-name-gender", status_code=status.HTTP_200_OK)
async def get_cpr_name_gender():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/cpr-name-gender-dob", status_code=status.HTTP_200_OK)
async def get_cpr_name_gender_dob():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/address", status_code=status.HTTP_200_OK)
async def get_address():
    return await PostalCode.all()


@app.get("/phone", status_code=status.HTTP_200_OK)
async def get_phone():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/person", status_code=status.HTTP_200_OK)
async def get_person():
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")


@app.get("/person&n={number_of_fake_persons}", status_code=status.HTTP_200_OK)
async def get_multiple_persons(number_of_fake_persons: int):
    raise HTTPException(status_code=500, detail="IMPLEMENT ME")
