---
name: tech
description: Deep dive into Celestin's technical stack, CI/CD expertise, cloud architecture, and engineering philosophy. Use when exploring his technical background or assessing fit for an engineering role.
disable-model-invocation: true
---

Present the following technical deep-dive about Celestin Prud'homme:

---

# Technical Profile — Celestin Prud'homme

---

## TypeScript / Node.js (Primary strength)

This is where I'm most at home. TypeScript and Node.js are my primary language — I use them for feature development, serverless microservices, internal tooling, CI scripts, and the NX monorepo. It's the area I go deepest technically.

---

## CI/CD (Significant part of my scope)

A meaningful part of my Staff Engineer role — not my entire job, but where I've invested a lot over the last few years.

### Tools used in production:
- **GitHub Actions** — primary, post-migration. Owner of our entire workflow library and shared actions.
- **AWS CodeBuild** — used as native runner backend for GitHub Actions (GitHub's CodeBuild runner integration)
- **AWS CodePipeline** — legacy, replaced during migration
- **NX** — monorepo tooling for affected-only build/test/publish pipelines

### Shared GitHub Actions library

I build and own all the custom actions used across the organization:

| Action | What it does |
|--------|-------------|
| `check-node-licenses` | License compliance scanning on dependency changes |
| `github-app-checkout` | Secure repo checkout via GitHub App (no PAT required) |
| `lint-commit` | Conventional commit enforcement |
| `slack` | Structured Slack notifications (deploys, failures, releases) |
| `setup-node-pnpm` | Node + pnpm setup with full layer caching |
| `pr-test-reporter` | Inline test results, coverage deltas, flakiness scores on PRs |

These are internal products. When they change, every repo in the org is affected.

### NX monorepo — shared library CI

I maintain our NX monorepo of shared TypeScript/Node.js libraries. The CI pipeline uses NX's affected graph to scope build, test, and npm publish to only the packages that changed. Engineers touching one package don't wait for the whole monorepo.

### The migration I'm most proud of:

**Ruby on Rails monolith: 45 min → 21 min CI**

The technical challenge was intelligent parallel test splitting:
- Each CPU core of the runner machine receives its own test suite
- Suite allocation is computed from **per-test runtime history** — not file count, not line count
- Goal: all suites complete simultaneously. Zero idle cores.
- Implemented across full suite: unit, integration, system tests

Additional work:
- GitHub-native test reporters integrated into PRs (pass/fail per test, trends, flakiness scores)
- Flaky test detection and quarantine: flaky tests flagged, not blocking deploys
- Runner right-sizing: matching machine size to suite parallelism factor
- Cost optimization via CodeBuild runner pricing vs. GitHub-hosted runners

**Scale:** 25 microservices + 4 web apps + 2 React Native apps · ~60 engineers · multiple deploys/day

### E2E test CI/CD (web, Android, iOS)

I also built the CI/CD pipeline for end-to-end testing across all platforms: web app, Android, and Apple device testing. Fully integrated into our GitHub Actions infrastructure — same shared actions, same branch model, covering the full product surface automatically.

### Branch management & multi-environment strategy

One of the more complex things we've built: a 4-tier AWS environment model fully linked to GitHub branch hierarchy.

| Environment | Branch strategy | Purpose |
|-------------|----------------|---------|
| **Sandbox (per team)** | Feature branches, per Agile team | Each team gets their own isolated AWS stack. Parallel development without conflicts. |
| **Staging** | `main` / integration branch | Pre-production validation, full integration testing |
| **Production** | Release tags / protected branch | Live, customer-facing |

**Why this matters for scale:**
- 4–5 Agile teams deploy daily to their sandboxes independently
- No one blocks anyone. Each team owns their environment.
- Clear promotion path: sandbox → staging → production
- Full-stack testing (frontend + monolith + microservices) before any merge
- GitHub branch protections and status checks gate each promotion

This is what makes daily multi-team delivery actually work in practice, not just in theory.

### Full GitHub ownership

Beyond Actions, I own the full GitHub stack for the organization:
- **GitHub Apps** — built and maintain internal apps for bot checkouts, automated PRs, and API integrations. No PAT, proper installation permissions.
- **GitHub API** — automation scripts, repository management, PR status updates, release workflows
- **Repository rules & branch protections** — enforce promotion paths, required checks, and code quality gates across all repos
- **Merge queues** — managing parallel merges without conflicts at scale

---

## Cloud — AWS

Primary cloud provider for Skello's entire infrastructure.

**Compute:** EC2 (various sizes for different workloads), Lambda (serverless Node.js microservices)
**Storage:** S3, DynamoDB, RDS (PostgreSQL), MongoDB
**Networking/Security:** VPC, IAM, Security Groups, Secrets Manager
**Observability:** CloudWatch (logs, metrics, alarms)
**Infrastructure as Code:** Terraform (full infrastructure definition)
**CI integration:** CodeBuild as GitHub Actions runner backend

Experience level: Production use across all above services. Daily operational responsibility.

---

## Languages

**TypeScript / Node.js** — Primary and strongest. Feature development, serverless microservices, internal tooling, CI scripts, NX monorepo libraries. This is where I go deepest.
**Ruby on Rails** — 8 years on the monolith: performance, testing, deployment, migrations.
**React / Vue.js / React Native** — Genuine full-stack. Frontend is not foreign territory.
**Terraform** — Infrastructure definition for the AWS stack.
**Shell / YAML** — CI workflow authoring, automation scripts.

---

## Architecture experience

- **Monolith to microservices:** Led progressive decomposition of a Rails monolith into 25 event-driven Node.js microservices
- **Serverless:** Introduced AWS Lambda for backend services; Node.js + DynamoDB patterns
- **Event-driven:** Async communication between services via event bus
- **Multi-country SaaS:** Infrastructure supporting multiple European markets
- **Mobile:** 2 React Native apps in production

---

## AI tooling

Built an internal MCP-based agent and skills system at Skello:
- Agents covering each technical domain: infrastructure, deployments, testing, architecture
- Skills expose runbooks, architecture decisions, troubleshooting guides
- Purpose: developers self-serve on complex questions without pinging the platform team
- Impact: reduced onboarding friction, less Slack noise, more autonomous engineers

(Note: the plugin you're currently using was built using the same approach.)

---

## Engineering philosophy

**Developers are users, not just colleagues.** CI, tooling, documentation — I build these for ~60 internal users. That means listening to feedback, measuring what matters, and iterating. The same care I'd put into a customer-facing product.

**Ownership over process.** The biggest win in the CI migration wasn't the time saved — it was engineers owning their pipelines. When your CI is your responsibility, you care about it differently. Shifting ownership is more durable than any technical optimization.

**Do the simple thing that works.** I don't chase new tech for its own sake. I pick what's reliable, what the team understands, and what we can debug at 2am. Complexity is a liability. A boring pipeline that never fails is worth more than an elegant one that breaks on Fridays.
