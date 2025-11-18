# NYC COVID-19 Data Analysis Capstone Project

## Project Overview
This capstone project analyzes COVID-19 case rates across New York City ZIP Code Tabulation Areas (ZCTAs) and examines their relationship with demographic and socioeconomic factors such as population density, median income, and racial composition.

## Project Structure
```
Capstone_Project/
├── data/
│   ├── raw/                          # Original, unprocessed data
│   │   ├── data-by-modzcta.csv      # COVID-19 data by modified ZCTA
│   │   ├── Population_den _edit.csv # Population density data
│   │   └── NH White 2021.csv        # Non-Hispanic White population data
│   ├── processed/                    # Cleaned and processed data
│   │   ├── zcta_case_rates_dec2020_apr2021.csv
│   │   ├── filtered_median_income_zctas.csv
│   │   ├── filtered_NH_White.csv
│   │   └── filtered_Pop_Den.csv
│   └── external/                     # External reference data
│       └── nyc-zip-codes.csv        # NYC ZIP code to borough mapping
├── code/
│   └── data_analysis.py             # Main analysis script
├── outputs/
│   ├── figures/                     # Generated visualizations
│   │   ├── Caserate_2020-21.pdf
│   │   ├── Caserate_Current.pdf
│   │   ├── Hotspot_2020_2022.pdf
│   │   ├── Hotspot_Current.pdf
│   │   ├── Median_Income.pdf
│   │   ├── NH_White.pdf
│   │   └── Pop_Density.pdf
│   └── tables/                      # Generated data tables
├── documentation/                    # Additional documentation
└── README.md                        # This file
```

## Data Sources
- **COVID-19 Data**: NYC Department of Health case rates by modified ZCTA
- **Demographic Data**: Population density, median income, and racial composition by ZCTA
- **Geographic Data**: NYC ZIP code to borough mapping

## Analysis Period
- **Primary Analysis**: December 1, 2020 to April 30, 2021
- **Current Data**: Latest available data for comparison

## Key Findings
The analysis examines:
1. COVID-19 case rates across NYC ZCTAs during the specified period
2. Relationship between case rates and socioeconomic factors
3. Geographic patterns in COVID-19 impact
4. Demographic disparities in COVID-19 outcomes

## Usage
1. Run the main analysis script: `python code/data_analysis.py`
2. Review generated outputs in the `outputs/` directory
3. Examine processed data in `data/processed/`

## Requirements
- Python 3.x
- pandas
- Additional dependencies as needed for analysis

## Notes
- All file paths in the code have been updated to reflect the new directory structure
- Data processing steps are documented in the analysis script
- Generated outputs are organized by type (figures vs. tables)