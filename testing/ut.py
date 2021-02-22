from pyats import aetest
import logging
from nested_lookup import nested_lookup

logger = logging.getLogger(__name__)

# define a common setup section by inherting from aetest
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed, steps):
        for device in testbed.devices:
            with steps.start('Connecting to %s' % device):
                testbed.devices[device].connect()
    
# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        for device in testbed.devices:
           with steps.start('Disconnecting from %s' % device):
                testbed.devices[device].disconnect()

# basic workflow to process each testcase using steps
def process_steps(test_steps, testbed, steps):
    for step in test_steps:
        with steps.start(step['desc']):
            if 'exec_command' in step.keys():
                var = testbed.devices[step['device']].execute(step['exec_command'])                
            if 'assert_value' in step.keys():
                assert step['assert_value'] in var
            if 'config_command' in step.keys():
                testbed.devices[step['device']].configure(step['config_command'])

# testcase classes which will take data from datafile
class Connectivity_during_normal_operation(aetest.Testcase):

    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        aetest.skipIf.affix(self.cleanup, self.cleanup_steps is None, 'no cleanup steps specified')

    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)
        
    @aetest.cleanup
    def cleanup(self, testbed, steps):
        process_steps(test_steps = self.cleanup_steps, testbed = testbed, steps=steps)
        
class Connectivity_during_ISP01_failover(aetest.Testcase):
    
    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        aetest.skipIf.affix(self.cleanup, self.cleanup_steps is None, 'no cleanup steps specified')

    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)
        
    @aetest.cleanup
    def cleanup(self, testbed, steps):
        process_steps(test_steps = self.cleanup_steps, testbed = testbed, steps=steps)

class Connectivity_during_ISP02_failover(aetest.Testcase):
    
    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        aetest.skipIf.affix(self.cleanup, self.cleanup_steps is None, 'no cleanup steps specified')

    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)
        
    @aetest.cleanup
    def cleanup(self, testbed, steps):
        process_steps(test_steps = self.cleanup_steps, testbed = testbed, steps=steps)

class Banner_check(aetest.Testcase):
    
    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        aetest.skipIf.affix(self.cleanup, self.cleanup_steps is None, 'no cleanup steps specified')

    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)
        
    @aetest.cleanup
    def cleanup(self, testbed, steps):
        process_steps(test_steps = self.cleanup_steps, testbed = testbed, steps=steps)
