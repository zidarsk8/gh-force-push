import os

import github_webhook
import flask
import github

ACCESS_TOKEN = os.environ.get("GH_ACCESS_TOKEN")
REPO = "zidarsk8/zengrc"
COMMENT_TEMPLATE = """
The force push was created with the same base commit and the
following changes have been made

[{before}..{after} diff](https://github.com/{repo}/compare/{before}..{after})

""".strip()


app = flask.Flask(__name__)  # Standard Flask app
webhook = github_webhook.Webhook(app)  # Defines '/postreceive' endpoint


@app.route("/")  # Standard Flask endpoint
def hello_world():
    return "Hello, World!"


@webhook.hook()
def on_push(data):
    branch_name = data["ref"].split("/")[-1]
    if not data["forced"]:
        return
    g = github.Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO)
    pulls = repo.get_pulls(head="test-commit")
    for pull in pulls:
        issue = repo.get_issue(pull.number)
        issue.create_comment(
            COMMENT_TEMPLATE.format(
                repo=REPO, before=data["before"][:10], after=data["after"][:10]
            )
        )
        pass


if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=1080, debug=True)
