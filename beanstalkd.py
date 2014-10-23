import time
import beanstalkc

from checks import AgentCheck

class BeanstalkdCheck(AgentCheck):
    def get_tube_stats(self):
        stats = {}
        for tube in self.client.tubes():
            tube_stats = self.client.stats_tube(tube)
            tube_stats = self.prefix_keys(tube, tube_stats)
            stats.update(tube_stats)

        return stats

    def prefix_keys(self, tube_name, stats):
        '''
        Our plugin output must be a flat dict. Since each tube returns the
        same key/value stats we must prefix key names with the tube name e.g.
        the key total-jobs for tube 'email_signup' becomes email_signup-total-jobs.
        '''
        new_dict = {}

        for k, v in stats.items():
            key = '%s-%s' % (tube_name, k)
            new_dict[key] = v

        return new_dict

    def check(self, instance):
        # Connect to Beanstalkd
        try:
            host = instance.get('host')
            port = instance.get('port')

            self.client = beanstalkc.Connection(host=host, port=port)
        except:
            self.log.info("Can't connect to Beanstalkd")
            return

        # Get the stats
        stats = self.client.stats()
        stats.update(self.get_tube_stats())

        for k, v in stats.items():
            self.gauge('beanstalkd.%s' % k,   v)

        # Close the connection
        self.client.close();