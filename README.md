# WikiDataPull

## Wiki Bias Research: Deletion Candidates Data Collection

This repository is part of a research project investigating bias in Wikipedia's notability guidelines. The data collected comprises the names of academics whose Wikipedia articles were flagged for deletion.

In this repository, we provide the Python script `wikiprojscrapingcode.py`, which was used to scrape data from a specific Wikipedia page: [Wikipedia: WikiProject Deletion sorting/Academics and educators/archive_2](https://en.m.wikipedia.org/wiki/Wikipedia:WikiProject_Deletion_sorting/Academics_and_educators/archive_2). This page serves as an archive of academics and educators whose articles were flagged for deletion.

## Description of the Code

`wikiprojscrapingcode.py` is a web scraping tool that fetches, processes, and saves relevant details from the targeted Wikipedia page. The output is a .csv file named `wikicombo.csv`, which contains the academic names and their respective Wikipedia links.

## Repository Contents

This repository contains:

- The Python script `wikiprojscrapingcode.py`, used for data scraping.
- The raw output `wikicombo.csv` file, the exact data sheet used to generate our findings prior to any data cleaning.

It's noteworthy that the mentioned Wikipedia page continually updates with more "Articles for Deletion" (AfD) discussions over time. The .csv file represents a snapshot of the deletion discussions available from around the summer of 2020, dating back to sometime in 2017, as stated in our research paper. 


Please feel free to explore the code and the data output to better understand how the research project collected its data.
