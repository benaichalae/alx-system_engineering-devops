Postmortem: Outage Incident on Alx School System

Issue Summary:

Duration: The outage occurred on February 17, 2024, starting at 20:07 Pacific Standard Time (PST) and lasted for approximately 3 hours until 23:07 PST.
Impact: The outage affected access to the Alx School System Engineering & DevOps project 0x19, causing the website to be completely unavailable. Users attempting to access the site experienced HTTP 500 Internal Server Errors, leading to a complete disruption of service. Approximately 90% of users were affected during the outage.

Timeline:

Detection: The issue was detected at 20:07 PST when users reported encountering HTTP 500 errors while attempting to access the website.
Investigation: The incident was initially investigated by the engineering team, who noticed a sudden increase in error rates through monitoring alerts.
Actions Taken: Engineers investigated the web server and application logs to identify the root cause of the issue. They suspected a potential misconfiguration or software bug causing the server errors.
Misleading Paths: Initially, the investigation focused on the web server configuration and network connectivity, which did not yield any conclusive results. There were assumptions about potential database issues causing the errors, leading to additional investigation in that area.
Escalation: As the issue persisted, the incident was escalated to senior engineering and DevOps team members for further analysis and resolution.
Resolution: The root cause of the issue was identified as a typo in the WordPress application code, specifically in the wp-settings.php file. A trailing 'p' was mistakenly added to the file extension 'php', causing the server to fail in serving the requested web page. The issue was resolved by correcting the typo in the code, restoring normal functionality to the website.

Root Cause and Resolution:

Root Cause: The root cause of the outage was a typographical error in the WordPress application code, leading to the incorrect file reference in wp-settings.php.
Resolution: The issue was fixed by manually correcting the typo in the code, removing the trailing 'p' from the file extension 'php' in the wp-settings.php file.

Corrective and Preventative Measures:

Improvements: To prevent similar outages in the future, the following measures can be implemented:
Implement rigorous testing procedures to catch code errors before deployment.
Introduce automated code review tools to identify potential code inconsistencies and typos.
Enhance monitoring and alerting systems to promptly detect and respond to similar incidents in real-time.
Tasks:
Conduct a thorough code review of all application files to identify and rectify any potential typos or coding errors.
Implement automated testing pipelines to validate code changes and prevent deployment of erroneous code.
Enhance monitoring systems to provide detailed insights into application performance and error rates, enabling proactive incident response.

In conclusion, the outage on the Alx School System Engineering & DevOps project 0x19 was caused by a simple typographical error in the WordPress application code. The issue was promptly identified and resolved, and corrective measures have been outlined to prevent similar incidents in the future.
