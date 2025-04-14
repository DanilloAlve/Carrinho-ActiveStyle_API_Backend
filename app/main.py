from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois pode restringir para http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency para obter o DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    return crud.get_produtos(db)

@app.post("/produtos")
def adicionar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.add_produto(db, produto)

@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.update_produto(db, produto_id, produto)

@app.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    return crud.delete_produto(db, produto_id)
