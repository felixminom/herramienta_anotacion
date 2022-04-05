from app.main import db
from app.main.model.lista_negra import TokenListaNegra
from backend.app.main.utils import guardar_cambios


def guardar_token(token, usuario_id):
    """ Guarda un token invalido en la tabla TokenListaNegra"""
    token_lista_negra = TokenListaNegra(token=token, usuario_id=usuario_id)
    try:
        guardar_cambios(token_lista_negra)
        response_object = {
            'estado': 'exito',
            'mensaje': 'Sesion cerrada exitosamente'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'estado': 'exito',
            'mensaje': e
        }
        return response_object, 400
