import time
from Monitor.Collector import SystemCollector

class SystemMonitor:
    """
    Continuously monitors the system by collecting
    snapshots at a fixed interval.
    """
    def __init__(self, interval: int = 5):
        self.interval = interval
        self.collector = SystemCollector()
        self.running = False
    def start(self):
        """
        Start continuous monitoring.
        """
        self.running = True
        print(f"Monitoring started (every {self.interval} seconds)\n")
        while self.running:
            snapshot = self.collector.collect()
            # Temporary output
            print(snapshot)
            time.sleep(self.interval)
    def stop(self):
        """
        Stop monitoring.
        """
        self.running = False


if __name__ == "__main__":

    monitor = SystemMonitor(interval=5)
    try:
        monitor.start()
        print(monitor)
    except KeyboardInterrupt:
        monitor.stop()
        print("\nMonitoring stopped.")