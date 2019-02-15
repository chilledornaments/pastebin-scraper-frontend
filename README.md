# pastebin-scraper-frontend

## Overview

This is the frontend to [this](https://github.com/mitchya1/PasteBin_SecurityScraper) tool.

The PasteBin_SecurityScraper iterates through the latest 249 (or whatever you configure) pastes on Pastebin and searches for strings. If it finds a match, the full paste, keyword, and URL of the paste are added to MongoDB (assuming you enable that feature).

The frontend provides a means to view and categorize (false alarm, match, unclassified) the responses from the scraper.

## Setup

- Clone the repo
    - The files in `app_files/` assume you've cloned the repo to `/opt/`

- Move `config.example.py` to `config.py`

- Fill in your MongoDB settings. These should match the credentials you're using for PasteBin_SecurityScraper
    - The user needs to be able to modify the documents in the collection

- Add a user for gunicorn to run as
    - `app_files/pbfe.service` assume the user is named `pbscrape`

- Move `app_files/pbfe.service` to `/etc/systemd/system/`

- Run `sudo systemctl daemon-reload`

- You can now run the application

*Optional*

There's an example NGINX config (`app_files/pbfe.service`) if you'd like to reverse proxy the Flask app.

