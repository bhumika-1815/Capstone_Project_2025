# Project Notes

## Data Processing Steps

1. **COVID-19 Data Processing**
   - Load case rate data by modified ZCTA
   - Filter for December 1, 2020 to April 30, 2021 period
   - Calculate total case rates for each ZCTA
   - Separate borough-level and ZCTA-level data

2. **Demographic Data Integration**
   - Load population density and income data
   - Clean ZCTA codes (remove 'ZCTA5 ' prefix)
   - Filter demographic data to match ZCTAs in case rate data
   - Merge case rates with demographic information

3. **Output Generation**
   - Generate processed datasets for analysis
   - Create visualizations (PDF outputs)
   - Organize outputs by type (figures vs. tables)

## Key Variables

- **ZCTA**: ZIP Code Tabulation Area (5-digit codes)
- **Total_Case_Rate**: Sum of case rates over the analysis period
- **Population Density**: Population per square mile
- **Median Income**: Median household income by ZCTA
- **Racial Composition**: Non-Hispanic White population percentage

## Analysis Period

- **Start Date**: December 1, 2020
- **End Date**: April 30, 2021
- **Rationale**: Covers a significant period of the COVID-19 pandemic in NYC

## Data Sources

- NYC Department of Health COVID-19 data
- US Census demographic data
- NYC geographic reference data
