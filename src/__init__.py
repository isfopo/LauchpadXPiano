from .RemoteScriptStarter import RemoteScriptStarter


def create_instance(c_instance):
    ''' Creates and returns Remote Script instance '''
    return RemoteScriptStarter(c_instance)
