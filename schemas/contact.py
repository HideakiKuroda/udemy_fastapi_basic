from pydantic import BaseModel, Field, EmailStr,HttpUrl
from datetime import datetime

class Contact(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50) 
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    # url: HttpUrl | None は　送信が必須でnullも許可
    # url: HttpUrl | None = Field(default=None) は　任意で送信が可能
    # url: HttpUrl | None = None も　任意で送信が可能
    gender: int = Field(..., strict=True, ge=0, le=2) # ge=0, le=2 0以上2以下
    massage: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    created_at: datetime



# Field(..., ...) の ... は「必須（required）」という意味です。

# Pydantic では ...（Ellipsis）を “このフィールドはデフォルト値がなく、入力で必ず渡されるべき” というマーカーとして扱います。
# 逆に 必須にしたくない（任意にしたい） 場合は、型を | None（または Optional[...]）にしたうえで、= None や Field(default=None) のように デフォルト値 を付けます。
# 補足：

# id: int のように「型注釈だけでデフォルトが無い」フィールドも、同様に必須になります。
# url: HttpUrl | None = Field(default=None) は「任意」です（None を許し、未指定でもOK）。

# SQLModel の Field も中身は Pydantic の Field なので、Field(...) の ... は「必須」の意味になります。
# ただし SQLModel（特に table=True のモデル）では、次の点が少しだけ “見え方” を変えます。
# API入力としての必須/任意（Pydantic側）

# 必須: デフォルト無し（例: name: str / name: str = Field(min_length=2)）
# 任意: | None ＋ デフォルトあり（例: url: HttpUrl | None = None / Field(default=None)）
# Field(...) は「必須」を明示する書き方（Pydanticと同じ）
# DB列としての NULL 可/不可（SQLAlchemy側）

# Optional（| None）だと基本 nullable=True になりやすく、str のように None を許さない型だと nullable=False になりやすい、という “DB制約” 側の意味も絡みます。
# よくある例（SQLModelのテーブル）:

# id: int | None = Field(default=None, primary_key=True) は「入力では未指定OK（自動採番想定）」という理由で default=None がよく使われます。
# name: str は「必須」になります（Field(...) を書かなくても必須）。