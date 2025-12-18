import requests
import json
from modelos import Comment
from datos import insertar_objeto
from servicios import get_comments_api
from auxiliares import url_comments

def obtener_data_comentarios():
    """Obtiene y procesa comentarios de la API"""
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
        print("Problemas al procesar su solicitud...")

def crear_comentario(numero, nombre, correo, contenido, id_post):
    """Crea un comentario en JSONPlaceholder y en la BD local"""
    comentario = Comment(
        id=numero,
        name=nombre,
        email=correo,
        body=contenido,
        postId=id_post
    )
    try:
        # URL de JSONPlaceholder para comentarios
        url = "https://jsonplaceholder.typicode.com/comments"
        
        # Datos del comentario en formato JSON
        datos_comentario = {
            "name": nombre,
            "email": correo,
            "body": contenido,
            "postId": id_post
        }
        
        # Realizar POST a JSONPlaceholder
        response = requests.post(
            url, 
            json=datos_comentario,
            headers={'Content-Type': 'application/json'}
        )
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 201:
            comentario_creado = response.json()
            print(f"Comentario creado con ID: {comentario_creado.get('id')}")
            
            # Insertar en la base de datos local
            id_comentario = insertar_objeto(comentario)
            return id_comentario
        else:
            print(f"Error al crear comentario: {response.status_code}")
            return None
            
    except Exception as error:
        print(f'Error al guardar el comentario: {error}')
        return None

def borrar_comentario(id_comentario):
    """Elimina un comentario de JSONPlaceholder y de la BD local"""
    from datos import eliminar_objeto_por_id
    try:
        # URL de JSONPlaceholder para eliminar comentario
        url = f"https://jsonplaceholder.typicode.com/comments/{id_comentario}"
        
        # Realizar DELETE a JSONPlaceholder
        response = requests.delete(url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print(f"Comentario {id_comentario} eliminado de JSONPlaceholder")
            
            # Eliminar de la base de datos local
            resultado = eliminar_objeto_por_id(Comment, id_comentario)
            return resultado
        else:
            print(f"Error al eliminar comentario: {response.status_code}")
            return False
            
    except Exception as error:
        print(f'Error al eliminar el comentario: {error}')
        return False

def actualizar_comentario(id_comentario, nombre=None, correo=None, contenido=None, id_post=None):
    """Actualiza un comentario en JSONPlaceholder"""
    try:
        # URL de JSONPlaceholder para actualizar comentario
        url = f"https://jsonplaceholder.typicode.com/comments/{id_comentario}"
        
        # Preparar datos a actualizar
        datos_actualizacion = {}
        if nombre:
            datos_actualizacion['name'] = nombre
        if correo:
            datos_actualizacion['email'] = correo
        if contenido:
            datos_actualizacion['body'] = contenido
        if id_post:
            datos_actualizacion['postId'] = id_post
        
        # Realizar PUT a JSONPlaceholder
        response = requests.put(
            url,
            json=datos_actualizacion,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            comentario_actualizado = response.json()
            print(f"Comentario {id_comentario} actualizado en JSONPlaceholder")
            return comentario_actualizado
        else:
            print(f"Error al actualizar comentario: {response.status_code}")
            return None
            
    except Exception as error:
        print(f'Error al actualizar el comentario: {error}')
        return None

def listar_comentarios(filtro_post_id=None):
    """Lista comentarios de JSONPlaceholder"""
    try:
        url = "https://jsonplaceholder.typicode.com/comments"
        
        if filtro_post_id:
            url = f"{url}?postId={filtro_post_id}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            comentarios = response.json()
            print(f"\nTotal de comentarios: {len(comentarios)}")
            return comentarios
        else:
            print(f"Error al obtener comentarios: {response.status_code}")
            return None
            
    except Exception as error:
        print(f'Error al listar comentarios: {error}')
        return None

def buscar_comentario_por_id(id_comentario):
    """Busca un comentario específico por su ID"""
    try:
        url = f"https://jsonplaceholder.typicode.com/comments/{id_comentario}"
        response = requests.get(url)
        
        if response.status_code == 200:
            comentario = response.json()
            return comentario
        else:
            print(f"Comentario no encontrado: {response.status_code}")
            return None
            
    except Exception as error:
        print(f'Error al buscar comentario: {error}')
        return None