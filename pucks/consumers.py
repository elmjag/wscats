from channels.generic.websocket import JsonWebsocketConsumer
from tango import DeviceProxy, EventType


class CassettePresenceEvents:
    def __init__(self, pucks_status_cb):
        self.device = DeviceProxy("b311a-e/ctl/cats-01")
        self.event_id = self.device.subscribe_event(
            "CassettePresence",
            EventType.CHANGE_EVENT,
            lambda e: pucks_status_cb(e.attr_value.value),
        )

    def unsubscribe(self):
        self.device.unsubscribe_event(self.event_id)


class CatsPucks(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self._cassettes = CassettePresenceEvents(self.pucks_status_changed)

    def pucks_status_changed(self, pucks_status):
        # convert the 'ndarray' type to list of bools,
        # so that we can serialize it as JSON
        pucks = [True if s == 1 else False for s in pucks_status]
        self.send_json({"pucks": pucks})

    def disconnect(self, close_code):
        self._cassettes.unsubscribe()
