from CRUD_controler.models import Usuario 

def guardar(nombre,last_name,nickname,correo,password):
    dato = Usuario.objects.create(
        name =nombre,
        last_name = last_name,
        nickname = nickname,
        correo = correo,
        password = password
        )
    dato.save()
    pass

def leer_todo ():
    dato = Usuario.objects.all()
    return dato 

def leer_uno(id = None,nickname = None):
    if id != None:
        try:
            dato = Usuario.objects.get(id_user = id)
        except:
            dato = None
        return dato
        pass
    if nickname != None:
        try:
            dato = Usuario.objects.get(nickname = nickname)
        except:
            dato = None    
            pass
        return dato
        pass
    pass
def actualizar(id,nombre , last_name ,nickname,correo,password):

    pass


def eliminar():

    pass

