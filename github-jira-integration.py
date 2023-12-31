import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():

  url = "https://sashank058.atlassian.net/rest/api/3/issue"

  API_TOKEN="<PUT_YOUR_API_TOKEN_HERE>"

  auth = HTTPBasicAuth("<YOUR_JIRA_EMAIL_ID_HERE>", API_TOKEN)

  headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
  }

  payload = json.dumps({
      "fields": {
      "description": {
          "content": [
              {
                  "content": [
                      {
                          "text": "My first Jira ticket.",
                          "type": "text"
                      }
                  ],
                  "type": "paragraph"
                  }
              ],
          "type": "doc",
           "version": 1
      },
      "project": {
         "key": "SA"
      },
      "issuetype": {
          "id": "10006"
      },
      "summary": "Main order flow broken",
  },
  "update": {}
  })

  webhook = requests.json
  response = None
  
  if webhook['comment'].get('body') == "/jira":
    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
    )
  else:
    print('Jira issue will be created if comment include /jira')

  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
