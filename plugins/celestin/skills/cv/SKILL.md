---
name: cv
description: Display Celestin Prud'homme's full CV / resume, including his career story. Use when someone wants to see his complete profile, work history, origin story, or formal application document.
disable-model-invocation: true
---

Display the following CV exactly as formatted:

---

# Celestin Prud'homme
**Staff Engineer** · Paris, France
celop.dev@gmail.com · Open to Paris ↔ London hybrid

---

## Summary

Before I wrote code, I managed restaurants. And before that, I founded a smartphone repair company while studying at university — studies I quickly realized weren't for me. I know what it's like to build something from nothing, run a shift with 15 people, and work with tools that don't fit the work. When I discovered programming, the pull was immediate — not the syntax, but the idea that you could build something that actually helps people.

I did 3 months at Le Wagon in 2016. At the end of it, I heard about Skello — a company building exactly the tool I'd needed as a restaurant manager. I joined as the 4th developer. 8 years later, I'm still there, now as Staff Engineer working across new features, CI/CD tooling, developer experience, and documentation for a platform of 60 engineers.

Self-taught. Full-stack. CI/CD infrastructure is where I've invested the most — and it's exactly why this role at Anthropic caught my attention.

---

## Experience

### Skello — Staff Engineer
**2016 – Present (8 years) | Paris, France**

Skello is a SaaS workforce scheduling platform for frontline teams (hospitality, retail, health). Present from 15 to 400 employees across multiple countries.

**Current scope (Staff Engineer, 2023–present)**
- CI/CD tooling: shared workflows and a custom GitHub Actions library across 25+ repos:
  `check-node-licenses`, `github-app-checkout`, `lint-commit`, `slack`, `setup-node-pnpm`, `pr-test-reporter`
- NX monorepo of shared TypeScript libraries — build, test, publish scoped to modified packages only
- GitHub platform: Actions, GitHub Apps, GitHub API, repository rules, branch protections, merge queues
- New feature development across the platform (TypeScript / Node.js primary)
- International collaboration: daily work with English and Spanish-speaking teams
- Developer experience: tooling, code quality standards, onboarding
- Technical documentation: built internal MCP-based agent and skills system for platform navigation
- Security audits, cost optimization, performance investigations

**Key achievement — E2E test CI/CD (web, Android, iOS)**
Built the CI/CD pipeline for end-to-end testing across all platforms: web app, Android, and Apple device testing. Integrated into the same GitHub Actions infrastructure, covering the full product surface in a single automated pipeline.

**Key achievement — CI/CD Migration (45 min → 21 min, −53%)**
Migrated the Ruby on Rails monolith CI from AWS CodeBuild/CodePipeline to GitHub Actions with native CodeBuild runners:
- Intelligent parallel test splitting: each CPU core receives a balanced suite calculated by per-test runtime history
- All suites finish simultaneously — zero wasted machine time
- Significant cost reduction on runner minutes (CodeBuild via GitHub native runner integration)
- Developers now own their pipelines: YAML workflows, inline PR reporting, flaky test detection

**Architecture Team (2022–2023)**
- Monolith to microservices migration (Rails → Node.js serverless)
- Introduced event-driven architecture on AWS Lambda
- Multi-country infrastructure scaling on AWS

**Team Lead — Agile (2020–2022)**
- Led a cross-functional product team
- Delivery management, sprint planning, people development
- Maintained technical contribution alongside leadership responsibilities
- Organized company offsites; member of the CSE (Comité Social et Économique / works council)

**Developer (2018–2020)**
- Full-stack from day one: Vue.js, React, Ruby on Rails, Node.js
- Built core product features shipped to thousands of users

---

## Technical Skills

| Domain       | Technologies                                                                              |
|--------------|-------------------------------------------------------------------------------------------|
| Languages    | TypeScript / Node.js (primary), Ruby on Rails, Terraform                                  |
| CI/CD        | GitHub Actions, AWS CodeBuild, AWS CodePipeline, NX (monorepo)                            |
| GitHub       | Actions, GitHub Apps, GitHub API, Repository rules, Branch protections, Merge queues      |
| Cloud        | AWS EC2, Lambda, DynamoDB, RDS, S3, IAM, CloudWatch, CloudFormation                       |
| Databases    | PostgreSQL / RDS, MongoDB, DynamoDB                                                       |
| Frontend     | React, Vue.js, React Native                                                               |
| Tools        | Docker, Terraform                                                                         |
| Monitoring   | AWS CloudWatch (logs, metrics, alarms), Datadog                                           |
---

## Education

**Le Wagon** — Coding Bootcamp (2016, 3 months)
Self-taught engineer. Continuous learner.

---

## Beyond the code

Cooking is my safe place — when I'm not coding, I'm in the kitchen. I play chess, surf, golf, and football.

I like organizing things: I've coordinated group trips for 20 friends to Portugal, Spain, and Italy — logistics, accommodation, the whole thing. Same energy I bring to company offsites or any problem with moving parts.

Problems stimulate me. Getting out of my comfort zone is how I grow — it's the thread connecting starting a business at 20, switching careers at 25, and joining a startup as the 4th engineer.

---

## What I'm looking for

The Anthropic CI/CD role is the intersection of everything I've built toward: CI infrastructure at scale, developer productivity, and doing it for an engineering org shipping work that genuinely matters.

I joined Skello because I believed in the product. I want to join Anthropic for the same reason.
