# RFQ for the P{agency.fullName}}
### {{date}}</h3>

### Table of Contents
{{#list sections}}
* {{this}}
{{/each}}

Note: All sections of this RFQ will be incorporated into the contract except the Statement of Objectives, Instructions, and Evaluation Factors.

******

## 1. Definitions
{{#each definitions}}

{{this}}

{{/list}}

# 2. Services
## Brief Description of Services & Type of Contract

{{services.descriptionOfServices}}

{{services.naicsText}}

## Budget
The government is willing to invest a maximum budget of {{services.maxBudget}} in this endeavor.

{{#if services.travel.requirement}}

The Government anticipates travel will be required under this effort. Contractor travel expenses will not exceed {{services.travel.budget}}.

{{services.travelLanguage}}

{{else}}
The Government does not anticipate significant travel under this effort.

{{/if}}

## Contract Line Item Number (CLIN) Format
<table>
<th>
<th>Base Period: {{services.basePeriodDuration.number}} {{services.basePeriodDuration.unit}}</th>
</th>
<tr>
<td>CLIN 0001, FFP- Completion - The Contractor shall provide services for the Government in accordance with the Performance Work Statement (PWS)</td>
</tr>
</table>

<table>
<tr>
<td>Iteration Period of Performance</td><td>{{services.iterationPoP.number}} {{services.iterationPoP.unit}}</td>
</tr>
<tr>
<td>Price Per Iteration</td><td>$XXXXX (Vendor Completes)</td>
</tr>
<tr>
<td>Period of Performance</td><td>{{services.basePeriodDuration.number}} {{services.basePeriodDuration.unit}}</td>
</tr>
<tr>
<td>Firm Fixed Price (Completion):</td><td>$XXXXX (Vendor Completes)</td>
</tr>
<table>


## Payment Schedule

{{services.paymentSchedule}}

# 3. Objectives

## General Background
{{#if objectives.generalBackground}}

{{objectives.generalBackground}}

{{else}}

Please provide several paragraphs about your project's history, mission, and current state.
{{/if}}

## Users

The primary users may include any of the following:
{{#if objectives.users}}


The primary users will include the following:
{{#each users}}
1. {{this}}
{{/each}}

{{else}}

The primary users may include any of the following:

{{#each objectives.stockUsers}}
1. {{this}}
{{/each}}

{{/if}}

## User Research
{objectives.userResearch}

{{#if objectives.whatPeopleNeed}}
## Understand What People Need
{{objectives.whatPeopleNeed}}

{{/if}}

{{#if objectives.startToFinish}}

## Address the whole experience, from start to finish

{objectives.startToFinish}

{{/if}}


{{objectives.userAccess}}

{{#if objectives.universalRequirements}}
# Universal Requirements
{{#each objectives.universalRequirements}}
## {{title}}

{{body}}
{{/each}}
{{/if}}


## Specific Tasks and Deliverables
This {{doc_type}} will require the following services:
{{#each deliverables}}

{{display}}

{{/each}}

## Deliverables

{{objectives.definitionOfDone}}

{{#each deliverables}}

### {{display}}
{{text}}

{{/each}}

## Place of Performance
{{#if objectives.location.Requirement}}

{{#if objectives.location.location}}
The contractor shall have a full-time working staff presence at {{objectives.location.location}}. The contractor shall have additional facilities to perform contract functions as necessary.

{{else}}

The contractor shall have a full-time working staff presence at [LOCATION HERE]. The contractor shall have additional facilities to perform contract functions as necessary.

{{else}}
The contractor is not required to have a full-time working staff presence on-site.

{{/if}}

{{objectives.location.offSiteDevelopmentCompliance}}

{{/if}}

## Kick Off Meeting
{{#if_eq objectives.kickOffMeeting 'none'}}
A formal kick-off meeting will not be required.


{{/if_eq}}

{{#if_eq objectives.kickOffMeeting 'in-person'}}

{{objectives.kickOffMeetingInPerson}}

{{/if_eq}}

{{#if_eq objectives.kickOffMeeting 'remote'}}

{rfq.objectives.kickOffMeetingRemote}

{{/if_eq}}

# 4. Key Personnel

{{key_personnel.keyPersonnelIntro}}

## Security Clearance and Onsite Presence

{{#if_eq rfq.key_personnel.clearanceRequired 'None'}}

Contractor personnel will not be required to have a security clearance.

{{else}}

Some contractor personnel will be required to have a clearance at the level of {{key_personnel.clearanceRequired}}.
{{/if}}

{{#if key_personnel.onSiteRequired}}
An onsite presence by the contractor will be required.

{{else}}

An onsite presence by the contractor will not be required.
{{/if}}

## Key Personnel Evaluation
{{#if key_personnel.evaluateKeyPersonnel}}

{{key_personnel.keyPersonnelRequirements}}

{{else}}

{key_personnel.notEvaluateKeyPersonnel}

{{/if}}


{{key_personnel.performanceWorkStatement}}


# 5. Invoicing & Funding

{invoicing_funding.invoicing}

<p>The Contractor shall submit an original invoice for payment to the following office:

{{#if rfq.invoicing_funding.billingAddress}}

{{rfq.invoicing_funding.billingAddress}}

{{else}}

ADD BILLING ADDRESS HERE
{{/if}}

# 6. Inspection and Delivery
{{#each inspection_and_delivery.items}}

## {{title}}

{{body}}

{{/each}}


## Collaboration Environment
{{#if inspection_and_delivery.workspace}}
<p>{agency.name} is currently using {{inspection_and_delivery.workspace}} as their primary collaborative workspace tool. The contractor is required to establish a collaborative workspace using either this tool or another that both the contractor and the CO can agree upon.
{{/if}}

{{inspection_and_delivery.deliveringDeliverables}}

{{#if transitionActivities}
## Transition Activities
{{inspection_and_delivery.TransitionActivities}}
{{/if}}

# 7. Government Roles

For the completion of this task, the {{agency.fullName}} will provide access to the following stakeholders:",

{{#each government_roles.roles}}
## {{title}}

{{text}}

{/each}

{{#if special_requirements}}
# 8. Special Requirements

{{special_requirements.stakeholderIntro}}

{{#each special_requirements}}

## {{title}}

{{text}}

{/each}
{{/if}}


# 9. Additional Contract Clauses
{contract_clauses.text}

{{#if appendix}}

#  10. Appendix
{{#each appendix.items}}

{{this}}

{{/each}}
{{/if}}
