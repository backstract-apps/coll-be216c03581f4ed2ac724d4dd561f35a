from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put('/users/id/')
async def put_users_id(id: int, username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], test: Annotated[str, Query(max_length=100)], test123: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, username, password, test, test123)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(id: int, name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, id, name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/')
async def get_profile(db: Session = Depends(get_db)):
    try:
        return await service.get_profile(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/id')
async def get_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profile/id/')
async def put_profile_id(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_profile_id(db, id, name, address, mobile, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profile/id')
async def delete_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/keshav/')
async def get_keshav(db: Session = Depends(get_db)):
    try:
        return await service.get_keshav(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/keshav/id')
async def get_keshav_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_keshav_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/keshav/')
async def post_keshav(id: int, test: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_keshav(db, id, test)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/keshav/id/')
async def put_keshav_id(id: int, test: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_keshav_id(db, id, test)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/keshav/id')
async def delete_keshav_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_keshav_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/')
async def get_records(db: Session = Depends(get_db)):
    try:
        return await service.get_records(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/id')
async def get_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/records/id/')
async def put_records_id(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_records_id(db, id, username, address, pincode)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/records/id')
async def delete_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/')
async def get_class(db: Session = Depends(get_db)):
    try:
        return await service.get_class(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/id')
async def get_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/class/')
async def post_class(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_class(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/class/id/')
async def put_class_id(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_class_id(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/class/id')
async def delete_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(id: int, username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], test: Annotated[str, Query(max_length=100)], test123: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, id, username, password, test, test123)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(doc: UploadFile, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, doc, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profile/')
async def post_profile(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_profile(db, id, name, address, mobile, password, email, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/records/')
async def post_records(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_records(db, id, username, address, pincode)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100, pattern='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+\\-=\\[\\]{};\':"\\\\|,.<>\\/?])[A-Za-z\\d!@#$%^&*()_+\\-=\\[\\]{};\':"\\\\|,.<>\\/?]{8,}$')], db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, username, password)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

