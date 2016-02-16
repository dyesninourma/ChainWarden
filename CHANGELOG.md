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
  signature algorithm, public key algorithm and RSA modulus size, basic
  constraints, key usage, extended key usage, subject alternative names, and a
  SHA256 fingerprint (`certmodel.py`).
- Name based chain assembly with self signed root detection and loop guarding
  (`chainbuild.py`).
- Policy checks with severities: weak signature, weak RSA key, expired, not yet
  valid, expiring soon, CA and leaf key usage sanity, path length, and expiry
