

def TaskMetrics(action, user, is_finalize=True):
    """ Este metodo actualiza las metricas del perfil
    + action: Es el tipo de accion a realizar, Create o Update
    + user: Es el usuario el cual se tiene que actualizar
    + is_finalize: Si la tarea se termino o no
    """
    profile = user.profile

    if action == 'Create':
        profile.tasks_created += 1
        profile.tasks_pending += 1
    elif action == 'Update':
        if is_finalize:
            profile.tasks_pending -= 1
            profile.tasks_finalize += 1
        else:
            profile.tasks_finalize -= 1
            profile.tasks_pending += 1

    profile.save()
