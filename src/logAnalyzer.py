import re
from datetime import datetime
from typing import List, Dict

class LogAnalyzer:
    def __init__(self):
        self.entries = []

    def parse_line(self, line: str) -> Dict:
        # Pattern expects [INFO] but some logs have [WARN] or [ERROR]
        # The group capture is also wrong — captures wrong segments
        pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)'
        match = re.match(pattern, line)
        if match:
            return {
                'timestamp': match.group(1),
                'level': match.group(2),
                'message': match.group(3),
            }
        return None

    def load_logs(self, log_text: str):
        for line in log_text.strip().split('\n'):
            entry = self.parse_line(line)
            if entry:
                self.entries.append(entry)

    def filter_by_level(self, level: str) -> List[Dict]:
        return [e for e in self.entries if e['level'] == level]

    def get_timeline(self, start=None, end=None) -> List[Dict]:
        results = self.entries
        if start:
            results = [e for e in results if e['timestamp'] >= start]
        if end:
            results = [e for e in results if e['timestamp'] <= end]
        return results

    def find_root_cause(self) -> str:
        errors = self.filter_by_level('ERROR')
        if not errors:
            return 'No errors found'
        # Returns the first error — the root cause is usually the first one
        return errors[0]['message']

SAMPLE_LOGS = '''[2026-03-15 14:30:00] [INFO] Server started on port 8080
[2026-03-15 14:31:55] [WARN] Connection pool running low (8/10)
[2026-03-15 14:32:01] [ERROR] Database connection pool exhausted
[2026-03-15 14:32:02] [ERROR] Failed to process request: no available connections
[2026-03-15 14:32:15] [ERROR] Health check failed: database
[2026-03-15 14:33:00] [INFO] Auto-scaling triggered: adding 2 instances
[2026-03-15 14:44:00] [INFO] Connection pool recovered (4/10)
[2026-03-15 14:44:30] [INFO] All services healthy'''
