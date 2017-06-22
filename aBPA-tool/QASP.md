## {{projectTitle}}
## Agile Delivery Services Blanket Purchase Agreement
# Request for Quotation
## Quality Assurance Surveillance Plan (“QASP”)

## 0.0 Introduction
The Technology Transformation Service has developed this Quality Assurance Surveillance Plan (QASP) to evaluate contractor actions while implementing the Performance Work Statement (PWS). It is designed to provide an effective surveillance method of monitoring contractor performance for each listed objective on the Performance Requirements Summary in the call order. It also provides a systematic method to evaluate the services the contractor is required to furnish.
 
## 1.0 Standard
The contractor is responsible for management and quality control actions to meet the terms of the call order. The contractor shall perform all work required in a satisfactory manner in accordance with the requirements of the PWS. The COR shall notify the CO for appropriate action if it is likely that the contractor will not achieve successful final delivery of the software code in accordance with the performance objectives and acceptable quality levels identified below.
 
## 2.0 The Contracting Officer
The contracting officer (CO) is responsible for monitoring contract compliance, contract administration, and cost control and for resolving any differences between the observations documented by the [Insert title of government authority for performance management: "contracting officer's representative (COR), "administrative contracting officer (ACO)," "quality assurance representative (QAR),” or "program manager (PM)"] and the contractor. The CO will designate one full-time COR as the government authority for performance management. The number of additional representatives serving as technical inspectors depends on the complexity of the services measured, as well as the contractor’s performance, and must be identified and designated by the CO.
 
## 3.0 The Contracting Officer’s Representative
The contracting officer’s representative (COR) is designated in writing by the CO to act as his or her authorized representative to assist in administering a contract. COR limitations are contained in the written appointment letter. The COR is responsible for technical administration of the project and ensures proper government surveillance of the contractor’s performance. The COR is not empowered to make any contractual commitments or to authorize any contractual changes on the government’s behalf. Any changes that the contractor deems may affect contract price, terms, or conditions shall be referred to the CO for action.  The COR will have the responsibility for completing QA monitoring forms used to document the inspection and evaluation of the contractor’s work performance. Government surveillance may occur under the inspection of services clause for any service relating to the contract.
 
## 4.0 Performance Requirements Summary
The COR will evaluate the performance objectives through surveillance as reflected below by reviews and acceptance of work products and services. As indicated, the COR will assess progress towards the final delivered software code. Note that the performance requirements listed below are required for the final deliverable. However, the sprints and incremental delivery of code will be assessed by the government to ensure that the contractor is on a path to successful final delivery. 
 
Deliverable or Required Services Performance Standard(s):
 
   **Deliverable or Required Services** | **Performance Standard(s)** | **Acceptable Quality Level** | **Method of Surveillance**
   ----------- | ---------------- | -------------- | ---------------
   Tested Code | Code delivered under the order must have substantial test code coverage and a clean code base | Minimum of 90% test coverage of all relevant code | Combination of manual review and the results from automated testing
   Error-free Code | [18F Front End Guide](https://frontend.18f.gov/) | 0 linting errors and 0 warnings | Combination of manual review and the results from automated testing
   Accessible | Web Content Accessibility Guidelines 2.0 AA (WCAG 2.0 AA) standards | 0 errors reported for WCAG 2.0 AA standards using an automated scanner and 0 errors reported in manual testing | [HTML_CodeSniffer](http://squizlabs.github.io/HTML_CodeSniffer/) or [pa11y](https://github.com/pa11y/pa11y)
   Deployed | Code must successfully build and deploy into staging environment. | Successful build with a single command | Combination of manual review and automatic testing
   Documentation | [18F Code Review Guide](https://github.com/18F/development-guide/tree/master/code_review) | All code submitted at the conclusion of each sprint and at the final submission passes all checks in the “Reviewing Code” section | Combination of manual review and automatic testing, if available
   Secure | OWASP Application Security Verification Standard 3.0 | Code submitted must be free of medium- and high-level static and dynamic security vulnerabilities | Clean tests from a static testing SaaS (such as Gemnasium) and from OWASP ZAP, along with documentation explaining any false positives
