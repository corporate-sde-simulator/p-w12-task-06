import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from logAnalyzer import LogAnalyzer, SAMPLE_LOGS

class TestLogAnalyzer:
    @pytest.fixture
    def analyzer(self):
        la = LogAnalyzer()
        la.load_logs(SAMPLE_LOGS)
        return la

    def test_parses_all_lines(self, analyzer):
        assert len(analyzer.entries) == 8, "Should parse all 8 log lines"

    def test_filter_errors(self, analyzer):
        errors = analyzer.filter_by_level('ERROR')
        assert len(errors) == 3, "Should find 3 ERROR entries"

    def test_timeline_sorted(self, analyzer):
        timeline = analyzer.get_timeline()
        timestamps = [e['timestamp'] for e in timeline]
        assert timestamps == sorted(timestamps), "Timeline should be chronologically sorted"

    def test_root_cause(self, analyzer):
        cause = analyzer.find_root_cause()
        assert 'connection pool' in cause.lower(), "Root cause was DB connection pool"
