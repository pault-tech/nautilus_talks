# nautilus_talks
A copy of Brad's pair trading strategy demo from YouTube

This is being kept up-to-date with the current Nautilus branch.

Note1: I had to mess around with the Poetry installation order by deleting the shipped lock file
and commenting out Nautilus in the .toml in order to get "poetry install" to work.

Note2: After downloading and poetry installing this repo, you will need to open a console shell
and navigate to ..\nautilus_talks\20220617 and execute the following command to unpack needed data files:
"poetry run inv extract-catalog"

This will first require you to have pipx or pip installed py package "invoke", e.g.
"pipx install invoke"
