from app.services.person_service import generate_person

async def generate_persons(count: int):
    if not 2 <= count <= 100:
        raise ValueError("Count must be between 2 and 100")
    results = []
    for _ in range(count):
        person = await generate_person()
        results.append(person)
    return results