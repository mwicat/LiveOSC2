from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot


from LO2Mixin import LO2Mixin


class LO2ParameterComponent(ControlSurfaceComponent, LO2Mixin):

    def __init__(self, send = False):
        self._is_send = send
        self._parameter = None
        super(LO2ParameterComponent, self).__init__()


    def set_parameter(self, param):
        self._parameter = param
        self._on_value_changed.subject = param


    def set_parameter_value(self, value):
        self._parameter.value = value
    
    
    @subject_slot('value')
    def _on_value_changed(self):
        if hasattr(self._parameter.canonical_parent, 'parameters'):
           p = list(self._parameter.canonical_parent.parameters).index(self._parameter)
           self._set_param(p, self._parameter)
