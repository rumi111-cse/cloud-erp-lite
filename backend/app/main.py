from fastapi import FastAPI
from app.core.database import engine
from app.models.base import Base
from app.routes import auth, user, organization, product
from .api.v1 import products

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(organization.router, prefix="/organizations", tags=["Organizations"])
app.include_router(product.router, prefix="/products", tags=["Products"])
