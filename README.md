# GitHub force push diff

Simple webhook to create comments to force push diffs.

Reasoning
---------
On bigger PRs where a reviewer goes through individual commits, it can be
distracting when there is a change made to an older commit. Changing an older
commit also rebases all following commits and all those are then shown on 
GitHub after the review. 

This webhook just makes it a lot easier for a reviewer to see what has been
changed in the force push. For instance if we had a typo in HEAD~5 the reviewer
would just be shown the diff of both end states and could avoid re-checking or
comparing the unmodified 4 commits.

Requirements
------------

- python 3
- virtual env
- visible server

Setup
-----

- Make sure you have a server visible from the web (if you're behind a firewall
  try using [ngrok](https://ngrok.com/).
- To run the server you must(should) setup env install requirements and run main
  ```
  virtualenv .venv
  . .venv/bin/activate
  pip install -r requirements.txt
  export GH_ACCESS_TOKEN="your_github_access_token"
  # Edit main.py and set the `REPO` where the hook shoud work
  python main.py
  ```
- Setup github webhook with:
  - Paload URL: `https://your.url_or.ip:1080/postreceive`
  - Content type: `application/json`
  - SSL verification: Disable



Note: the diff between two commits uses GitHub 
[two dot diff](https://github.blog/changelog/2018-09-18-two-dot-comparison/). 
