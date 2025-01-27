# Project: Web Scraping and Visualization of Centers in Poland

## Introduction
This project combines web scraping with data visualization to analyze the distribution of therapeutic centers in Poland. These centers specialize in providing auditory integration therapy and related services, supporting individuals with various auditory and developmental challenges. By extracting data from a publicly available website and visualizing it using Tableau, the project aims to offer valuable insights into the geographic spread of these facilities.

## Background
Auditory integration therapy centers play a crucial role in supporting individuals, especially children, with conditions like auditory processing disorders, autism, and other developmental challenges. Understanding the availability and distribution of these centers can assist families, healthcare professionals, and policymakers in identifying service gaps and optimizing resource allocation. This project was motivated by the need to make such information more accessible and visually engaging.

The data for this analysis was collected from the website [https://johansen-ias.pl/terapeuci/](https://johansen-ias.pl/terapeuci/), which lists therapeutic centers across Poland.

## Tools I Used
The project utilized the following tools and technologies:
- **Python**:
  - **Requests**: To fetch the website's HTML content.
  - **BeautifulSoup (bs4)**: For parsing and extracting relevant data from the HTML.
  - **Regular Expressions (re)**: To identify contact details, such as phone numbers, for counting centers.
  - **CSV module**: For exporting the cleaned data into a structured file format.
- **Tableau**: To visualize the processed data and create an interactive dashboard accessible to a broad audience.

## The Analysis
1. **Web Scraping**:
   - The script retrieves the HTML content of the target webpage and parses it using BeautifulSoup.
   - Identifies city names and associated therapists by processing the structure of the webpage (e.g., elements like `.elementor-tab-title` and `.elementor-tab-content`).
   - Uses regular expressions to count therapeutic centers based on recognizable patterns, such as phone numbers.

2. **Data Storage**:
   - The scraped data, including city names and the number of associated centers, is exported to a CSV file named `city_centers.csv`.

3. **Data Visualization**:
   - The CSV file is imported into Tableau.
   - An interactive dashboard is created to display the distribution of centers across Poland. Users can view the data geographically and explore city-specific details.
   - The dashboard is available at [Tableau Dashboard](https://public.tableau.com/app/profile/filip.cieciuch/viz/OrodkiwPolsce/Dashboard1), and [here](/Dashboard.png)

## What I Learned
Through this project, I gained insights into:
- The structure and dynamics of web scraping, including handling real-world HTML inconsistencies.
- The power of regular expressions for extracting specific patterns from unstructured text.
- The effectiveness of Tableau in transforming raw data into a user-friendly and interactive visual format.
- The practical challenges of integrating data scraping and visualization workflows.

## Conclusions
This project highlights the potential of combining web scraping with data visualization to address real-world needs. By making information about therapeutic centers more accessible and visually intuitive, the project can support:
- Families seeking nearby therapy options for their children.
- Policymakers and organizations planning resource distribution.
- Researchers analyzing trends in healthcare and therapeutic services.

The resulting Tableau dashboard serves as a tool for understanding and improving the availability of these critical services in Poland.

## Future Directions
- Expand the dataset to include additional details, such as services offered or staff qualifications.
- Automate the entire workflow to ensure regular updates to the Tableau dashboard.
- Incorporate machine learning to predict areas with unmet demand for new centers.
