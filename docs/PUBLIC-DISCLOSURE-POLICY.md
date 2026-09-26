# SOC CORE — Public Disclosure & Sanitization Policy

This repository exists to demonstrate engineering concepts without exposing sensitive operational information.

## Allowed Public Content

The following may be published when properly sanitized:

- conceptual architecture;
- generic workflows;
- fictitious incidents;
- reserved documentation IP addresses;
- invalid example domains;
- generic schemas;
- engineering principles;
- high-level capability descriptions;
- public roadmap information.

## Prohibited Public Content

The following must not be committed:

- production source code unless explicitly approved for publication;
- passwords;
- API keys;
- access tokens;
- certificates or private keys;
- internal IP addresses;
- internal hostnames;
- tenant or subscription IDs;
- user identities from real incidents;
- customer information;
- sensitive screenshots;
- exact production network diagrams;
- firewall policies;
- production database credentials or connection strings;
- internal service URLs;
- proprietary detection logic where disclosure creates operational risk.

## Sanitization Requirements

Before publication:

1. Replace identities with fictitious values.
2. Replace real IP addresses with documentation ranges.
3. Replace domains with reserved example domains.
4. Remove timestamps when they can identify a real incident.
5. Remove tenant, subscription, device and correlation identifiers.
6. Verify screenshots manually before committing.
7. Assume Git history is permanent.

## Safe Example Values

Use values such as:

- `198.51.100.0/24`
- `203.0.113.0/24`
- `192.0.2.0/24`
- `example.com`
- `example.org`
- `analyst@example.com`

## Final Rule

If publication creates uncertainty about whether information is sensitive, do not publish it until reviewed.
