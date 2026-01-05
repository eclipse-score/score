# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

#!/usr/bin/env python3

import os
import json
import requests
import sys
from dotenv import load_dotenv


def set_output(name, value):
    print(f"::set-output name={name}::{value}")

def set_failed(message):
    print(f"::error::{message}")
    sys.exit(1)

def main():
    linked_issue_numbers_str = os.environ.get('LINKED_ISSUES')
    github_token = os.environ.get('GITHUB_TOKEN')
    repo_owner = os.environ.get('GITHUB_REPOSITORY_OWNER')
    repo_name = os.environ.get('GITHUB_REPOSITORY').split('/')[-1]

    if not github_token:
        set_failed("GITHUB_TOKEN is not set. Ensure it's passed as an environment variable.")

    if not linked_issue_numbers_str:
        print("No issues linked in the PR description. Skipping type check.")
        set_output('found_bug_issue', 'false')
        set_output('found_feature_issue', 'false')
        set_output('found_task_issue', 'false')
        set_output('other_issue_types', '[]')
        return

    try:
        linked_issue_numbers = json.loads(linked_issue_numbers_str)
    except json.JSONDecodeError:
        set_failed(f"Failed to parse LINKED_ISSUES: {linked_issue_numbers_str}. Ensure it's valid JSON.")

    print(f"Linked issue numbers: {linked_issue_numbers}")

    found_bug_issue = False
    found_feature_issue = False
    found_task_issue = False
    other_issue_types = []

    graphql_url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Content-Type": "application/json"
    }

    for issue_number in linked_issue_numbers:
        try:
            query = """
                query GetIssueType($owner: String!, $repo: String!, $issueNumber: Int!) {
                  repository(owner: $owner, name: $repo) {
                    issue(number: $issueNumber) {
                      id
                      title
                      issueType {
                        name
                      }
                    }
                  }
                }
            """

            variables = {
                "owner": repo_owner,
                "repo": repo_name,
                "issueNumber": issue_number,
            }

            response = requests.post(graphql_url, headers=headers, json={'query': query, 'variables': variables})
            response.raise_for_status()
            result = response.json()

            if 'errors' in result:
                set_failed(f"GraphQL errors for issue #{issue_number}: {result['errors']}")

            issue_data = result.get('data', {}).get('repository', {}).get('issue')

            if not issue_data:
                print(f"Warning: Issue #{issue_number} not found in this repository or no data returned.")
                other_issue_types.append({'number': issue_number, 'type': 'Issue Not Found'})
                continue

            issue_type_name = issue_data.get('issueType', {}).get('name')

            if issue_type_name:
                type_value = issue_type_name
                print(f"Issue #{issue_number} has Built-in Issue Type: {type_value}")

                if type_value == 'Bug':
                    found_bug_issue = True
                elif type_value == 'Feature':
                    found_feature_issue = True
                elif type_value == 'Task':
                    found_task_issue = True
                else:
                    other_issue_types.append({'number': issue_number, 'type': type_value})
            else:
                print(f"Issue #{issue_number} has no built-in 'issueType' specified.")
                other_issue_types.append({'number': issue_number, 'type': 'No Built-in Issue Type'})

        except requests.exceptions.RequestException as e:
            set_failed(f"HTTP error fetching issue #{issue_number} type: {e}")
        except Exception as e:
            set_failed(f"An unexpected error occurred for issue #{issue_number}: {e}")

    set_output('found_bug_issue', str(found_bug_issue).lower())

if __name__ == "__main__":
    main()
