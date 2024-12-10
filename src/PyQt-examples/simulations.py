import time
import threading
import numpy as np
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

class FakeDevice(QWidget):
    """Mimic simple device behavior for the MAT example"""
    # Define signals for this class
    managerChanged = pyqtSignal(str)
    accessorChanged = pyqtSignal(str)
    transporterChanged = pyqtSignal(str)

    def __init__(self, runtime=10, name="My fake device", parent=None):
        super(FakeDevice, self).__init__()
        self._runtime = runtime
        self._name = name
        self._manager_status = "init"
        self._accessor_status = "init"
        self._transporter_status = "init"

    @property
    def runtime(self):
        """Get the runtime of the simulator"""
        return self._runtime
    
    @runtime.setter
    def runtime(self, value):
        """Set the runtime of the simulator"""
        if not isinstance(value, int):
            raise ValueError("runtime must be an int")
        self._runtime = value

    @property
    def name(self):
        """Get the name of the device"""
        return self._name
    
    @property
    def manager_status(self):
        """Get the manager status"""
        return self._manager_status
    
    @manager_status.setter
    def manager_status(self, value):
        """Set the manager status"""
        if self.manager_status != value:
            self.managerChanged.emit(value)
        self._manager_status = value
    
    @property
    def accessor_status(self):
        """Get the accessor status"""
        return self._accessor_status
    
    @accessor_status.setter
    def accessor_status(self, value):
        """Set the accessor status"""
        if self.accessor_status != value:
            self.accessorChanged.emit(value)
        self._accessor_status = value
    
    @property
    def transporter_status(self):
        """Get the transporter status"""
        return self._transporter_status
    
    @transporter_status.setter
    def transporter_status(self, value):
        """Set the transporter status"""
        if self.transporter_status != value:
            self.transporterChanged.emit(value)
        self._transporter_status = value
    
    def gen_random_status(self):
        """Generate a random status"""
        status_choices = ["clear", "warn", "assert"]
        status_weights = [0.7, 0.2, 0.1]
        status = np.random.choice(status_choices, p=status_weights)
        return status
    
    def update_status(self):
        """Update with randomly-generated statuses"""
        self.manager_status = self.gen_random_status()
        self.accessor_status = self.gen_random_status()
        self.transporter_status = self.gen_random_status()

    def print_status(self):
        """Print the statuses"""
        print("\n")
        print(f"M: {self.manager_status}")
        print(f"A: {self.accessor_status}")
        print(f"T: {self.transporter_status}")

    def run(self):
        """Run the simulator"""
        time.sleep(10)
        print(f"Device \"{self.name}\" has started")
        for i in range(self.runtime):
            time.sleep(1)
            self.update_status()
            self.print_status()
        print("\n")
        print(f"Device \"{self.name}\" has stopped")

    def run_threaded(self):
        """Run the simulator in a new thread"""
        thread = threading.Thread(target=self.run)
        thread.start()