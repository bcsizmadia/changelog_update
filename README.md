# Changelog Update Action 🎉

- [Changelog Update Action 🎉](#changelog-update-action-)
  - [What does it do? 🐍](#what-does-it-do-)
  - [Usage 📦](#usage-)
  - [Inputs 🛠️](#inputs-️)

This GitHub Action automatically updates the `CHANGELOG.md` file in your repository whenever a new release is published.

## What does it do? 🐍

1. It checks out your code.
2. Sets up Python 3.x.
3. Installs the necessary Python dependencies.
4. Runs a Python script that fetches the details of the newly published release and updates the `CHANGELOG.md` file accordingly.

## Usage 📦

Here are 2 examples of how to use this action:

```yaml
name: Update Changelog 🎉

on:
  release:
    types: [published]

jobs:
  update-changelog:
    runs-on: ubuntu-latest

    steps:
    - name: Changelog Update 📄
      uses: bcsizmadia/changelog_update@main
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        commit_message: "🎉 Update changelog for new release"
```

```yaml
name: Update Changelog 🎉

on:
  release:
    types: [published]

jobs:
  update-changelog:
    runs-on: ubuntu-latest

    steps:
    - name: Changelog Update 📄
      uses: bcsizmadia/changelog_update@main
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
```

## Inputs 🛠️

The action currently supports the following inputs:

`token` - **required** - [`scope: repo`] - Your GitHub token. This is used to authenticate the action and provide it with the necessary permissions to make changes to your repository.
  
`commit_message` - **optional** - Commit message for the update. If not provided, a default commit message will be used.