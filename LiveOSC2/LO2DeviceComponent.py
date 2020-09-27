from _Framework.DeviceComponent import DeviceComponent
from _Framework.SubjectSlot import subject_slot


from LO2ParameterComponent import LO2ParameterComponent
from LO2Mixin import LO2Mixin


class LO2DeviceComponent(DeviceComponent, LO2Mixin):


    def __init__(self):
        self._parameters = []
        super(LO2DeviceComponent, self).__init__(device_selection_follows_track_selection=False)

        self.set_default('_track_id', '_device_id')
        for param_pos in range(128):
            self.add_callback(
                '/fx/param/{}/val'.format(param_pos), self._device_param)

    def _update_appointed_device(self):
        super(LO2DeviceComponent, self)._update_appointed_device()
        self.update_device_selection()

    def update_device_selection(self):
        super(LO2DeviceComponent, self).update_device_selection()
        self._refresh_params()

    def set_device(self, device):
        super(LO2DeviceComponent, self).set_device(device)
        self._on_parameters_changed.subject = device
        self._on_parameters_changed()

    @subject_slot('parameters')
    def _on_parameters_changed(self):
        self.log_message('params changed')
        diff = len(self._device.parameters) - len(self._parameters)

        if diff > 0:
            for i in range(diff):
                self._parameters.append(LO2ParameterComponent())

        if diff < 0:
            for i in range(len(self._parameters)-1, len(self._device.parameters)-1, -1):
                self._parameters[i].disconnect()
                self._parameters.remove(self._parameters[i])

        for i,pc in enumerate(self._parameters):
            pc.set_parameter(self._device.parameters[i])

        self._refresh_params()

    def _device_param(self, msg, src):
        if self._device is not None:
            addr_fields = msg[0].split('/')
            p = int(addr_fields[3])
            v = msg[2]
            prm = self._device.parameters[p]
            prm_range = abs(prm.min - prm.max)
            prm_range_value = v * prm_range
            prm.value = prm.min + prm_range_value
