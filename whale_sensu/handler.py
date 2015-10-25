import whaleapi
from whaleapi.utils import converter
from whale_sensu.sensu.handler import SensuHandler


class WhaleHandler(SensuHandler):

    def handle(self):
        whaleapi.initialize(self.api_token(), self.api_host())

        timestamp = self.event.get('timestamp')
        hostname = self.event['client'].get('name')
        event_status = self.event['check'].get('status', 2)
        check = self.event['check'].get('name')
        text = self.event['check'].get('output')

        if timestamp is None or hostname is None or check is None or text is None:
            return self.bail('Could not send event to Whale Monitoring. Some data is missing.')

        whaleapi.api.Event.send(
            title='%s %s on %s' % (self.whale_alert_type(event_status).title(), check,
                                   str(hostname).lower()),
            text=text,
            timestamp=converter.epoch_to_iso_8601(timestamp),
            host=hostname,
            alert_type=self.whale_alert_type(event_status),
            aggregation_key=str('sensu.%s.%s' % (hostname, check)).lower(),
            source_type_name='sensu'
        )

    def whale_settings(self):
        whale_settings = self.settings.get('whale', {})
        return whale_settings

    def api_token(self):
        token = self.whale_settings().get('api_token')
        if not token:
            return self.bail('Please set a api_token in the handler settings.')
        return str(token)

    def api_host(self):
        return self.whale_settings().get('api_host')

    def whale_alert_type(self, status):
        status = int(status)
        if status == 0:
            return 'success'
        elif status == 1:
            return 'warning'
        elif status == 2:
            return 'error'
        else:
            return 'warning'


def run_handler():
    WhaleHandler()


if __name__ == "__main__":
    run_handler()
