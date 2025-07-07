from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def put_users_id(
    db: Session, id: int, username: str, password: str, test: str, test123: str
):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "test": test,
            "test123": test123,
            "password": password,
            "username": username,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def put_students_id(db: Session, id: int, name: str, age: str):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {"id": id, "age": age, "name": name}.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_profile(db: Session):

    query = db.query(models.Profile)

    profile_all = query.all()
    profile_all = (
        [new_data.to_dict() for new_data in profile_all] if profile_all else profile_all
    )
    res = {
        "profile_all": profile_all,
    }
    return res


async def get_profile_id(db: Session, id: int):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    profile_one = query.first()

    profile_one = (
        (
            profile_one.to_dict()
            if hasattr(profile_one, "to_dict")
            else vars(profile_one)
        )
        if profile_one
        else profile_one
    )

    headers = {}

    payload = {"asd": profile_one}
    apiResponse = requests.put(
        "https://api.beemerbenzbentley.site/platform/docs",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    asdas = apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    res = {
        "profile_one": profile_one,
    }
    return res


async def put_profile_id(
    db: Session,
    id: int,
    name: str,
    address: str,
    mobile: str,
    password: str,
    email: str,
):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))
    profile_edited_record = query.first()

    if profile_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "email": email,
            "mobile": mobile,
            "address": address,
            "password": password,
        }.items():
            setattr(profile_edited_record, key, value)

        db.commit()
        db.refresh(profile_edited_record)

        profile_edited_record = (
            profile_edited_record.to_dict()
            if hasattr(profile_edited_record, "to_dict")
            else vars(profile_edited_record)
        )
    res = {
        "profile_edited_record": profile_edited_record,
    }
    return res


async def delete_profile_id(db: Session, id: int):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        profile_deleted = record_to_delete.to_dict()
    else:
        profile_deleted = record_to_delete
    res = {
        "profile_deleted": profile_deleted,
    }
    return res


async def get_keshav(db: Session):

    query = db.query(models.Keshav)

    keshav_all = query.all()
    keshav_all = (
        [new_data.to_dict() for new_data in keshav_all] if keshav_all else keshav_all
    )
    res = {
        "keshav_all": keshav_all,
    }
    return res


async def get_keshav_id(db: Session, id: int):

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))

    keshav_one = query.first()

    keshav_one = (
        (keshav_one.to_dict() if hasattr(keshav_one, "to_dict") else vars(keshav_one))
        if keshav_one
        else keshav_one
    )

    res = {
        "keshav_one": keshav_one,
    }
    return res


async def post_keshav(db: Session, id: int, test: str):

    record_to_be_added = {"id": id, "test": test}
    new_keshav = models.Keshav(**record_to_be_added)
    db.add(new_keshav)
    db.commit()
    db.refresh(new_keshav)
    keshav_inserted_record = new_keshav.to_dict()

    res = {
        "keshav_inserted_record": keshav_inserted_record,
    }
    return res


async def put_keshav_id(db: Session, id: int, test: str):

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))
    keshav_edited_record = query.first()

    if keshav_edited_record:
        for key, value in {"id": id, "test": test}.items():
            setattr(keshav_edited_record, key, value)

        db.commit()
        db.refresh(keshav_edited_record)

        keshav_edited_record = (
            keshav_edited_record.to_dict()
            if hasattr(keshav_edited_record, "to_dict")
            else vars(keshav_edited_record)
        )
    res = {
        "keshav_edited_record": keshav_edited_record,
    }
    return res


async def delete_keshav_id(db: Session, id: int):

    query = db.query(models.Keshav)
    query = query.filter(and_(models.Keshav.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        keshav_deleted = record_to_delete.to_dict()
    else:
        keshav_deleted = record_to_delete
    res = {
        "keshav_deleted": keshav_deleted,
    }
    return res


async def get_records(db: Session):

    query = db.query(models.Records)

    records_all = query.all()
    records_all = (
        [new_data.to_dict() for new_data in records_all] if records_all else records_all
    )
    res = {
        "records_all": records_all,
    }
    return res


async def get_records_id(db: Session, id: int):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    records_one = query.first()

    records_one = (
        (
            records_one.to_dict()
            if hasattr(records_one, "to_dict")
            else vars(records_one)
        )
        if records_one
        else records_one
    )

    res = {
        "records_one": records_one,
    }
    return res


async def put_records_id(
    db: Session, id: int, username: str, address: str, pincode: str
):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))
    records_edited_record = query.first()

    if records_edited_record:
        for key, value in {
            "id": id,
            "address": address,
            "pincode": pincode,
            "username": username,
        }.items():
            setattr(records_edited_record, key, value)

        db.commit()
        db.refresh(records_edited_record)

        records_edited_record = (
            records_edited_record.to_dict()
            if hasattr(records_edited_record, "to_dict")
            else vars(records_edited_record)
        )
    res = {
        "records_edited_record": records_edited_record,
    }
    return res


async def delete_records_id(db: Session, id: int):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        records_deleted = record_to_delete.to_dict()
    else:
        records_deleted = record_to_delete
    res = {
        "records_deleted": records_deleted,
    }
    return res


async def get_class(db: Session):

    query = db.query(models.Class)

    class_all = query.all()
    class_all = (
        [new_data.to_dict() for new_data in class_all] if class_all else class_all
    )
    res = {
        "class_all": class_all,
    }
    return res


