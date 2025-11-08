# Exceptions personalizadas para o projeto

class FornecedorNotFoundError(Exception):
    """Exception para erro de fornecedor não encontrado"""
    pass

class FornecedorValidationError(Exception):
    """Exception para erro de validação de fornecedor"""
    pass

class FornecedorIntegrityError(Exception):
    """Exception para erro de integridade de fornecedor"""
    pass

class FornecedorDatabaseError(Exception):
    """Exception para erro de banco de dados de fornecedor"""
    pass