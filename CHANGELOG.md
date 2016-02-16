# Changelog

All notable changes to this project are documented here. The format follows
Keep a Changelog, and this project uses semantic versioning.

## [0.1.0] - 2026-09-02

### Added

- PEM block reader that splits a text buffer into labelled base64 blocks and
  decodes CERTIFICATE blocks (`pemread.py`).
- Minimal DER tag-length-value walker that rejects indefinite lengths and
  reaches the fields needed for auditing (`der.py`).
- Certificate model parsed from DER: subject, issuer, serial, validity dates,
