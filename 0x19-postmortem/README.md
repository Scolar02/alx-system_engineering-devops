### Postmortem: Authentication Service Downtime
##### Issue Summary
The authentication service experienced complete downtime, affecting all user logins and API access, on July 10th at 08:00 to 11:30 (EAT) . This was due to excessive concurrent database connections due to a code bug causing resource exhaustion.
##### Timeline
08:00 (EAT) - The issue was detected. The support team detected escalating user complaints and support notifications about increased login failures.
08:10 (EAT) - Immediate investigation was launched, focusing on server health, load, and database performance.
08:30 (EAT) - The team was briefly led astray by network assumptions, triggering temporary network diagnostics that didn't address the core issue.
08:40 (EAT) - The development and Database teams were brought in to provide specialized insights.
09:30 (EAT) - The team discovered excessive concurrent database connections due to a code bug causing resource exhaustion.
10:00 (EAT) -  With a code fix and recalibration of database connection pooling, the issue was fixed.
##### Root Cause and Resolution
* Cause: An underlying code bug in the authentication service hindered proper closure of database connections, leading to a buildup of unclosed connections and resource exhaustion.
* Resolution: Identification and resolution of the code issue were carried out, followed by reconfiguration of connection pool settings to ensure timely connection releases.
##### Corrective and Preventative Measures:
Remediation: Strengthening code review procedures to encompass connection management, implementing circuit breakers, and instituting comprehensive monitoring.
Action Items:
+ Code Review Enhancement: Augment code review practices to include thorough assessment of connection closure and resource handling.
+ Circuit Breaker Implementation: Integration of circuit breakers to restrict connection accumulation during peak periods.
+ Enhanced Monitoring: Deployment of robust monitoring mechanisms for tracking database connections and resource utilization, with alerts triggered by abnormal patterns.
+ Documentation: Revise documentation to incorporate best practices for effective connection management.
##### Conclusion
In conclusion, this incident serves as a reminder of the indispensable role of stringent code evaluation and resource administration to circumvent issues arising from resource depletion. The thorough inquiry resulted in pinpointing the root cause, implementing a solution, and outlining strategies to forestall similar occurrences. The incident underscores the importance of maintaining code quality and effective monitoring to uphold the reliability and accessibility of critical services.
