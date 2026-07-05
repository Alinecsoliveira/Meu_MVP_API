from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Session, Pokemon
from logger import logger
from schemas.pokemon import (
    PokemonSchema,
    PokemonViewSchema,
    PokemonBuscaSchema,
    PokemonDelSchema,
    ListaPokemonsSchema,
    ErrorSchema
)
from flask_cors import CORS

# Informações da API
info = Info(title="Pokédex API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Redireciona para a documentação")
pokemon_tag = Tag(name="Pokémons", description="Cadastro e gerenciamento de Pokémons")

# Redireciona para /openapi
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# Cadastro (POST)
@app.post('/cadastrar_pokemon', tags=[pokemon_tag],
          responses={"200": PokemonViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def cadastrar_pokemon(body: PokemonSchema):
    with Session() as session:
        try:
            pokemon = Pokemon(nome=body.nome, tipo=body.tipo, nivel=body.nivel)
            logger.debug(f"Adicionando Pokémon de nome: '{pokemon.nome}'")
            session.add(pokemon)
            session.commit()
            return PokemonViewSchema.from_orm(pokemon).model_dump(), 200
        except IntegrityError:
            session.rollback()
            return {"erro": "Pokémon já cadastrado"}, 409
        except Exception as e:
            session.rollback()
            return {"erro": str(e)}, 400

# Listar todos (GET)
@app.get('/pokemons', tags=[pokemon_tag],
         responses={"200": ListaPokemonsSchema, "400": ErrorSchema})
def listar_pokemons():
    with Session() as session:
        pokemons = session.query(Pokemon).all()
        return {
            "pokemons": [PokemonViewSchema.from_orm(p).model_dump() for p in pokemons]
        }, 200

# Buscar por ID (GET)
@app.get('/buscar_pokemon', tags=[pokemon_tag],
         responses={"200": PokemonViewSchema, "404": ErrorSchema})
def buscar_pokemon(query: PokemonBuscaSchema):
    with Session() as session:
        pokemon = session.query(Pokemon).filter(Pokemon.id == query.id).first()
        if not pokemon:
            return {"erro": "Pokémon não encontrado"}, 404
        return PokemonViewSchema.from_orm(pokemon).model_dump(), 200

# Deletar (DELETE)
@app.delete('/deletar_pokemon', tags=[pokemon_tag],
            responses={"200": PokemonViewSchema, "404": ErrorSchema})
def deletar_pokemon(query: PokemonBuscaSchema):
    with Session() as session:
        pokemon = session.query(Pokemon).filter(Pokemon.id == query.id).first()
        if not pokemon:
            return {"erro": "Pokémon não encontrado"}, 404
        session.delete(pokemon)
        session.commit()
        return PokemonViewSchema.from_orm(pokemon).model_dump(), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)




