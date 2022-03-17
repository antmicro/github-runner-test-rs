import google.auth, json
from google.auth.transport.requests import AuthorizedSession

def main():
    credentials, _ = google.auth.default()
    authed_session = AuthorizedSession(credentials)
    URL = f"https://compute.googleapis.com/compute/v1/projects/github-runner-test/zones/europe-west4-a/instances/gh-actions-runner-newflow-3-auto-spawned0"
    r = authed_session.get(URL)
    result = json.loads(r.text)
    print(f"0 -> {result}")
    URL = f"https://compute.googleapis.com/compute/v1/projects/github-runner-test/zones/europe-west4-a/instances/gh-actions-runner-newflow-3-auto-spawned1"
    r = authed_session.get(URL)
    result = json.loads(r.text)
    print(f"1 -> {result}")

if __name__ == '__main__':
    main()

