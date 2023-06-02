from CRUD_controler.models import Usuario 

def guardar(nombre,last_name,nickname,correo,password):
    dato = Usuario.objects.create(
        name =nombre,
        last_name = last_name,
        nickname = nickname,
        correo = correo,
        password = password
        )
    return dato
    pass

def leer_todo ():
    dato = Usuario.objects.all()
    return dato 

def leer_uno(id = None,correo = None):
    if id != None:
        dato = Usuario.objects.get(id_user = id)
        return dato
        pass
   
    pass
def actualizar(id,nombre , last_name ,nickname,correo,password):

    pass


def eliminar():

    pass
