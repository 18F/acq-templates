Acquisition Plan for {{ buy.name }} | {{ date }}
==============================================


| Plan ID            | {{ id }}     |
|--------------------|-------------------------|
| Project Title      | {{ buy.name }}          |
| Plan Status        | {{ buy.acquisitionPlanStatus }}   |
| Project Number(s)  | {{ buy.id }}            |
| Solicitation Number| {{ buy.rfqId }}         |
| Estimated Dollar Value | {{ buy.dollars }}     |
| Nature of Action   | {{ buy.procurementVehicle }}  |
| Region             | Central Office<br />Service Central Office - General Services Administration<br />Office of Citizen Services and Communications   |
| Requiring Agency   | {{ buy.project.iaa.client.agency }}   |
| Bureau             | {{ buy.project.iaa.client.name }} |
| High Risk?         | No                      |
| Small Business Set-aside? | {{ buy.setAsideStatus }} |
| General Counsel Participation Needed? | No      |
| Level of Competition | {{ buy.competitionType }} |

[*Review GSAM 507.105 Contents of acquisition plans.*](http://farsite.hill.af.mil/vfgsara.htm)

## 7.105(a) Acquisition Background and Objectives

> **FAR guidance:** In order to facilitate attainment of the acquisition objectives, the plan must identify those milestones at which decisions should be made (see paragraph (b)(21) of this section). The plan must address all the technical, business, management, and other significant considerations that will control the acquisition. The specific content of plans will vary, depending on the nature, circumstances, and stage of the acquisition. In preparing the plan, the planner must follow the applicable instructions in paragraphs (a) and (b) of this section, together with the agency’s implementing procedures. Acquisition plans for service contracts or orders must describe the strategies for implementing performance-based acquisition methods or must provide rationale for not using those methods (see Subpart 37.6).

## 7.105(a)(1) Statement of Need

> **FAR guidance:** Introduce the plan by a brief statement of need. Summarize the technical and contractual history of the acquisition. Discuss feasible acquisition alternatives, the impact of prior acquisitions on those alternatives, and any related in-house effort.

{{ buy.description }}

### Technical History



### Contractual History

{{ buy.contractualHistory }}

### Acquisition Alternatives

There are no existing government efforts to perform same or similar work with
in-house employees. It is not feasible for {{ buy.project.iaa.client }} to perform this effort in-house
with government employees, nor is it feasible to perform this effort under an
agreement with another government agency.

**Full and Open Competition**: Market research revealed that the requirement is
within scope of an existing contract vehicle that can meet the government’s
requirements.  Therefore, a full and open competition is not considered to be an
optimal solution.

**Non-GSA GWAC**: including NASA SEWP III, ECSIII, and NIH CIO-SP2 – While these
GWACS allow for a variety of order types, there were no scope area provisions
that distinguish them from GSA contract vehicles. The additional time and
expense required initiating a new acquisition with a non-GSA vehicle and
contracting office during both the acquisition cycle and administration of the
task order cannot be justified. Therefore, a NON-GSA GWAC is not considered to
be an optimal solution.

**GSA GWACs, including Alliant, Alliant SB, VETS**: GSA GWAC’s provide for various
services including Information Technology, Financial Services and other
Professional Service solutions. Although the predominant nature of the current
requirement is Information Technology services, it is not the most optimal
contract vehicle for meeting the government’s requirements; therefore, a GSA
GWAC is not considered because there is an existing internal BPA that aligns
with the services.

**FSS Schedule**: Agile Delivery Services Blanket Purchase Agreement (aBPA), a
contracting vehicle from TTS, creates an opportunity for members of
the vendor community who specialize in agile software development to provide
those services to TTS.  

Due to the nature of this requirement, this acquisition will be issued in
accordance under the aBPA Pool Three Full Stack, under the GSA Multiple Award
Schedule (MAS), also known as Federal Supply Schedule (FSS) contract, Schedule
70, General Purpose Commercial Information Technology Equipment, Software, and
Services, under Special Item Number (SIN) 132-51, Information Technology
Professional Services.

## 7.105(a)(2) Applicable Conditions

> **FAR guidance:** State all significant conditions affecting the acquisition, such as --
>
>  (i) Requirements for compatibility with existing or future systems or  programs and
>
>  (ii) Any known cost, schedule, and capability or performance constraints.

There are no significant conditions affecting this procurement.

## 7.105(a)(3) Costs

> **FAR guidance:** Set forth the established cost goals for the acquisition and the rationale supporting them, and discuss related cost concepts to be employed, including, as appropriate, the following items:
>
> 1.  Life-cycle cost. Discuss how life-cycle cost will be considered. If it is not used, explain why. If appropriate, discuss the cost model used to develop life-cycle-cost estimates.
>
> 2.  Design-to-cost. Describe the design-to-cost objective(s) and underlying assumptions, including the rationale for quantity, learning-curve, and economic adjustment factors. Describe how objectives are to be applied, tracked, and enforced. Indicate specific related solicitation and contractual requirements to be imposed.
>
> 3.  Application of should-cost. Describe the application of should-cost analysis to the acquisition (see 15.407-4).

The total estimated cost is {{ buy.dollars }}. This acquisition will have period
of performance of {{ buy.periodOfPerformance }}.

The Independent Government Cost Estimate (IGCE) was created by using the
pre-established competitive prices under the GSA Schedule 70, MOBIS, and
[CALC tool](https://calc.gsa.gov/) rates.

Please see attached IGCE for a detailed price breakout by labor category.

Design-to-cost was not performed because it was not applicable due to the nature
of the requirement. This will be an open source software platform that will be
built using agile methodologies.

Should cost analysis, as defined in FAR 15.407-4, will not be performed because
Cost Analysis is not required when using GSA Schedules, or when adequate
competition is likely to occur.

## 7.105(a)(4) Capability or Performance Conditions

> **FAR guidance:** Specify the required capabilities or performance characteristics of the supplies or the performance standards of the services being acquired and state how they are related to the need.

> **TTS ACQ guidance:**
>
> For software development or other service buys - Pull the information that is in the Quality Assurance Surveillance Plan that discusses how the vendor will be measured.
>
> For COTS or HW buy discuss when the delivery needs to occur?

The product will be built in an agile way, using open source code,
human-centered design, and with an extensible infrastructure and robust
documentation.

Please see attached Quality Assurance and Surveillance Plan for a detailed
description of vendor measurement.

## 7.105(a)(5) Delivery or Performance-period Requirements

> **FAR guidance:** Describe the basis for establishing delivery or performance-period requirements (see Subpart 11.4). Explain and provide reasons for any urgency if it results in concurrency of development and production or constitutes justification for not providing for full and open competition.

### Period of performance

Period of performance shall be {{ buy.periodOfPerformance }}. The period of
performance was determined based on the needs of the project.

The period of performance is expected to begin within 10 calendar days after
award; anticipated award date is {{ buy.awardDate }}.

### Place of performance

The primary place of performance will be at the contractor’s facility. Work may
be performed at GSA Headquarters at 1800 F St. NW, Washington, DC, and alternate
sites. TTS is a distributed team.

## 7.105(a)(6) Trade Offs

> **FAR guidance:** Discuss the expected consequences of trade-offs among the various cost, capability or performance, and schedule goals.

The Government is more concerned with obtaining superior technical and
management capabilities than with making awards at the lowest overall price to
the Government. However, the Government will not make awards at a significantly
higher overall price to achieve slightly superior technical value. Offerors will
be advised in the RFQ that the technical evaluation factors combined are
significantly more important than price.

## 7.105(a)(7) Risks

> **FAR guidance:** Discuss technical, cost, and schedule risks and describe what efforts are planned or underway to reduce risk and the consequences of failure to achieve goals. If concurrency of development and production is planned, discuss its effects on cost and schedule risks.

### Technical Risk

Technical risk is low for the following reasons:

1. The adoption of Agile practices reduces the amount of unverified technical product;
1. COR will be appointed to manage the day to day activities of the contractor; and
1. The problem complexity of this task is modest.

### Cost Risk

There is a medium cost risk associated with this task order due to the
contracting type being labor-hour. The government will mitigate the cost risk
by having a project plan in place that monitors the performance of the 2-week
agile sprints, as well as, a daily stand up status meeting which will  help keep
the project on pace so that cost can be monitored and maintained. In addition,
the labor hour contract type will include a Not-to-Exceed amount that will be
closely monitored as the sprints progress.

### Schedule Risk

With the overall procurement, there is a low schedule risk associated
with having the contractor ready to begin work at time of award. There is a low
risk in meeting delivery schedules under day-to-day conditions. The Government
and Contractor will work together to set realistic timeframes and control
milestones associated with the support, and all other pertinent deliverables in
accordance with the awarded contract. As part of this being purchased off of the
Agile Blanket Purchase Agreement (aBPA), work will be conducted in two-week
sprints and reviewed at the end of each sprint for acceptability before moving
on. The contractor and government may mutually agree to alter sprint length as
needed.

## 7.105(a)(8) Acquisition Streamlining

> **FAR guidance:** If specifically designated by the requiring agency as a program subject to acquisition streamlining, discuss plans and procedures to:
>
> 1.  Encourage industry participation by using draft solicitations, presolicitation conferences, and other means of stimulating industry involvement during design and development in recommending the most appropriate application and tailoring of contract requirements;
>
> 2.  Select and tailor only the necessary and cost-effective requirements; and
>
> 3.  State the timeframe for identifying which of those specifications and standards, originally provided for guidance only, shall become mandatory.
>

### Industry Involvement Plan

This program has not been specifically designated by {{ buy.project.iaa.client.name }} as a
program that is subject to acquisition streamlining. Therefore, an industry
involvement plan is not required.

### Selection and Tailoring of Requirements Plan

This program has not been specifically designated by {{ buy.project.iaa.client.name }} as a
program that is subject to acquisition streamlining. Therefore, selection
and tailoring of requirements plan is not required.

### Timeframe for Finalizing Mandatory Requirements

This program has not been specifically designated by {{ buy.project.iaa.client.name }} as a
program that is subject to acquisition streamlining. The mandatory requirements
will be finalized prior to release of the solicitation to the contractor.

## 7.105(b)(1) Sources

> **FAR guidance:** Indicate the prospective sources of supplies or services that can meet the need. Consider required sources of supplies or services (see part 8) and sources identifiable through databases including the Governmentwide database of contracts and other procurement instruments intended for use by multiple agencies available at https://www.contractdirectory.gov/contractdirectory/. Include consideration of small business, veteran-owned small business, service-disabled veteran-owned small business, HUBZone small business, small disadvantaged business, and women-owned small business concerns (see part 19), and the impact of any bundling that might affect their participation in the acquisition (see 7.107) (15 U.S.C. 644(e)). When the proposed acquisition strategy involves bundling, identify the incumbent contractors and contracts affected by the bundling. Address the extent and results of the market research and indicate their impact on the various elements of the plan (see part 10)

### Sources

Market research indicates that the services that are required are available as
commercial services under the Agile BPA (aBPA), the Pool Three Full Stack (17
small and large vendors), under the GSA Multiple Award Schedule (MAS), also
known as Federal Supply Schedule (FSS) contract, Schedule 70, General Purpose
Commercial Information Technology Equipment, Software, and Services, under
Special Item Number (SIN) 132-51, Information Technology Professional Services.
There are several sources that have been identified as being able to provide
these services under the Agile BPA.

### Market Research

Reference Acquisition Alert 2013-03 determines TTS’s Agile Delivery Services
Blanket Purchase Agreement (aBPA) Pool 3 is a multi-award BPA set up with 17
vendors consisting of nine (9) small businesses and eight (8) other than small
businesses.  An aBPA was established to acquire agile delivery capabilities such
as: user-centered design, agile architecture, agile software development,
test-driven development, API-first design, DevOps and full-stack teams to help
work on TTS-managed projects. This is part of TTS's efforts to increase the
capacity to help agency partners do great work, through using agile processes to
transform the way the federal government buys and builds digital services. Due
to the nature of this requirement, by using the aBPA vehicle, the resulting call
order will deliver the requirement with a contractor that has already been
identified as capable of working in an agile way.

## 7.105(b)(2) Competition

> **FAR guidance:**
>
> 1.  Describe how competition will be sought, promoted, and sustained throughout the course of the acquisition. If full and open competition is not contemplated, cite the authority in 6.302, discuss the basis for the application of that authority, identify the source(s), and discuss why full and open competition cannot be obtained.
>
> 2.  Identify the major components or subsystems. Discuss component breakout plans relative to these major components or subsystems. Describe how competition will be sought, promoted, and sustained for these components or subsystems.
>
> 3.  Describe how competition will be sought, promoted, and sustained for spares and repair parts. Identify the key logistic milestones, such as technical data delivery schedules and acquisition method coding conferences, that affect competition.
>
> 4.  When effective subcontract competition is both feasible and desirable, describe how such subcontract competition will be sought, promoted, and sustained throughout the course of the acquisition. Identify any known barriers to increasing subcontract competition and address how to overcome them.

This will be a competitive procurement on the Agile BPA using FAR Part 8.4
procedures. The award will be based on the best value determined from an
evaluation of process, technical, scoring plan, and price. This allows the
Government to accomplish its mission in a more efficient and effective manner by
gaining contractor expertise in the areas required. The intent of the Government
is to make a Best Value Selection based on the offer that provides the most
advantageous and best value to the Government, all factors and prices are
considered.   

### Major Component Competition

There are no major components competition anticipated under this procurement.

### Spare and Repair Parts Competition

There are no spare and repair parts competitions anticipated under this
procurement.

### Subcontracting Competition

Contractors must adhere to FAR Clause 52.244-5, “Competition in Subcontracting,”
where the prime shall select subcontractors on a competitive basis to the
maximum practical extent.

## 7.105(b)(3) Contract Type Selection

> **FAR guidance:** Discuss the rationale for the selection of contract type. For other than firm-fixed-price contracts, see 16.103(d) for additional documentation guidance. Acquisition personnel shall document the acquisition plan with findings that detail the particular facts and circumstances, (e.g., complexity of the requirements, uncertain duration of the work, contractor’s technical capability and financial responsibility, or adequacy of the contractor’s accounting system), and associated reasoning essential to support the contract type selection. The contracting officer shall ensure that requirements and technical personnel provide the necessary documentation to support the contract type selection.

Based on the nature of this requirement, the government intends to award a
labor-hour (LH) task order under the master Agile BPA (aBPA) terms and
conditions because the work required for this task order cannot be defined due
to the prototype being built in an agile way, using open source code,
human-centered design, and with an extensible infrastructure and robust
documentation.


## 7.105(b)(4) Source Selection Procedures

> **FAR guidance:** Discuss the source-selection procedures for the acquisition, including the timing for submission and evaluation of proposals, and the relationship of evaluation factors to the attainment of the acquisition objectives (see subpart 15.3). When an EVMS is required (see FAR 34.202(a)) and a pre-award IBR is contemplated, the acquisition plan must discuss—
>
> 1.  How the pre-award IBR will be considered in the source selection decision;
>
> 2.  How it will be conducted in the source selection process (see FAR 15.306); and
>
> 3.  Whether offerors will be directly compensated for the costs of participating in a pre-award IBR.

This requirement will be a competitive acquisition. Due to the nature of the
requirement, the timeframe for submission of quotations is 14 calendar days
which provides enough time for potential vendors to submit quotations. Questions
and/or comments regarding this RFQ shall be submitted as issues within the
GitHub repository at {{ buy.githubRepository }} within 5 calendar days
of RFQ posting, to allow the Government sufficient time to respond. All
questions and comments will be publicly available. Interested vendors shall
subscribe to the repository for changes and comments. Questions or comments
received after the required deadline may not be answered. Vendors are
instructed to submit their quotes electronically through the eBuy web portal by
the official closing date and time identified. Late quotations will not be
considered.

The source selection organization for this procurement is:

Chairperson: TBD, GSA

The Technical Evaluation Panel will consist of the following members:

{{ buy.panelists }}

The Government will evaluate technical Quotes based on the criteria
shown below. The TEP will evaluate the submissions to arrive at a rating
for the technical quote as a whole. Award will be made to the Offeror
whose quote provides the best value to the government.

The basis for award shall be the best value determination using the
following evaluation criteria: Excellent, Good, Marginal, Acceptable, and
Unacceptable. The task order will be awarded based on evaluation of the
price and technical quotes as submitted by each offeror.

The order of importance of the evaluation criteria is:

1.  Management Approach
1.  Technical Approach
1.  Key Personnel
1.  Past Performance

The four (4) non-price criteria, when combined, are significantly more
important than price when determining best value. However, if quotes are
evaluated as technically equal in quality, price will become a major
consideration in selecting the successful vendor. The Government plans
to award without discussions, however the Government reserves the right
to hold discussions if needed.

## 7.105(b)(5) Acquisition Considerations

> **FAR guidance:**
>
> 1. For each contract contemplated, discuss use of multiyear contracting, options, or other special contracting methods (see [*part 17*](https://www.acquisition.gov/far/html/FARTOCP17.html#wp223561)); any special clauses, special solicitation provisions, or FAR deviations required (see [*subpart 1.4*](https://www.acquisition.gov/far/html/Subpart%201_4.html#wp1044104)); whether sealed bidding or negotiation will be used and why; whether equipment will be acquired by lease or purchase (see [*subpart 7.4*](https://www.acquisition.gov/far/html/Subpart%207_4.html#wp1084017)) and why; and any other contracting considerations. Provide rationale if a performance-based acquisition will not be used or if a performance-based acquisition for services is contemplated on other than a firm-fixed-price basis (see [*37.102*](https://www.acquisition.gov/far/html/Subpart%2037_1.html#wp1082895)(a), [*16.103*](https://www.acquisition.gov/far/html/Subpart%2016_1.html#wp1085506)(d), and [*16.505*](https://www.acquisition.gov/far/html/Subpart%2016_5.html#wp1095799)(a)(3)).
>
> 1.  For each order contemplated, discuss—
>
>     a.  For information technology acquisitions, how the capital planning and investment control requirements of [*40 U.S.C. 11312*](http://uscode.house.gov/uscode-cgi/fastweb.exe?getdoc+uscview+t37t40+1574+51++%2840%29%20%20AND%20%28%2840%29%20ADJ%20USC%29%3ACITE%20%20%20%20%20%20%20%20%20) and OMB Circular A-130 will be met (see [*7.103*](https://www.acquisition.gov/far/html/Subpart%207_1.html#wp1098057)(v) and [*part 39*](https://www.acquisition.gov/far/html/FARTOCP39.html#wp223485)); and
>
>     b.  Why this action benefits the Government, such as when—
>
>        i.  The agency can accomplish its mission more efficiently and effectively (e.g., take advantage of the servicing agency’s specialized expertise; or gain access to contractors with needed expertise); or
>
>        ii. Ordering through an indefinite delivery contract facilitates access to small business concerns, including small disadvantaged business concerns, 8(a) contractors, women-owned small business concerns, HUBZone small business concerns, veteran-owned small business concerns, or service-disabled veteran-owned small business concerns.
>
> 1.  For information technology acquisitions using Internet Protocol, discuss whether the requirements documents include the Internet Protocol compliance requirements specified in [*11.002*](https://www.acquisition.gov/far/html/Subpart%2011_1.html#wp1086792)(g) or a waiver of these requirements has been granted by the agency’s Chief Information Officer.
>
> 1.  For each contract (and order) contemplated, discuss the strategy to transition to firm-fixed-price contracts to the maximum extent practicable. During the requirements development stage, consider structuring the contract requirements, e.g., contract line items (CLINS), in a manner that will permit some, if not all, of the requirements to be awarded on a firm-fixed-price basis, either in the current contract, future option years, or follow-on contracts. This will facilitate an easier transition to a firm-fixed-price contract because a cost history will be developed for a recurring definitive requirement.

### Equipment Lease or Purchase

This requirement does not involve Lease or Purchase items.

### Section 508

Section 508 of the Rehabilitation Act of 1973, as amended, requires that when
Federal agencies develop, procure, maintain, or use electronic and information
technology, Federal employees with disabilities have access to and use of
information and data that is comparable to the access and use by Federal
employees who are not individuals with disabilities, unless an undue burden
would be imposed on the agency. Section 508 also requires that individuals with
disabilities, who are members of the public seeking information or services from
a Federal agency, have access to and use of information and data that is
comparable to that provided to the public who are not individuals with
disabilities, unless an undue burden would be imposed on the agency.

The following standard is applicable for compliance:

1194.22 Web-based Intranet and Internet Information and Applications.

The contractor should review the following websites for additional 508 information:
- http://www.section508.gov/index.cfm?FuseAction=Content&ID=12
- http://www.access-board.gov/508.htm
- http://www.w3.org/WAI/Resources

### Option Clauses

Option Clause: FAR 52.217-8 -- OPTION TO EXTEND SERVICES

The Government may require continued performance of any services within the
limits and at the rates specified in the contract.

Option Clause: FAR 52.2147-9 -- OPTION TO EXTEND THE TERM OF THE CONTRACT

The Government may extend the term of this contract by written notice to the
Contractor within 5 days provided that the Government gives the Contractor a
preliminary written notice of its intent to extend at least 15 days before the
contract expires.

Option Clause: GSAR 552.217-71 – NOTICE REGARDING OPTION(S)

GSA has included an option to extend the term of this contract in order to
demonstrate the value it places on quality performance by providing a mechanism
for continuing a contractual relationship with a successful Offeror that
performs at a level which meets or exceeds GSA’s quality performance
expectations as communicated to the Contractor, in writing, by the Contracting
Officer or designated representative.

### Performance Based Elements

Performance based elements will be used to the maximum extent practicable
because there are metrics and standards such as open source code, human-centered
design, an extensible infrastructure, robust documentation, and other
deliverables that need to be achieved in accordance with certain performance
objectives. Requirements have been defined by the PWS with expected outcomes;
the contractor will be required to submit a Quality Assurance Plan (QAP); and
the contractor’s performance will be monitored based on the government’s Quality
Assurance Surveillance Plan (QASP).

### Monitoring Office (or Individual)

The following individuals will monitor contractor performance:

- Client Technical Point of Contact: {{ buy.productLead.name }}
- {{ buy.contractingOffice.name }} Program Manager: {{ buy.contractingOffice.programManager.name }}
- {{ buy.contractingOffice.name }} Contracting Specialist(s): {{ buy.contractingSpecialist.name }}
- {{ buy.contractingOffice.name }} Contracting Officer: {{ buy.contractingOfficer.name }}

{{ buy.contractingOfficerRepresentative.name }} will perform all Contracting Officer's
Representative (COR) responsibilities for the resulting contract.  The COR
responsibilities will be described in a COR Letter of Appointment.  The COR and
Technical Point of Contact (TPOC) will be responsible for quality assurance
surveillance.  The Contracting Officer has the authority for issuing
modifications, and changes.

### Rationale for Not Using Performance Based Contracting Methods

Performance based elements will be used to the maximum extent practicable.

## 7.105(b)(6) Budgeting & Funding

> **FAR guidance:** Include budget estimates, explain how they were derived, and discuss the schedule for obtaining adequate funds at the time they are required (see subpart 32.7).

The estimated cost of this acquisition is {{ buy.dollars }} based on the
Independent Government Cost Estimate (IGCE). This acquisition will have
a period of performance lasting up to {{ buy.periodOfPerformance }}.

The IGCE was developed using median labor rates for aBPA labor rates for the
types of labor categories needed to support this acquisition.

Services to be provided under this task order are severable. Funds have been
designated for the base and option periods under Interagency Agreement No.
{{ buy.project.iaa.id }} in the amount of {{ buy.project.dollars }}.


## 7.105(b)(7) Product or Service Descriptions

> **FAR guidance:** Explain the choice of product or service description types (including performance-based acquisition descriptions) to be used in the acquisition.

{{ buy.description }}

Please see the attached PWS for a full description of the requirements for the
solution.

## 7.105(b)(8) Priorities Allocations and Allotments

> **FAR guidance:** When urgency of the requirement dictates a particularly short delivery or performance schedule, certain priorities may apply. If so, specify the method for obtaining and using priorities, allocations, and allotments, and the reasons for them (see subpart 11.6).

There are no priorities, allocations, or allotments for this procurement. If the
priority changes during the course of performance, GSA will obtain the
appropriate rating and modify the contract accordingly.

## 7.105(b)(9) Contractor vs. Government Performance

> **FAR guidance:** Address the consideration given to OMB Circular No. A-76 (see subpart 7.3).

There is no Contractor versus Government Performance considerations
under this contract. This acquisition is not related to an A-76 effort
and does not compare government versus contractor performance of the
requirements. This requirement does not fall under OMB Circular A-76 as
the Government intends to contract with the private sector.

The services required are currently performed by industry. The Government does
not have the resources required to successfully provide the required services.

## 7.105(b)(10) Inherently Governmental Functions Consideration

> **FAR guidance:** Address the consideration given to subpart 7.5.

This requirement is for commercial services and not an inherently governmental
function or critical function pursuant to FAR 7.503 or as defined in FAR 2.101.

The following resources were reviewed in making this determination:
- GSAM Subpart 507.5, Inherently Governmental Functions
- OFPP Policy Letter 11-01, Performance of Inherently Governmental and Critical
Functions
- GSA Acquisition Alert 2011-07, Inherently Governmental and Critical Functions.

## 7.105(b)(11) Management Information Requirements

> **FAR guidance:** Discuss, as appropriate, what management system will be used by the Government to monitor the contractor’s effort. If an Earned Value Management System is to be used, discuss the methodology the Government will employ to analyze and use the earned value data to assess and monitor contract performance. In addition, discuss how the offeror’s/contractor’s EVMS will be verified for compliance with the American National Standards Institute/Electronics Industries Alliance (ANSI/EIA) Standard-748, Earned Value Management Systems, and the timing and conduct of integrated baseline reviews (whether prior to or post award). (See 34.202.)

GSA will provide contract administration for this task order. The Government
will use the draft Quality Assurance Surveillance Plan (QASP) (will be provided)
to monitor the contractor’s performance. The QASP will provide oversight help to
ensure that service levels reach and maintain the required levels for
performance of this task. Further, the QASP provides the Government with a
proactive way to avoid unacceptable or deficient performance, and provides
verifiable input for the required Past Performance Information Assessments. The
QASP is a living document and may be updated by the Government as necessary. Any
updates to the QASP will be provided to the contractor. If needed, the draft
QASP will be updated within 10 business days of the contract kick-off meeting by
TTS Product Lead and/or the COR. The Government and Contractor will jointly
conduct calibration and quality review sessions as required.

## 7.105(b)(12) Make or Buy

> **FAR guidance:** Discuss any consideration given to make-or-buy programs (see 15.407-2).

In accordance with FAR 15.407-2(c), this acquisition will not require a
make-or-buy program because it is less than $13.5M, and the Contracting Officer
does not consider the information necessary or applicable due to the nature of
the project.  

## 7.105(b)(13) Test and Evaluation

> **FAR guidance:** To the extent applicable, describe the test program of the contractor and the Government. Describe the test program for each major phase of a major system acquisition. If concurrency is planned, discuss the extent of testing to be accomplished before production release.

The QASP specifies particular testing and evaluation criteria (e.g. continuous
integration, documentation, and the use of modern testing frameworks) that the
government feels will lead to positive outcomes from the vendor.

## 7.105(b)(14) Logistics Considerations

> **FAR guidance:** Describe
>
> 1.  The assumptions determining contractor or agency support, both initially and over the life of the acquisition, including consideration of contractor or agency maintenance and servicing (see subpart 7.3), support for contracts to be performed in a designated operational area or supporting a diplomatic or consular mission (see 25.301-3); and distribution of commercial items;
>
> 1.  The reliability, maintainability, and quality assurance requirements, including any planned use of warranties (see part 46);
>
> 1.  The requirements for contractor data (including repurchase data) and data rights, their estimated cost, and the use to be made of the data (see part 27); and
>
> 1.  Standardization concepts, including the necessity to designate, in accordance with agency procedures, technical equipment as “standard” so that future purchases of the equipment can be made from the same manufacturing source.

### Contractor or Agency Support Assumptions

There are no Contractor or Agency Support Assumptions for this contract.

### Requirements for Contractor Data

18F intends that any data or deliverable created as a result of the work
performed under the call order be committed to the public domain.

Further, 18F intends to commit the following items, to the public domain, at a
minimum:
- All data, documents, graphics and code created under this call order
including but not limited to, plans, reports, schedules, schemas, metadata,
architecture designs, and the like;
- Any and all new open source software created by the contractor and forks or
branches of current open source software where the contractor has made a
modification; and,
- Any and all new tooling, scripting configuration management, infrastructure
as code, or any other final changes or edits to successfully deploy or operate
the software.

The contractor shall use open source technologies wherever possible, in support
of the 18F Source Code Policy. All licenses must be expressly listed in the
deliverable. Regardless of license(s) used (e.g., MIT, GPL, Creative Commons 0)
the license(s) shall be clearly listed in the documentation.

If the contractor needs to use work that does not have an open source license,
the contractor is required to request permission from 18F, in writing, before
utilizing that work in any way in connection with the order. If approved, all
licenses shall be clearly set forth in a conspicuous place when work is
delivered to 18F.

If an open source license provides implementation guidance, the contractor shall
ensure compliance with that guidance. If implementation guidance is not
available, the contractor shall attach or include the license within the work
itself. Examples of this include code comments at the beginning of a file or
contained in a license file within a software repository.

### Quality Assurance, Warranty Plans

The Contractor shall indicate the warranty period and license period of any
software provided throughout the life cycle of this contract requirement.

A Quality Assurance Plan (QAP) will be a required deliverable under this
contract and a Quality Assurance Surveillance Plan (QASP) will be utilized by
the government to monitor the performance of the contractor. Additionally, the
contractor shall apply industry standards and best practices to outline
quality assurance practices in program management, including, at a minimum,
identification of quality control factors and processes, evaluation methods,
earned value management, and process improvement.

### Standardization Concepts

The product will be built using industry standards and best practices from the
beginning. Accordingly, there will not be a future need to standardize during
the life of the product.

## 7.105(b)(15) Government Furnished Property

> **FAR guidance:** Indicate any Government property to be furnished to contractors, and discuss any associated considerations, such as its availability or the schedule for its acquisition (see 45.102).

The Government will not furnish any property in accordance with performance
under this contract.

## 7.105(b)(16) Government Furnished Information

> **FAR guidance:** Discuss any Government information, such as manuals, drawings, and test data, to be provided to prospective offerors and contractors. Indicate which information that requires additional controls to monitor access and distribution (e.g., technical specifications, maps, building designs, schedules, etc.), as determined by the agency, is to be posted via the enhanced controls of the GPE at http://www.fedbizopps.gov (see 5.102(a)).

The Government will furnish any necessary data at time of award.

The contractor shall be responsible for properly protecting all information
used, gathered, disclosed, or developed as a result of work under this contract.
The contractor shall also protect all Government data by treating information as
sensitive. All information gathered or created under this contract shall be
considered as Sensitive But Unclassified (SBU) information. If contractor
personnel must remove any information from the primary work area they should
protect it to the same extent they would their proprietary data and/or company
trade secrets. The use of this data is subject to the Privacy Act and shall be
utilized in full accordance with all rules of conduct as applicable to Privacy
Act Information

## 7.105(b)(17) Environmental and Energy Conservation Objectives

> **FAR guidance:** Discuss all applicable environmental and energy conservation objectives associated with the acquisition (see part 23), the applicability of an environmental assessment or environmental impact statement (see 40 CFR 1502), the proposed resolution of environmental issues, and any environmentally-related requirements to be included in solicitations and contracts (see 11.002 and 11.303).

Pursuant to FAR 23.000, no pollution control, energy conservation, hazardous
material, or uses of recovered material issues have been identified for this
acquisition. This contract will not require the use of Class 1 Ozone Depleting
Substances (ODS).

**Proposed Environmental Assessment Statement Issue Resolution**
There are no proposed environmental assessment statement issue resolutions for
this acquisition.

**Proposed Environmental Impact Statement Issue Resolution**
There are no proposed environmental impact statement issue resolutions for this
acquisition.

## 7.105(b)(18) Security Considerations

> **FAR guidance**
>
> 1.  For acquisitions dealing with classified matters, discuss how adequate security will be established, maintained, and monitored (see subpart 4.4).
>
> 1.  For information technology acquisitions, discuss how agency information security requirements will be met.
>
> 1.  For acquisitions requiring routine contractor physical access to a Federally-controlled facility and/or routine access to a Federally-controlled information system, discuss how agency requirements for personal identity verification of contractors will be met (see subpart 4.13).
>
> 1.  For acquisitions that may require Federal contract information to reside in or transit through contractor information systems, discuss compliance with subpart 4.19.

**Security: Low**

All GSA Contractors must comply with the GSA policies below (these documents are all referenced within the GSA IT
Security Policy):

- GSA Information Technology (IT) Security Policy, CIO P 2100.1l.
- GSA Order CIO P 2181.1 “GSA HSPD-12 Personal Identity Verification and Credentialing Handbook”, October 20, 2008.
- GSA Order CIO 2104.1, “GSA Information Technology (IT) General Rules of Behavior”, July 3, 2003.
- GSA Order CPO 1878.1, “GSA Privacy Act Program”, dated October 27, 2003.
- GSA IT SPG 04-26, “FISMA Implementation”.”
- GSA IT SPG 06-29, “Contingency Plan Testing”.”
- GSA IT SPG 06-30, “Managing Enterprise Risk.”
- GSA IT SPG 08-39,IT Security Program Management Implementation Plan FY 2009
- GSA IT SPG 09-44, “Plan of Action and Milestones (POA&M).”
- NIST Special Publication 800-53 Revision 3, “Recommended Security Controls for Federal Information Systems.”
- NIST Special Publication 800-53A, “Guide for Assessing the Security Controls in Federal Information Systems.”

Contractors are also required to comply with Federal Information Processing
Standards (FIPS), the “Special Publications 800 series” guidelines published by
NIST, and the requirements of FISMA.

In the event that performance of this task order requires access to Privacy
Information, Contractors shall adhere to the Privacy Act, Title 5 of the U.S.
Code, Section 552a and any other applicable rules and regulations.

The work shall be performed off-site and will not need a GSA Authority to
Operate because it is not a live system, and it will not be owned or run by GSA.
The software will be hosted on GSA-approved and GSA ATO’d Cloud.gov Platform as
a Service (PaaS) solution. Furthermore, the vendor will work with dummy data and
publicly-available data sets. Accordingly, privacy is a non-issue with respect
to this procurement.

The Federal Acquisition Regulation (FAR) requires that all federal entities
ensure that all Contractors have current and approved security background
investigations that are equivalent to investigations performed on Federal
employees. As outlined in GSA CIO P 2100.1C – GSA Information Technology
Security Policy, Standard Operating Procedure for GSA HSPD-12, Personnel
Security Process dated November 18, 2005, and the Homeland Security Presidential
Directive – 12 (HSPD-12). The following is required:

> Effective October 27, 2005, all new GSA associates and contract
employees must have a National Agency Check with written Inquiries
(NACI)\~:\~ National Agency Check with written Inquiries and Credit
(NACIC) for contract employees\~:\~ or equivalent investigation
initiated. Successful results from the FBI National Criminal History
Check (i.e. fingerprint check) portion of the NACI/NACIC must be
received for issuance of an identity credential for access to GSA
facilities and IT systems.

The Contractor shall obtain approved background investigations to accomplish its
support to GSA. Contractor personnel shall be required to have the appropriate
level of investigation and/or security clearance for each selected site and
information system. Contractor personnel shall also be required to submit a
Request for User ID when access is required to a Government computer, to include
the submission of proof, to GSA, that a favorable National Agency Check has been
completed. The Contractor may be required to have access to live data and/or
sensitive information and resources during performance of this authorized access
to such information and shall be required to sign a non-disclosure. The
Contractor shall observe and comply with the security provisions in effect at
each selected site. Any required identification badges shall be worn and
displayed at all times. Contractor personnel shall submit a Request for Deletion
of User ID when access in no longer required. The results of these clearances
shall be provided to the Federal Government ISSM or ISSO upon request, but
consistent with maintaining privacy of the individuals. All personnel with
access to root or pseudo root access of servers and database administrators
shall meet these requirements.

## 7.105(b)(19) Contract Administration

> **FAR guidance:** (19) Contract administration. Describe how the contract will be administered. In contracts for services, include how inspection and acceptance corresponding to the work statement’s performance criteria will be enforced.

Contract administration will be performed by the following individuals:

- Client Technical Point of Contact: {{ buy.productLead.name }}
- Contracting Officer Representative: {{ buy.contractingOfficerRepresentative.name }}
- {{ buy.contractingOffice.name }} Program Manager: {{ buy.contractingOffice.programManager.name }}
- {{ buy.contractingOffice.name }} Contracting Specialist(s): {{ buy.contractingSpecialist.name }}
- {{ buy.contractingOffice.name }} Contracting Officer: {{ buy.contractingOfficer.name }}

## 7.105(b)(20) Other Considerations

> **FAR guidance:** Discuss, as applicable:
>
> 1.  Standardization concepts;
>
> 1.  The industrial readiness program;
>
> 1.  The Defense Production Act;
>
> 1.  The Occupational Safety and Health Act;
>
> 1.  Support Anti-terrorism by Fostering Effective Technologies Act of 2002 (SAFETY Act) (see subpart 50.2);
>
> 1.  Foreign sales implications;
>
> 1.  Special requirements for contracts to be performed in a designated operational area or supporting a diplomatic or consular mission; and
>
> 1.  Any other matters germane to the plan not covered elsewhere.

There are no other considerations.

## 7.105(b)(21) Milestones for the Acquisition Cycle Applicable Milestones

> **FAR guidance:** (21) Milestones for the acquisition cycle. Address the following steps and any others appropriate:
>
> -   Acquisition plan approval.
>
> -   Statement of work.
>
> -   Specifications.
>
> -   Data requirements.
>
> -   Completion of acquisition-package preparation.
>
> -   Purchase request.
>
> -   Justification and approval for other than full and open competition where applicable and/or any required D&F approval.
>
> -   Issuance of synopsis.
>
> -   Issuance of solicitation.
>
> -   Evaluation of proposals, audits, and field reports.
>
> -   Beginning and completion of negotiations.
>
> -   Contract preparation, review, and clearance.
>
> -   Contract award

### Acquisition Plan Approval

Planned:

Actual:

### Statement of Work

Planned:

Actual:

### Specifications 6/15/2016

Planned:

Actual:

### Package Completion 6/15/2016

Planned:

Actual:

### Purchase Request 6/15/2016

Planned:

Actual:

### Justification for Approval 6/15/2016

Planned:

Actual:

### Issuance of Solicitation 8/2/2016

Planned:

Actual:

### Proposal Evaluation 8/9/2016

Planned:

Actual:

### Negotiation Begin 8/10/2016

Planned:

Actual:

### Negotiation Completion 8/16/2016

Planned:

Actual:

### Contract Preparation 8/22/2016

Planned:

Actual:

### Contract Review 8/24/2016

Planned:

Actual:

### Contract Award 8/31/2016

Planned:

Actual:

## Signatures

Requiring Office Planner


__________________________________ 	            ______________		
{{ buy.contractingOffice.programManager.name }}                   Date
{{ buy.contractingOffice.programManager.email }}



________________________________________   	______________
{{ buy.contractingSpecialist.name }}                 	 Date
{{ buy.contractingSpecialist.email }}



________________________________________   	______________
{{ buy.contractingOfficer.name }}, Contracting Officer       Date
{{ buy.contractingOfficer.email }}


## Approval Information

Approval Information


Approval Authority - Contracting Officer




________________________________________   	______________
{{ buy.contractingOfficer.name }}, Contracting Officer       Date
{{ buy.contractingOfficer.email }}


Approval Authority - One Level above the Contracting Officer



________________________________________   	______________
{{ buy.contractingSupervisor.name }}    		      Date
{{ buy.contractingSupervisor.email }}

Plan Status Approval Status    {{ buy.acquisitionPlanStatus }}

## File Attachments

No attachments available N/A
