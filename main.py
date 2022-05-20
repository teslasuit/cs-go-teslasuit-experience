import time
import cs_go_client
import ts_client

class CSGOTeslatuitForceFeedback:
    def start(self):
        self.cs_go_client = cs_go_client.TsGoDamageListener()
        self.ts_client = ts_client.TsClient()
        self.cs_go_client.init()
        self.cs_go_client.set_event_callback(self.ts_client.process_ff_events)
        self.ts_client.init()
        while True:
            self.cs_go_client.process()

ff = CSGOTeslatuitForceFeedback()
ff.start()
