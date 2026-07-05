# Pokédex API

Este pequeno projeto faz parte do trabalho de conclusão da Disciplina **Desenvolvimento Full Stack Básico** 

API desenvolvida em Python com Flask para gerenciar Pokémons em uma Pokédex.  
Permite cadastrar, listar, buscar e excluir Pokémons.

## 🚀 Funcionalidades
- `POST /cadastrar_pokemon` → Cadastrar novo Pokémon
- `GET /pokemons` → Listar todos os Pokémons
- `GET /buscar_pokemon?id=...` → Buscar Pokémon por ID
- `DELETE /deletar_pokemon?id=...` → Excluir Pokémon por ID

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

O servidor estará disponível em http://127.0.0.1:5000
