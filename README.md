# python-devops-learning

## terraform-learning

- Configured Terraform for AWS, managing cloud resources with customized attributes.
- Explored providers, resources, variables, and conditional expressions for nuanced infrastructure setups. Also, implemented S3 backend for remote state storage.
- Created reusable infrastructure using Terraform modules.
- Manage environments with Terraform workspaces.
- Integrated Terraform with HashiCorp Vault for secure secret management.

Find the implementation here: https://github.com/sasagarw/terraform-learning

## ebs-snapshots-stale.py

Used in Identifying Stale EBS Snapshots

In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

### Description:

The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.

## github-jira-integration.py

This aims to automate the process of creation of Jira tickets directly from GitHub comments using python script.

### Description:

Currently, the manual and time-intensive process of generating Jira tickets necessitates developers to log in to the Jira dashboard, manually input all required details, and create a new ticket. To streamline this process, we aim to develop a Python application that establishes a seamless connection between GitHub and Jira.

By implementing a Python app and configuring a webhook in a GitHub repository, we can automate the creation of Jira tickets. When a developer comments "/jira", the Python app is triggered, initiating the generation of a corresponding ticket in Jira.

For this initiative, we will leverage the Flask framework to construct the Python app. Additionally, we will employ API calls to interact with the Jira API, enabling the automated creation of tickets based on information extracted from GitHub issue comments. The python app will run on AWS EC2 instance which the instance IP connected to internet gateway for public access so that github can call this application when triggered using "/jira".
