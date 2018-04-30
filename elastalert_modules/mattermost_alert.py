from elastalert.alerts import Alerter
import requests
import time

# Disable SSL warnings in requests needed if Mattermost uses HTTPS
requests.packages.urllib3.disable_warnings()

class MatterMostAlerter(Alerter):

    # Rule must have these required options
    required_options = set(['mattermost_webhook_url', 'error_description_field', 'alert_name_field'])
    # Alert is called
    def alert(self, matches):
        # Iterate through Matches captured by the rule
        for match in matches:
            payload = {}
            # Obtaining required options for this Alert
            url = self.rule['mattermost_webhook_url']
            errorName = self.rule['alert_name_field']
            errorString = self.rule['error_description_field'] 
            # posting the match to MatterMost
            try:
                match_string = "%s %s :small_blue_diamond:%s :small_orange_diamond:%s" % ( match['type'], match[errorName], match['host'], match[errorString])
                payload['text'] = match_string
                try:
                    response = requests.post(url, verify=False, json=payload, timeout=(3.05, 27))
                except requests.exceptions.Timeout:
                    response = requests.post(url, verify=False, json=payload, timeout=(3.05, 27))
                except requests.exceptions.RequestException as e:
                    sys.exit(1)
                except:
                    sys.exit(2)
            except:
                sys.exit(3)
    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'Mattermost Alerter',
                'mattermost_webhook_url': self.rule['mattermost_webhook_url'],
                'error_description_field': self.rule['error_description_field'],
                'alert_name_field': self.rule['alert_name_field']}
