import sys
import unittest
from datetime import timezone
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from chainwarden import der  # noqa: E402
from chainwarden.certmodel import CertParseError, _parse_time  # noqa: E402


def tlv(tag, text):
    return SimpleNamespace(tag=tag, value=text.encode("ascii"))


class TimeParsingTests(unittest.TestCase):
    def test_utctime_pivot_is_unchanged(self):
        self.assertEqual(_parse_time(tlv(der.TAG_UTC_TIME, "490101000000Z")).year, 2049)
        self.assertEqual(_parse_time(tlv(der.TAG_UTC_TIME, "500101000000Z")).year, 1950)

    def test_generalized_time(self):
        parsed = _parse_time(tlv(der.TAG_GENERALIZED_TIME, "20260101000000Z"))
        self.assertEqual((parsed.year, parsed.month, parsed.day), (2026, 1, 1))
        self.assertIs(parsed.tzinfo, timezone.utc)

    def test_malformed_values_raise_cert_parse_error_with_the_field(self):
        cases = [(der.TAG_UTC_TIME, "2401", "UTCTime"),
                 (der.TAG_UTC_TIME, "2401010000X0Z", "expected digits"),
                 (der.TAG_GENERALIZED_TIME, "2026010100000Z", "GeneralizedTime")]
        for tag, text, needle in cases:
            with self.assertRaises(CertParseError) as ctx:
                _parse_time(tlv(tag, text))
            self.assertIn(needle, str(ctx.exception), (text, str(ctx.exception)))


if __name__ == "__main__":
    unittest.main()
