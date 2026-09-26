# Sanitized Detection Example

## Scenario

A successful authentication event is followed by suspicious endpoint behavior for the same identity within a short period.

## Objective

Demonstrate the **concept** of cross-source correlation without exposing production detection logic.

## Pseudologic

```text
IF authentication.result == "success"
AND endpoint.alert.confidence >= defined_threshold
AND identity matches across both events
AND time_difference <= correlation_window
THEN create correlated security context
```

## Enrichment

The correlated event may then receive additional context from:

- identity information;
- asset criticality;
- threat intelligence;
- vulnerability exposure;
- prior related observations.

## Important

This example is deliberately incomplete and generic.

It is not production detection logic and should not be copied into a security environment without validation.
