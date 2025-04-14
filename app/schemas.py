from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    imagem: str

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
