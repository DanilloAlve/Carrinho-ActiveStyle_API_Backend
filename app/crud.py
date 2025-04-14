from sqlalchemy.orm import Session
from . import models, schemas

def get_produtos(db: Session):
    return db.query(models.Produto).all()

def add_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
    db_produto = db.query(models.Produto).get(produto_id)
    if db_produto:
        for attr, value in produto.dict().items():
            setattr(db_produto, attr, value)
        db.commit()
        db.refresh(db_produto)
    return db_produto

def delete_produto(db: Session, produto_id: int):
    db_produto = db.query(models.Produto).get(produto_id)
    if db_produto:
        db.delete(db_produto)
        db.commit()
    return db_produto
