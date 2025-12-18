import requests
import json
from modelos import Comment
from datos import insertar_objeto
from .negocio_posts import crear_publicacion
from servicios import get_comments_api




def obtener_data_comentarios(url):
    comentarios = get_comments_api()
    if comentarios:
        for comentario in comentarios:
            crear_comentario(
                comentario['id'],
                comentario['name'],
                comentario['email'],
                comentario['body'],
                comentario['postId']
            )
    else:
        print(
            f"Problemas al procesar su solicitud...")


def crear_comentario(numero, nombre, correo, contenido, id_post):
    comentario = Comment(
        id=numero,
        name=nombre,
        email=correo,
        body=contenido,
        postId=id_post
    )
    try:
        id_comentario = insertar_objeto(comentario)
        return id_comentario
    except Exception as error:
        print(f'Error al guardar al usuario: {error}')

def borrar_comentario(id_comentario):
    from datos import eliminar_objeto_por_id
    try:
        resultado = eliminar_objeto_por_id(Comment, id_comentario)
        return resultado
    except Exception as error:
        print(f'Error al eliminar el comentario: {error}')
        return False