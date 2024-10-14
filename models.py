# models.py

from dataclasses import dataclass

@dataclass
class Venda:
    id_venda: int = None
    nome_produto: str = ""
    valor_produto: float = 0.0
