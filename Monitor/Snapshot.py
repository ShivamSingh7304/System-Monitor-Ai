from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class SystemSnapshot:
    """
    Represents the complete state of the computer
    at a single point in time.
    """

    timestamp: datetime = field(default_factory=datetime.now)
    cpu: Dict[str, Any] = field(default_factory=dict)
    ram: Dict[str, Any] = field(default_factory=dict)
    disk: Dict[str, Any] = field(default_factory=dict)
    battery: Dict[str, Any] = field(default_factory=dict)
    network: Dict[str, Any] = field(default_factory=dict)
    operating_system: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert snapshot into a serializable dictionary."""

        return {
            "timestamp": self.timestamp.isoformat(),
            "cpu": self.cpu,
            "ram": self.ram,
            "disk": self.disk,
            "battery": self.battery,
            "network": self.network,
            "operating_system": self.operating_system,
        }

if __name__ == "__main__":

    snapshot = SystemSnapshot()

    print(snapshot)