from typing import Annotated

from fastapi import Depends

from src.utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDepends = Annotated[IUnitOfWork, Depends(UnitOfWork)]
