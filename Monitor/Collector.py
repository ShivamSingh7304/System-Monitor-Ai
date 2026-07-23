from Monitor.Snapshot import SystemSnapshot

from Stats_Functions import cpu_stats
from Stats_Functions import battery_stats
from Stats_Functions import disk_status
from Stats_Functions import ram_stats
from Stats_Functions import speed_test
from Stats_Functions import operating_system


class SystemCollector:
    """
    Collects the complete state of the system.
    """
    def collect(self) -> SystemSnapshot:
        snapshot = SystemSnapshot(
            cpu=cpu_stats.invoke({}),
            ram=ram_stats.invoke({}),
            disk=disk_status.invoke({}),
            battery=battery_stats.invoke({}),
            network=speed_test.invoke({}),
            operating_system=operating_system.invoke({})
        )
        return snapshot


if __name__ == "__main__":
    collector = SystemCollector()
    snapshot = collector.collect()
    print(snapshot)