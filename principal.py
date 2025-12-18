from negocio import (
    registrar_usuario,
    iniciar_sesion,
    listado_publicaciones,
    crear_publicacion,
    eliminar_publicacion,
    crear_comentario,
    crear_compania,
    
)
from interfaces_usuario import menu_inicial
from auxiliares import validar_correo
from servicios.serper import busqueda
from datos.obtener_datos import obtener_listado_objetos, eliminar_objeto_por_id
from modelos.modelos import Comment, Company
from negocio.negocio_comments import borrar_comentario
# obtener_data_usuarios_api(url_usuarios)
# listado_usuarios_db()
# crear_user_api(url_usuarios)
# eliminar_user_api(url_usuarios)
# obtener_data_publicaciones(url_publicaciones)
# listado_publicaciones()
# registrar_usuario()


def app():
    while True:
        menu_inicial()
        opcion_inicial = input('Seleccione su opción [0-3]: ')
        if opcion_inicial == '1':
            registrar_usuario()
        elif opcion_inicial == '2':
            if iniciar_sesion() == True:
                print('Sesión iniciada. Accediendo al menú de sesión...')
                session_active = True
                while session_active:
                    print('\n--- Menú de Sesión ---')
                    print('[1] Posts')
                    print('[2] Comments')
                    print('[3] Companies')
                    print('[0] Cerrar sesión')
                    recurso = input('Seleccione recurso [0-3]: ')
                    if recurso == '1':
                        while True:
                            print('\n-- Posts --')
                            print('[1] Ver listado')
                            print('[2] Guardar nuevo')
                            print('[3] Borrar por id')
                            print('[0] Volver')
                            r = input('Opción Posts [0-3]: ')
                            if r == '1':
                                listado_publicaciones()
                            elif r == '2':
                                titulo = input('Título: ')
                                contenido = input('Contenido: ')
                                user_id = input('ID Usuario: ')
                                try:
                                    user_id = int(user_id)
                                except:
                                    print('ID Usuario inválido.')
                                    continue
                                crear_publicacion(titulo, contenido, user_id)
                            elif r == '3':
                                id_elim = input('ID publicación a eliminar: ')
                                try:
                                    id_elim = int(id_elim)
                                except:
                                    print('ID inválido.')
                                    continue
                                eliminar_publicacion(id_elim)
                            elif r == '0':
                                break
                            else:
                                print('Opción inválida')
                    elif recurso == '2':
                        while True:
                            print('\n-- Comments --')
                            print('[1] Ver listado')
                            print('[2] Guardar nuevo')
                            print('[3] Borrar por id')
                            print('[0] Volver')
                            r = input('Opción Comments [0-3]: ')
                            if r == '1':
                                listado = obtener_listado_objetos(Comment)
                                if listado:
                                    for c in listado:
                                        print(f'{c.id} | {c.name} | {c.email} | postId:{c.postId}')
                            elif r == '2':
                                nombre = input('Nombre: ')
                                correo = input('Email: ')
                                contenido = input('Contenido: ')
                                post_id = input('ID Post: ')
                                try:
                                    post_id = int(post_id)
                                except:
                                    print('ID Post inválido.')
                                    continue
                                crear_comentario(None, nombre, correo, contenido, post_id)
                                if not validar_correo(correo):
                                    print('Correo inválido.')
                                    continue
                            elif r == '3':
                                id_elim = input('ID comentario a eliminar: ')
                                try:
                                    id_elim = int(id_elim)
                                except: 
                                    print('ID inválido.')
                                    continue
                                borrar_comentario(id_elim)
                            elif r == '0':
                                break
                            else:
                                print('Opción inválida')
                    elif recurso == '3':
                        while True:
                            print('\n-- Companies --')
                            print('[1] Ver listado')
                            print('[2] Guardar nuevo')
                            print('[3] Borrar por id')
                            print('[0] Volver')
                            r = input('Opción Companies [0-3]: ')
                            if r == '1':
                                listado = obtener_listado_objetos(Company)
                                if listado:
                                    for c in listado:
                                        print(f'{c.id} | {c.name} | {c.catchPhrase} | {c.bs}')
                            elif r == '2':
                                nombre = input('Nombre compañía: ')
                                slogan = input('Slogan: ')
                                negocio = input('Negocio (bs): ')
                                crear_compania(nombre, slogan, negocio)
                            elif r == '3':
                                id_elim = input('ID compañía a eliminar: ')
                                try:
                                    id_elim = int(id_elim)
                                except:
                                    print('ID inválido.')
                                    continue
                                eliminar_objeto_por_id(Company, id_elim)
                            elif r == '0':
                                break
                            else:
                                print('Opción inválida')
                    elif recurso == '0':
                        print('Cerrando sesión...')
                        session_active = False
                    else:
                        print('Opción inválida')
        elif opcion_inicial == '3':
            busqueda()
        elif opcion_inicial == '0':
            print('Saliendo...')
            break
        else:
            print('Opción Incorrecta, vuelva a intentar...')


app()
