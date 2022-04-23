from .LaunchpadXPiano import LaunchpadXPiano


def create_instance(c_instance):
    ''' Creates and returns Remote Script instance '''
    return LaunchpadXPiano(c_instance)
