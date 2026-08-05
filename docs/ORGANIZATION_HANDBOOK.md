# channelsiege organization handbook

> Organization-wide defaults for repositories maintained under **channelsiege**. A repository may strengthen these rules locally, but should not silently weaken them.

## Mission and scope

channelsiege maintains software, services, and infrastructure for channel-oriented content, communication, and delivery workflows. The `.github` repository is the canonical home for the organization profile, contribution policy, security guidance, support expectations, reusable templates, and planning links.

## Repository expectations

Every active repository should make the following easy to discover:

- its purpose, ownership boundary, supported environments, and maturity level;
- reproducible local-development and test commands;
- the source of truth for interfaces, schemas, configuration, and generated artifacts;
- release, rollback, deprecation, and compatibility expectations;
- links to the relevant GitHub Project and Linear work.

Services and clients should document their protocol boundaries, failure behavior, rate and retry assumptions, and compatibility guarantees.

## Change workflow

1. Start from an issue, Linear item, or clearly documented maintenance objective.
2. Use a focused branch and keep unrelated work out of the pull request.
3. Explain the change, motivation, risk, validation, compatibility impact, and rollback path.
4. Run the narrowest relevant checks plus any organization-level conformance checks.
5. Resolve conflicts semantically: reconstruct both sides' intent, preserve compatible behavior, and document deliberate trade-offs.
6. Prefer squash merges for focused changes unless preserving commit structure materially improves review or auditability.

## Quality and delivery evidence

A change is complete only when another maintainer can understand and reproduce it. Pull requests should include exact commands and environments, expected and observed outcomes, negative-path coverage, documentation updates, and relevant CI or local-equivalent evidence.

Keep interfaces backwards compatible where practical. Breaking changes require an explicit migration path, versioning decision, consumer audit, and rollback plan.

## Security and data handling

Never commit credentials, tokens, private keys, production data, or sensitive logs. Report vulnerabilities privately according to `SECURITY.md`. Pin dependencies, actions, containers, and generated inputs where reproducibility or supply-chain integrity matters.

## Documentation and decisions

Documentation is part of the deliverable. Keep examples executable, links current, assumptions explicit, and repository boundaries unambiguous. Record architectural, protocol, compatibility, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning and status

GitHub is the source of truth for code, reviews, checks, releases, and delivery evidence. Linear is the source of truth for prioritization, dependencies, sequencing, and cross-project planning. The organization GitHub Project provides the cross-repository execution view. See `PROJECTS.md` for the routing contract.

## Organization health checklist

Review periodically:

- [ ] The organization profile accurately describes the project and its boundaries.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Active repositories have owners, descriptions, topics, and maintained READMEs.
- [ ] Default branches and required checks reflect current risk.
- [ ] Stale repositories are archived or carry an explicit status notice.
- [ ] Project links resolve and completed work is reflected in both GitHub and Linear.
- [ ] Shared workflows and templates are versioned, tested, and backwards compatible.
