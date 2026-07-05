from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from model.pokemon import Pokemon

class PokemonSchema(BaseModel):
    """Define como um novo Pokémon deve ser representado"""
    nome: str = "Pikachu"
    tipo: str = "Elétrico"
    nivel: Optional[int] = 5

class PokemonBuscaSchema(BaseModel):
    """Define a estrutura para buscar um Pokémon pelo ID"""
    id: int

class ListaPokemonsSchema(BaseModel):
    """Define como uma listagem de Pokémons será retornada"""
    pokemons: List[PokemonSchema]

def apresenta_pokemons(pokemons: List[Pokemon]):
    """Retorna uma representação dos Pokémons seguindo o schema definido"""
    result = []
    for p in pokemons:
        result.append({
            "nome": p.nome,
            "tipo": getattr(p, "tipo", None),
            "nivel": getattr(p, "nivel", None),
        })
    return {"pokemons": result}

class PokemonViewSchema(BaseModel):
    """Define como um Pokémon será retornado"""
    id: int = 1
    nome: str = "Pikachu"
    tipo: str = "Elétrico"
    nivel: Optional[int] = 5

    model_config = ConfigDict(from_attributes=True)

class PokemonDelSchema(BaseModel):
    """Define a estrutura do dado retornado após uma requisição de remoção"""
    message: str
    nome: str

def apresenta_pokemon(pokemon: Pokemon):
    """Retorna uma representação de um Pokémon seguindo o schema definido"""
    return {
        "id": pokemon.id,
        "nome": pokemon.nome,
        "tipo": getattr(pokemon, "tipo", None),
        "nivel": getattr(pokemon, "nivel", None)
    }

class ErrorSchema(BaseModel):
    """Define como será a estrutura de uma mensagem de erro."""
    erro: str



