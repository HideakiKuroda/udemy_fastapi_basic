from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime

router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact])   #一覧表示
async def get_contact_all():
    #　test でデータを登録
    dammy_date = datetime.now()
    return [
        contact_schema.Contact(
            id=1, 
            name="山田", 
            email="taro@example.com", 
            url="http://example.com", 
            gender=1, massage="Hello", 
            is_enabled=True, 
            created_at=dammy_date
            )
    ]
    

@router.post("/contacts", response_model=contact_schema.Contact)  #保存
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.get("/contacts/{contact_id}", response_model=contact_schema.Contact)   #詳細表示
async def get_contact(contact_id: int):
    return contact_schema.Contact(id=contact_id)  
    

@router.put("/contacts/{contact_id}", response_model=contact_schema.Contact )   #更新
async def update_contact(contact_id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{contact_id}", response_model=contact_schema.Contact)   #削除
async def delete_contact(contact_id: int):
    return 