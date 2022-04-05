from app.main import db
from app.main.utils import commit_db, eliminar_entidades, guardar_cambios
from app.main.model.parrafo import Parrafo


def guardar_parrafo(data):
    parrafo_nuevo = Parrafo(
        secuencia=data.secuencia,
        titulo=data.titulo,
        texto=data.texto,
        texto_html=data.texto_html,
        politica_id=data.politica_id
    )
    guardar_cambios(parrafo_nuevo)


def eliminar_parrafos_politica(politica_id):
    parrafos = Parrafo.query.filter_by(politica_id=politica_id).all()

    if parrafos:
        eliminar_entidades(parrafos)
        return True

    return False


def consultar_num_parrafos_politica(politica_id):
    """ Consulta el total de parrafos/secciones de una política"""
    num_parrafos = (db.session.query(Parrafo)
                    .filter(Parrafo.politica_id == politica_id).count())
    return num_parrafos
