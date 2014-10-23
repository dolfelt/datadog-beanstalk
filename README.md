## Beanstalk Datadog Agent Check ##

### Install ###
* Put beanstalkd.py in /etc/dd-agent/checks.d/
* Put beanstalkd.yml in /etc/dd-agent/conf.d/
* Restart dd-agent

### Dependencies ###

* [Beanstalkc](https://github.com/earl/beanstalkc)
* [PyYAML](http://pyyaml.org/)

### Datadog Docs ###
[Agent Checks](http://docs.datadoghq.com/guides/agent_checks/)

### Examples ###
This agent check is currently being used in production for [When I Work](http://wheniwork.com).