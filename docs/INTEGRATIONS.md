# SOC CORE — Integration Philosophy

## Principle

**SOC CORE adapts to the company's security ecosystem, not the other way around.**

The platform is designed to integrate with technologies already present in an organization.

## Supported Integration Patterns

Depending on the source, an integration may use:

- REST API
- Webhook
- Syslog
- Agent
- Log forwarding
- Database access
- Message queue
- File-based ingestion
- Vendor SDK
- Other documented telemetry interfaces

## Integration Lifecycle

A typical integration follows this model:

1. **Collect** — retrieve or receive relevant telemetry.
2. **Validate** — verify schema, authentication and expected fields.
3. **Normalize** — map source-specific data into a consistent model.
4. **Enrich** — add threat, identity, asset or vulnerability context.
5. **Correlate** — connect related events and entities.
6. **Assess** — evaluate severity and risk.
7. **Act** — support incident handling, automation or analyst review.

## Technical Limitations

The existence of an API does not guarantee complete integration.

Feasibility depends on:

- exposed endpoints and telemetry;
- authentication methods;
- permission model;
- licensing;
- data freshness;
- pagination and rate limits;
- connectivity;
- vendor restrictions;
- event quality;
- retention;
- API stability.

SOC CORE integrations should therefore be evaluated source by source.

## Design Goal

Integrations should be modular enough that the failure or replacement of one source does not require redesigning the entire platform.
