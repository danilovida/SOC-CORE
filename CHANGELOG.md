# Changelog

All notable changes to the public SOC CORE documentation project will be documented here.

## 2026-10-06

### Added

- Public documentation for the integrated **Network Detection & Prevention (IDS/IPS)** capability.
- IDS-mode coverage for passive network detection, visibility and alerting.
- IPS-mode coverage for preventive controls where architecture, supported integrations and organizational policy allow safe enforcement.
- Correlation of network detections with asset, identity, vulnerability and threat intelligence context.
- Brazilian Portuguese documentation for **Network Exposure & Port Scanning**, aligning capability coverage between the English and Portuguese READMEs.
- Public roadmap coverage for Asset Inventory Management, Cloud Security / CASB, network exposure scanning and IDS/IPS.

### Reviewed

- Confirmed that **Asset Inventory Management** is already documented in both English and Brazilian Portuguese.
- Confirmed that **Cloud Security / CASB**, including Cloud Discovery, Shadow IT and organization-controlled governance, is already documented in both languages.

### Security

- IDS/IPS documentation remains conceptual and does not expose production signatures, prevention rules, internal topology, addresses, sensor placement or operational configurations.

## 2026-10-01

### Added

- Integrated **Asset Inventory Management** capability documented as part of SOC CORE.
- Multi-source asset discovery, normalization and correlation for unified operational visibility.
- Asset classification across endpoints, servers, network infrastructure, security appliances, IoT and other observed device types.
- Source provenance and per-asset visibility with identifiers, recent observations and technical context when available.
- Search, filtering and CSV export for operational reporting and audit support.
- Identification of unknown or insufficiently classified assets for analyst review.
- Integrated **Cloud Security / CASB** capability documented as part of SOC CORE.
- Cloud Discovery for identifying cloud applications and services observed in the environment.
- Shadow IT visibility and application-governance workflows.
- Risk-based classification and recurring audit views for cloud application usage.
- Separation between CASB-relevant applications and technical network/infrastructure telemetry.
- Organization-controlled approved-application governance, preserving human validation over authorization decisions.

### Security

- Asset Inventory public documentation remains conceptual and does not expose production asset lists, internal IP addresses, hostnames, device identifiers, correlation rules or operational configurations.
- CASB public documentation remains conceptual and does not expose production rules, credentials, corporate allowlists, users, internal addressing or operational integration details.

## 2026-09-26

### Added

- Initial public SOC CORE repository.
- English primary README.
- Brazilian Portuguese README.
- Conceptual architecture documentation.
- Integration philosophy.
- Security model.
- AI-assisted analysis principles.
- Public disclosure and sanitization policy.
- Public roadmap.
- Sanitized example incident.
- Sanitized example detection.

### Security

- Established a documentation-first publication model.
- Explicitly excluded production code, credentials, internal infrastructure data and identifiable incident content.
