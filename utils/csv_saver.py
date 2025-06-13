import csv
from pathlib import Path

class CSVSaver:
    def __init__(self, filename: Path = None):
        if filename is None:
            filename = Path(__file__).parent.parent / "results" / "results.csv"
        self.filename = filename
        self.fieldnames = ["operation", "cluster_type", "input_size", "time_taken", "memory_used"]
        self._initialize_csv()

    def _initialize_csv(self):
        if not self.filename.exists():
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def save(self, operation, cluster_type, input_size, time_taken, memory_used):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow({
                "operation": operation,
                "cluster_type": cluster_type,
                "input_size": input_size,
                "time_taken": time_taken,
                "memory_used": memory_used
            })

