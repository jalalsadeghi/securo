from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from src.database import get_db
from src.models import User
from src.schemas import UserCreate, UserRead
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/users", tags=["Users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserRead)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        first_name=user.first_name,
        family_name=user.family_name,
        email=user.email,
        phone_number=user.phone_number,
        password_hash=hashed_password,
        company=user.company,
        country=user.country
    )

    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    return new_user
