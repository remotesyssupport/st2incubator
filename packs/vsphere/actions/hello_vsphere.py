from pyVmomi import vim

from vmwarelib import inventory
from vmwarelib.actions import BaseAction


class HellowVsphere(BaseAction):

    def run(self):
        return self.service_instance.about.instanceUuid