async def get_class_id(db: Session, id: int):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    class_one = query.first()

    class_one = (
        (class_one.to_dict() if hasattr(class_one, "to_dict") else vars(class_one))
        if class_one
        else class_one
    )

    res = {
        "class_one": class_one,
    }
    return res


async def post_class(db: Session, id: int, subject: str):

    record_to_be_added = {"id": id, "subject": subject}
    new_class = models.Class(**record_to_be_added)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    class_inserted_record = new_class.to_dict()

    res = {
        "class_inserted_record": class_inserted_record,
    }
    return res


async def put_class_id(db: Session, id: int, subject: str):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))
    class_edited_record = query.first()

    if class_edited_record:
        for key, value in {"id": id, "subject": subject}.items():
            setattr(class_edited_record, key, value)

        db.commit()
        db.refresh(class_edited_record)

        class_edited_record = (
            class_edited_record.to_dict()
            if hasattr(class_edited_record, "to_dict")
            else vars(class_edited_record)
        )
    res = {
        "class_edited_record": class_edited_record,
    }
    return res


async def delete_class_id(db: Session, id: int):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        class_deleted = record_to_delete.to_dict()
    else:
        class_deleted = record_to_delete
    res = {
        "class_deleted": class_deleted,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(
    db: Session, id: int, username: str, password: str, test: str, test123: str
):

    record_to_be_added = {
        "id": id,
        "test": test,
        "test123": test123,
        "password": password,
        "username": username,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def post_students(db: Session, doc: UploadFile, request: Request):
    header_authorization: str = request.headers.get("header-authorization")

    headers = {}

    payload = {"doc": doc}
    apiResponse = requests.post(
        "https://cc1fbde45ead-in-south-01.backstract.io/sleepy-perlman-affa1684582511f0a7a02a3957a8b30123/api/file_upload",
        headers=headers,
        json=payload if "formData" == "raw" else None,
    )
    test_api2 = apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    res = {
        "test1": test_api2,
    }
    return res


async def post_profile(
    db: Session,
    id: int,
    name: str,
    address: str,
    mobile: str,
    password: str,
    email: str,
    request: Request,
):
    header_authorization: str = request.headers.get("header-authorization")

    record_to_be_added = {
        "id": id,
        "name": name,
        "email": email,
        "mobile": mobile,
        "address": address,
        "password": password,
    }
    new_profile = models.Profile(**record_to_be_added)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    profile_inserted_record = new_profile.to_dict()

    headers = {"authorization": header_authorization}

    payload = {"workspace_id": name, "collection_id": name}
    apiResponse = requests.get(
        "https://api.beemerbenzbentley.site/sigma/api/v1/api_builder/?api_id=api_3cd711dfa2214c4685385fd6a56213e8",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    test_apis = apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text

    headers = {"authorization": header_authorization}
    headers["Authorization"] = (
        "Bearer Bearer v4.public.eyJlbWFpbF9pZCI6ICJzaGl2YW10ZXN0aW5nN0BnbWFpbC5jb20iLCAidXNlcl9pZCI6ICJiZjJmOTAwZGQzYjE0ZTQ4OTk5NjljZjZlMzkzN2NkMCIsICJvcmdfaWQiOiAiTkEiLCAic3RhdGUiOiAic2lnbnVwIiwgInJvbGVfbmFtZSI6ICJOQSIsICJyb2xlX2lkIjogIk5BIiwgInBsYW5faWQiOiAiMTAxIiwgImFjY291bnRfdmVyaWZpZWQiOiAiMSIsICJhY2NvdW50X3N0YXR1cyI6ICIwIiwgInVzZXJfbmFtZSI6ICJzaGl2YW0gc3JpdmFzdGF2YSIsICJzaWdudXBfcXVlc3Rpb24iOiAzLCAiZXhwIjogMzUwMzk3NjMxOC4zMTk0NzksICJleHBpcnlfdGltZSI6IDM1MDM5NzYzMTh9a5yY-3hBj7K6G4ZXGUcGPHJMUi60WSe71ix8oRPGsYQyUN23o75DeMm0X5vsx2RcH9ksNot6dvD3HYWlBksOBA"
    )
    payload = {"workspace_id": address, "workspace_name": address}
    apiResponse = requests.get(
        "https://api.beemerbenzbentley.site/sigma/api/v1/workspace/list",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    user_details = (
        apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    )
    res = {
        "profile_inserted_record": profile_inserted_record,
        "test": test_apis,
        "test1": user_details,
    }
    return res


async def post_records(db: Session, id: int, username: str, address: str, pincode: str):

    record_to_be_added = {
        "id": id,
        "address": address,
        "pincode": pincode,
        "username": username,
    }
    new_records = models.Records(**record_to_be_added)
    db.add(new_records)
    db.commit()
    db.refresh(new_records)
    records_inserted_record = new_records.to_dict()

    user_list = []  # Creating new list

    # Add element to the list 'user_list'
    user_list.insert(0, username)

    # Get the length of the list 'user_list'
    id = len(user_list)
    res = {
        "records_inserted_record": records_inserted_record,
        "test1": user_list,
    }
    return res


async def post_login(db: Session, username: str, password: str):

    query = db.query(models.Users)
    query = query.filter(
        and_(models.Users.username == username, models.Users.password == password)
    )

    login = query.first()

    login = (
        (login.to_dict() if hasattr(login, "to_dict") else vars(login))
        if login
        else login
    )

    res = {
        "login": login,
    }
    return res
