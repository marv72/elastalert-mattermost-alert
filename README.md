# Elastalert Mattermost Alert
ElastAlert alert to get Elasticsearch hits into a Mattermost channel, [ElastAlert Alerts](http://elastalert.readthedocs.io/en/latest/ruletypes.html#alerts)

# MatterMost WebHook
You need to create mattermost webhook, [documented here](https://docs.mattermost.com/developer/webhooks-incoming.html).  There must be a channel and webhook to send the messages to.

# Install this alert
This is a simple python module, and I recommend copying the module to Site-Packages, quick way so it is always found.
```
$ cd /usr/lib/pythonX.X/site-packages
$ mkdir elastalert_modules
$ cd elastalert_modules
$ touch __init__.py
$ cp /tmp/mattermost_alert.py .
```
This means that ElastAlert will import the alert with 
```
from elastalert_modules.mattermost_alert import MatterMostAlerter
```
This means that the folder must be in a location where it can be imported as a python module.

# ElastAlert Configuration file

There are four mandataory fields that must be added to a ElastAlert 

``alert: "elastalert_modules.mattermost_alert.MatterMostAlerter"`` - location of the module and class

``mattermost_webhook_url: "https://<fqdn>/hooks/<webhookId>"`` - URL of the Mattermost WebHook

``error_description_field: "<field-name>"`` - Set this to a field in the hit that contains the error name 

``alert_name_field: "<field-name>"`` - Set this to a field in the hit that contains the main error payload 

Sample elastalert configuration file included in example_rules

## ElastAlert - [Read the Docs](http://elastalert.readthedocs.org).


