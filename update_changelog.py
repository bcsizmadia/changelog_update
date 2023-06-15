from github import Github
import os
import json
import sys

github_event_path = os.environ.get("GITHUB_EVENT_PATH")
with open(github_event_path, "r") as f:
    payload = json.load(f)
release = payload["release"]

g = Github(os.environ.get("INPUT_TOKEN"))

repo = g.get_repo(os.environ.get("GITHUB_REPOSITORY"))
new_version = release["tag_name"]
changes = release["body"]

contents = repo.get_contents("CHANGELOG.md")
changelog = contents.decoded_content.decode()

changelog = changelog + f"\n\n## {new_version}\n\n{changes}"
commit_message = (
    os.environ.get("INPUT_COMMIT_MESSAGE")
    or f"docs(changelog): update for version {new_version}"
)

repo.update_file(contents.path, commit_message, changelog, contents.sha)
