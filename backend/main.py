from fastapi import FastAPI

from backend.api.routes.fornecedores import router as fornecedores_router

app = FastAPI(
    title='Agent Buy - API de Fornecedores',
    description='API para gerenciamento de fornecedores',
    version='1.0.0'
)

app.include_router(fornecedores_router)

#Rota Raiz
@app.get('/')
def read_root():
    return {'message': 'API de Fornecedores'}