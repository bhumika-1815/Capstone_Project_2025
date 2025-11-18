"""
NYC COVID-19 Data Analysis
==========================

This script analyzes COVID-19 case rates across NYC ZCTAs and examines
their relationship with demographic and socioeconomic factors.

Author: Capstone Project
Date: 2024
"""

import pandas as pd
import os
from pathlib import Path

# Set up paths
project_root = Path(__file__).parent.parent
data_raw_dir = project_root / "data" / "raw"
data_processed_dir = project_root / "data" / "processed"
outputs_dir = project_root / "outputs"

# Ensure output directories exist
data_processed_dir.mkdir(parents=True, exist_ok=True)
outputs_dir.mkdir(parents=True, exist_ok=True)

def load_and_process_covid_data():
    """Load and process COVID-19 case rate data."""
    print("Loading COVID-19 data...")
    
    # Load the COVID-19 data
    file_path = data_raw_dir / "data-by-modzcta.csv"
    df = pd.read_csv(file_path)
    
    # Display basic info about the dataset
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst few rows:")
    print(df.head())
    
    # Convert week_ending to datetime format
    df["week_ending"] = pd.to_datetime(df["week_ending"])
    
    # Filter for the range: December 1, 2020 to April 30, 2021
    mask = (df["week_ending"] >= "2020-12-01") & (df["week_ending"] <= "2021-04-30")
    filtered_df = df.loc[mask]
    
    print(f"\nFiltered dataset shape: {filtered_df.shape}")
    
    return filtered_df

def calculate_case_rates(filtered_df):
    """Calculate total case rates for each ZCTA."""
    print("\nCalculating case rates...")
    
    # Sum case rates over time for each borough and ZCTA
    summed_case_rates = filtered_df.sum(numeric_only=True).to_frame(name="Total_Case_Rate")
    summed_case_rates.index.name = "Region"
    
    # Separate boroughs and ZCTAs
    borough_case_rates = summed_case_rates.loc[
        summed_case_rates.index.str.startswith("CASERATE_") &
        summed_case_rates.index.str.match(r"CASERATE_(BX|BK|MN|QN|SI)$")
    ]
    
    zcta_case_rates = summed_case_rates.loc[
        summed_case_rates.index.str.match(r"CASERATE_\d{5}$")
    ]
    
    # Rename borough index values for clarity
    borough_case_rates.index = borough_case_rates.index.str.replace("CASERATE_", "")
    borough_case_rates.index.name = "Borough"
    
    print(f"Found {len(zcta_case_rates)} ZCTAs and {len(borough_case_rates)} boroughs")
    print("\nZCTA case rates (first 10):")
    print(zcta_case_rates.head(10))
    
    # Process ZCTA data
    zcta_case_rates.reset_index(inplace=True)
    zcta_case_rates["ZCTA"] = zcta_case_rates["Region"].str.replace("CASERATE_", "")
    zcta_case_rates = zcta_case_rates[["ZCTA", "Total_Case_Rate"]]
    
    # Save processed data
    output_path = data_processed_dir / "zcta_case_rates_dec2020_apr2021.csv"
    zcta_case_rates.to_csv(output_path, index=False)
    print(f"\nSaved ZCTA case rates to: {output_path}")
    
    return zcta_case_rates, borough_case_rates

def process_demographic_data(case_rate_df):
    """Process demographic and socioeconomic data."""
    print("\nProcessing demographic data...")
    
    # Load demographic data
    income_file = data_raw_dir / "Population_den _edit.csv"
    income_df = pd.read_csv(income_file)
    
    print(f"Income data shape: {income_df.shape}")
    print(f"Income data columns: {list(income_df.columns)}")
    
    # Clean ZCTA codes (remove 'ZCTA5 ' if present)
    income_df['ZCTA'] = income_df['ZCTA'].astype(str).str.replace('ZCTA5 ', '')
    case_rate_df['ZCTA'] = case_rate_df['ZCTA'].astype(str)
    
    # Filter income_df to include only ZCTAs in the case_rate_df
    filtered_income_df = income_df[income_df['ZCTA'].isin(case_rate_df['ZCTA'])]
    
    # Save filtered income data
    income_output_path = data_processed_dir / "filtered_median_income_zctas.csv"
    filtered_income_df.to_csv(income_output_path, index=False)
    print(f"Saved filtered income data to: {income_output_path}")
    
    # Merge case rates with demographic data
    merged_df = pd.merge(case_rate_df, filtered_income_df, on='ZCTA', how='left')
    
    # Save merged data
    merged_output_path = data_processed_dir / "filtered_Pop_Den.csv"
    merged_df.to_csv(merged_output_path, index=False)
    print(f"Saved merged data to: {merged_output_path}")
    
    print(f"\nMerged dataset shape: {merged_df.shape}")
    print("\nMerged data preview:")
    print(merged_df.head())
    
    return merged_df

def main():
    """Main analysis function."""
    print("NYC COVID-19 Data Analysis")
    print("=" * 50)
    
    try:
        # Step 1: Load and process COVID-19 data
        filtered_df = load_and_process_covid_data()
        
        # Step 2: Calculate case rates
        zcta_case_rates, borough_case_rates = calculate_case_rates(filtered_df)
        
        # Step 3: Process demographic data
        merged_df = process_demographic_data(zcta_case_rates)
        
        print("\n" + "=" * 50)
        print("Analysis completed successfully!")
        print(f"Processed data saved to: {data_processed_dir}")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()