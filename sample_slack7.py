Experiment — Jenkins Slack Notification Integration

Aim:
Integrate Slack with Jenkins and receive build notifications in Slack channel.

--------------------------------------------------

Step 1 — Install Slack

1. Open browser
2. Download Slack for Windows:
   https://slack.com/intl/en-in/downloads/windows

3. Install Slack
4. Login to Slack
5. Join workspace:
   VVCE

--------------------------------------------------

Step 2 — Create Slack Channel

1. Open Slack
2. Under Channels click:
   +

3. Click:
   Create a channel

4. Channel name:
   devops-group-channel

5. Set channel as:
   Public

6. Click:
   Create

--------------------------------------------------

Step 3 — Install Slack Plugin in Jenkins

1. Open Jenkins:
   http://localhost:8080

2. Go to:
   Manage Jenkins

3. Click:
   Plugins

4. Update plugins if required

5. Search:
   Slack Notification

6. Install plugin:
   Slack Notification Plugin

7. Restart Jenkins if asked

--------------------------------------------------

Step 4 — Configure Slack in Jenkins

1. Go to:
   Manage Jenkins → System

2. Scroll down to:
   Slack

--------------------------------------------------

Step 5 — Find Slack Workspace Name

1. Open Slack
2. Click workspace name at top-left

Example:
   vvcegroup.slack.com

3. Copy only:
   vvcegroup

NOT:
   https://vvcegroup.slack.com

NOT full URL

--------------------------------------------------

Step 6 — Add Jenkins Integration in Slack

Open browser:

https://my.slack.com/services/new/jenkins-ci

1. Select workspace
2. Select channel:
   #devops-group-channel

3. Click:
   Add Jenkins CI Integration

--------------------------------------------------

Step 7 — Copy Integration Token

After integration is created:

1. Scroll down
2. Find:
   Integration Token Credential ID

3. Copy token

Example:
   NmP5CkducmOmFPQcCyHJe6U7

--------------------------------------------------

Step 8 — Add Credentials in Jenkins

1. Go to:
   Manage Jenkins → Credentials

2. Click:
   Global

3. Click:
   Add Credentials

4. Set:

   Kind:
   Secret text

   Secret:
   Paste copied Slack token

   ID:
   slack-token

   Description:
   slack-token

5. Click:
   Create

--------------------------------------------------

Step 9 — Configure Slack Section in Jenkins

Go again to:

Manage Jenkins → System → Slack

Fill details:

Workspace:
vvcegroup

Credential:
slack-token

Default channel:
#devops-group-channel

--------------------------------------------------

Step 10 — Test Slack Connection

Click:
Test Connection

If successful:
Success

Message will appear in Slack channel.

--------------------------------------------------

Step 11 — Create Jenkins Freestyle Project

1. Click:
   New Item

2. Project name:
   devops-ia

3. Select:
   Freestyle Project

4. Click:
   OK

--------------------------------------------------

Step 12 — Add Build Step

1. Scroll to:
   Build Steps

2. Click:
   Add build step

3. Select:
   Execute Windows Batch Command

4. Add command:

java --version

OR

echo Hello Jenkins

--------------------------------------------------

Step 13 — Configure Slack Notifications

1. Scroll to:
   Post-build Actions

2. Click:
   Add post-build action

3. Select:
   Slack Notifications

4. Enable:

✔ Notify Build Start

✔ Notify Success

✔ Notify Every Failure

--------------------------------------------------

Step 14 — Save and Build

1. Click:
   Save

2. Click:
   Build Now

--------------------------------------------------

Step 15 — Verify Slack Notification

Open Slack channel:

#devops-group-channel

You should see messages like:

devops-ia - #1 Started

devops-ia - #1 Success

--------------------------------------------------

Important Notes

1. Workspace should only be:
   vvcegroup

NOT:
   https://vvcegroup.slack.com

2. Never paste commands inside Slack token field.

Wrong:
https://vvcegroup.slack.com/services/hooks/jenkins-ci?token=pip install flask

Correct:
Only token text

3. Channel name must start with:
   #

Example:
#devops-group-channel

--------------------------------------------------

Output:

Slack notification received successfully from Jenkins build.