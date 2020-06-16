# Contributing to HTTP Emoji Codes

Contributing is simple! HTTP Emoji Codes is a static site generated by MkDocs & Material
for MkDocs. The status code pages are generated from the
`httpemojicodes/emojicodes.json` file.

## Setting Up Your Dev Environment

1. Fork & Clone the repository.
2. Set up [Poetry](https://python-poetry.org){target=_blank}
3. Install Python3.7 (we recommend using
   [pyenv](https://github.com/pyenv/pyenv){target=_blank})
4. Run `poetry install` in the project directory.

## Adding or Updating Emoji Codes

In order to make an update or add a new code, simply fork this repository, make your
update, and create PR.

If you're updating a description or adding a new code, we ask that you cite your source
for the new status code. An RFC or a source like
[MDN](https://developer.mozilla.org){target=_blank} is highly encouraged.

If you're updating an emoji code, we ask that you check the
[Twemoji DB](https://github.com/facelessuser/pymdown-extensions/blob/master/pymdownx/twemoji_db.py){target=_blank}
to ensure it's currently supported.

## Running a Build

1. Make sure you've completed all the steps in
   [Setting Up Your Dev Environment](#setting-up-your-dev-environment)
2. Run `mkdocs build`.
3. Preview the resulting output in the `site/` directory in your browser!