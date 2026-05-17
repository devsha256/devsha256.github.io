---
layout: post
title: "Migrating 100+ APIs from CloudHub 1.0 to a New VPC"
date: 2025-08-20 10:30:00 +0530
tags: [mulesoft, cloudhub, devops, architecture]
featured: false
excerpt: "How I automated the migration of over 100 MuleSoft APIs, Anypoint MQs, and Azure DevOps pipelines to a new VPC using Postman JavaScript scripts and the CloudHub REST API."
---

When a client's parent company acquired them, the immediate challenge was migrating their entire MuleSoft estate — 100+ APIs, dozens of Anypoint MQ queues, and a forest of Azure DevOps pipelines — to the parent company's VPC. With a tight deadline and a small team, manual migration was not an option.

This post walks through the automation strategy we used.

## The Scope

| Asset Type | Count |
|---|---|
| Mule APIs (CloudHub 1.0) | 112 |
| Anypoint MQ Queues | 43 |
| Azure DevOps Pipelines | 38 |

Each API needed its VPC association updated, properties re-mapped to the new environment, and deployment verified.

## Step 1: Inventory with the CloudHub REST API

The first step was pulling a complete inventory using the CloudHub Management API:

```javascript
// Postman pre-request script
const baseUrl = pm.environment.get("CLOUDHUB_BASE_URL");
const orgId   = pm.environment.get("ORG_ID");
const envId   = pm.environment.get("ENV_ID");

pm.sendRequest({
  url: `${baseUrl}/cloudhub/api/v2/applications`,
  method: "GET",
  header: {
    "Authorization": `Bearer ${pm.environment.get("ACCESS_TOKEN")}`,
    "X-ANYPNT-ORG-ID": orgId,
    "X-ANYPNT-ENV-ID": envId
  }
}, (err, res) => {
  const apps = res.json().data;
  pm.environment.set("APP_LIST", JSON.stringify(apps));
  pm.environment.set("APP_COUNT", apps.length);
  console.log(`Found ${apps.length} applications`);
});
```

## Step 2: The Migration Script

With the inventory in hand, I wrote a Postman Collection runner script to iterate over each application and update its VPC binding:

```javascript
// Test script — runs after each API response
const apps      = JSON.parse(pm.environment.get("APP_LIST"));
let   idx       = parseInt(pm.environment.get("CURRENT_IDX") || "0");
const targetVpc = pm.environment.get("TARGET_VPC_ID");

const current = apps[idx];
if (!current) {
  console.log("✅ All applications migrated.");
  return;
}

// Patch the app's VPC association
const patchBody = {
  deploymentUpdateSideEffects: { reassignDomain: false },
  application: {
    muleVersion: { version: current.muleVersion },
    vpcId: targetVpc,
    region: current.region
  }
};

pm.environment.set("CURRENT_APP_NAME", current.domain);
pm.environment.set("PATCH_BODY", JSON.stringify(patchBody));
pm.environment.set("CURRENT_IDX", idx + 1);

// Trigger next iteration
pm.execution.setNextRequest("Patch Application VPC");
```

## Step 3: Validation

After migration, each app was validated automatically:

```javascript
// Verify the app is running in the correct VPC
const res = pm.response.json();
pm.test("Application in correct VPC", () => {
  pm.expect(res.vpcId).to.eql(pm.environment.get("TARGET_VPC_ID"));
});
pm.test("Application status is STARTED", () => {
  pm.expect(res.status).to.eql("STARTED");
});
```

## Anypoint MQ Migration

Anypoint MQ queues were migrated via the Anypoint MQ REST API, recreating each queue in the new environment with the same DLQ configuration, max retries, and TTL settings.

## Azure DevOps Pipeline Updates

Pipelines were updated using variable group replacement — a PowerShell script iterated over all pipeline YAML files and substituted old VPC endpoint variables with the new ones.

## Results

- ✅ All 112 APIs migrated within the maintenance window
- ✅ Zero production incidents post-migration
- ✅ Full rollback script prepared (unused)
- ⏱️ Total automation time: ~4 hours vs. estimated 3 weeks manual

The takeaway: investing a day in a well-structured automation script is almost always worth it over a week of repetitive manual work.
