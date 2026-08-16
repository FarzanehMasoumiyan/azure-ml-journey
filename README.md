# Azure ML Journey

Public learning log documenting my path from ML research/teaching background to production-ready Azure ML & MLOps skills — following a structured 12-week plan covering Azure ML, deployment, CI/CD, and GenAI.

## Progress

| Week | Focus | Status |
|---|---|---|
| 1 | Cloud foundations — account, resource group, storage, ML workspace | ✅ Done |
| 2 | Training a model with the Azure ML SDK v2 | ⬜ Upcoming |
| 3 | AI-900/901 Fundamentals certification | ⬜ Upcoming |
| 4–5 | Deploying a model as a managed online endpoint | ⬜ Upcoming |
| 6 | CI/CD for ML with GitHub Actions | ⬜ Upcoming |
| 7 | Monitoring & drift detection | ⬜ Upcoming |
| 8 | DP-100 certification | ⬜ Upcoming |
| 9–12 | GenAI portfolio: RAG app, MLOps-wrapped CV project, agentic AI demo | ⬜ Upcoming |

---

## Week 1 — Cloud Foundations

**Goal:** Set up the core Azure resources needed for everything that follows: a resource group, a storage account, and an Azure ML workspace, all provisioned via the CLI rather than clicking through the portal.

### What I built

- Azure free account with a monthly budget and email alerts configured to avoid surprise charges
- Azure CLI installed and authenticated
- A resource group (`rg-ml-journey`) in the `canadacentral` region
- A storage account (`stmljourney2026`)
- An Azure ML workspace (`mlw-ml-journey`)
- Verified everything in Azure ML Studio

### Commands used

```powershell
# Authenticate
az login

# Resource group
az group create --name rg-ml-journey --location canadacentral
az group show --name rg-ml-journey --output table

# Storage account (see "Challenges" below for why the provider check came first)
az provider show --namespace Microsoft.Storage --query registrationState --output tsv
az provider register --namespace Microsoft.Storage
az storage account create --name stmljourney2026 --resource-group rg-ml-journey --location canadacentral --sku Standard_LRS
az storage account show --name stmljourney2026 --resource-group rg-ml-journey --output table

# Azure ML workspace
az extension add -n ml
az ml workspace create --name mlw-ml-journey --resource-group rg-ml-journey --location canadacentral
```

### Challenges & how I fixed them

Documenting these because debugging cloud infrastructure is its own skill — these weren't blockers, they were the actual learning.

- **`az` not recognized after install** — PATH wasn't refreshed in the open terminal. Fix: close and reopen PowerShell in a new window after any CLI install.
- **PowerShell line continuation** — `\` (used in bash/Linux examples) isn't valid in PowerShell; either use a backtick (`` ` ``) or write the command on a single line. Switched to single-line commands to avoid the issue entirely.
- **`SubscriptionNotFound` on storage account creation, despite a valid, active subscription** — root cause was that the `Microsoft.Storage` resource provider wasn't yet registered on a brand-new subscription. Fixed by explicitly running `az provider register --namespace Microsoft.Storage` and waiting for `registrationState` to return `Registered` before retrying.
- **Budget alert set to 0.08% instead of 80%** — Azure's "% of budget" field takes a plain percentage number (`80`), not a decimal fraction (`0.08`). Easy to misread the first time.
- **Accidentally cloned the repo into `C:\WINDOWS\system32`** — cloned before navigating to a proper project folder. Fixed with `Move-Item` to relocate to `Documents\Projects`. Lesson for next time: always `cd` into the target folder *before* running `git clone`.


## Tech stack (growing each week)

`Azure ML` · `Azure CLI` · `PowerShell` · `Git/GitHub` · `Python` *(from Week 2 onward)*

---

## About this repo

I'm using this repo as a public, honest log of building production ML deployment skills — including the setup issues and fixes, not just the polished end state. If you're hiring for a Data Scientist / ML Engineer role and want to see how I approach and debug new tools, this is meant to show that directly.