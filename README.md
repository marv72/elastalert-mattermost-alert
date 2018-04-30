# elastalert-mattermost-alert
ElastAlert alert to get Elasticsearch hits into a Mattermost channel, created using the ElastAlerts docs page [ElastAlert Alerts](http://elastalert.readthedocs.io/en/latest/ruletypes.html#alerts)

# How to install this alert

I recommend copying the module to Site-Packages, quick way so it is always found.
```
/usr/lib/pythonX.X/site-packages/elastalert_modules
```
Or you can add to sys path.

# Sample rule
You need to create mattermost webhook, [documented here](https://docs.mattermost.com/developer/webhooks-incoming.html).

Then add these four mandatory fields to the alert yaml file and the hits from the elastalert rulle will be sent to MatterMost channel.
```
alert: "elastalert_modules.mattermost_alert.MatterMostAlerter"
mattermost_webhook_url: "https://<fqdn>/hooks/<webhookId>"
error_description_field: "ErrorDesc"
alert_name_field: "MessageFlow"
```

## ElastAlert - [Read the Docs](http://elastalert.readthedocs.org).


