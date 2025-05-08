import csv
import os
from datetime import datetime
import pandas as pd

# Default data with last updated dates (hardcoded for fallback)
ibm_data = {
    'Below 25% Mn': {'asp': 8252, 'date': 'March 2025'},
    '25% to below 35% Mn': {'asp': 10731, 'date': 'March 2025'},
    '35% to below 46% Mn': {'asp': 20255, 'date': 'March 2025'},
    '46% and above Mn': {'asp': 32965, 'date': 'March 2025'},
    'Dioxide Ore': {'asp': 21766, 'date': 'March 2025'}
}

transport_costs = {
    'rail': (800, 1000),
    'road': (2000, 2500),
    'water': (450, 550),
    'slurry': (80, 100)
}

EXPORT_PATH = r"D:\\Google Drive\\Sheetal Holding\\Current Stuff\\mn_ore_price_summary.xlsx"

def get_user_input_indian():
    print("Select Manganese Ore Grade:")
    for i, grade in enumerate(ibm_data.keys(), 1):
        data = ibm_data[grade]
        print(f"{i}. {grade} (IBM ASP: ₹{data['asp']} as of {data['date']})")

    grade_choice = int(input("Enter choice number: "))
    grade = list(ibm_data.keys())[grade_choice - 1]

    print("\nIBM ASP value is taken from: IBM Monthly Price Report")
    premium_pct = float(input("Enter Market premium % [Default: 15]: ") or 15)

    use_moil = input("Show MOIL price adjustment for reference? (y/n): ").strip().lower() == 'y'
    moil_base = None
    moil_change_pct = 0

    if use_moil:
        moil_base = input("Enter MOIL base price (leave blank if unknown): ")
        moil_base = float(moil_base) if moil_base else None
        moil_change_pct = float(input("MOIL price % increase/decrease (e.g., 35 or -5): ") or 0)

    distance = float(input("Enter transport distance in km [Default: 500]: ") or 500)
    print("Modes available: rail, road, water, slurry")
    mode = input("Select mode of transport [Default: road]: ") or 'road'

    return grade, premium_pct, use_moil, moil_base, moil_change_pct, distance, mode.lower()

def get_user_input_foreign():
    country = input("Enter country of origin: ")
    currency = input("Enter currency (INR/USD) [Default: INR]: ").strip().upper() or 'INR'
    exchange_rate = 1

    if currency == 'USD':
        exchange_rate = float(input("Enter current USD to INR exchange rate [e.g., 83.2]: ") or 83.2)

    print("Select Manganese Ore Grade:")
    for i, grade in enumerate(ibm_data.keys(), 1):
        print(f"{i}. {grade}")
    grade_choice = int(input("Enter choice number: "))
    grade = list(ibm_data.keys())[grade_choice - 1]

    base_price = float(input(f"Enter CIF base price ({currency}/ton): ")) * exchange_rate
    customs = float(input(f"Enter customs duty or taxes ({currency}/ton): ") or 0) * exchange_rate
    port_handling = float(input(f"Enter port/handling charges ({currency}/ton): ") or 0) * exchange_rate
    inland_logistics = float(input(f"Enter inland logistics ({currency}/ton): ") or 0) * exchange_rate
    misc_costs = float(input(f"Enter any other cost ({currency}/ton): ") or 0) * exchange_rate

    return country, base_price, customs, port_handling, inland_logistics, misc_costs, grade

def calculate_price_indian(grade, premium_pct, use_moil, moil_base, moil_change_pct, distance, mode):
    ibm_price = ibm_data[grade]['asp']
    ibm_date = ibm_data[grade]['date']

    final_price = ibm_price * (1 + premium_pct / 100)
    explanation = [
        f"IBM ASP for {grade}: ₹{ibm_price} (as of {ibm_date})",
        f"+ {premium_pct}% Market Premium => ₹{final_price:.2f}"
    ]

    if use_moil:
        if moil_base is not None:
            moil_adjusted = moil_base * (1 + moil_change_pct / 100)
            explanation.append(f"MOIL Reference: Base ₹{moil_base}, Change {moil_change_pct}% => ₹{moil_adjusted:.2f}")
        else:
            explanation.append("MOIL base price not provided, skipping MOIL reference.")

    if mode not in transport_costs:
        raise ValueError("Invalid transport mode selected.")

    per_250_range = transport_costs[mode]
    multiplier = distance / 250
    low_cost = per_250_range[0] * multiplier
    high_cost = per_250_range[1] * multiplier

    explanation.append(f"\nTransport: {mode.title()} mode for {distance} km")
    explanation.append(f"Estimated cost: ₹{low_cost:.2f} - ₹{high_cost:.2f} per ton (excluding taxes/border costs)")

    total_low = final_price + low_cost
    total_high = final_price + high_cost

    explanation.append(f"\nEstimated Total Delivered Price: ₹{total_low:.2f} - ₹{total_high:.2f} per ton")
    return explanation, {
        'Date': datetime.today().strftime('%Y-%m-%d'),
        'Ore Grade': grade,
        'IBM ASP (₹/ton)': ibm_price,
        'IBM Date': ibm_date,
        'Market Premium (%)': premium_pct,
        'MOIL Applied': use_moil,
        'MOIL Base Price': moil_base,
        'MOIL Change (%)': moil_change_pct,
        'Distance (km)': distance,
        'Transport Mode': mode,
        'Transport Cost Low (₹/ton)': low_cost,
        'Transport Cost High (₹/ton)': high_cost,
        'Final Price Low (₹/ton)': total_low,
        'Final Price High (₹/ton)': total_high
    }

def calculate_price_foreign(country, base_price, customs, port_handling, inland_logistics, misc_costs, grade):
    total_cost = base_price + customs + port_handling + inland_logistics + misc_costs
    ibm_price = ibm_data[grade]['asp']

    result = {
        'Date': datetime.today().strftime('%Y-%m-%d'),
        'Country of Origin': country,
        'Ore Grade': grade,
        'IBM ASP (₹/ton)': ibm_price,
        'CIF Base Price (₹/ton)': base_price,
        'Customs (₹/ton)': customs,
        'Port Handling (₹/ton)': port_handling,
        'Inland Logistics (₹/ton)': inland_logistics,
        'Misc Costs (₹/ton)': misc_costs,
        'Total Landed Cost (₹/ton)': total_cost,
        'Profit or Loss (₹/ton)': round(ibm_price - total_cost, 2)
    }

    explanation = [
        f"Imported from {country} with total landed cost: ₹{total_cost:.2f}/ton",
        f"IBM ASP for {grade}: ₹{ibm_price:.2f}/ton",
        f"→ {'Profit' if result['Profit or Loss (₹/ton)'] >= 0 else 'Loss'} of ₹{abs(result['Profit or Loss (₹/ton)']):.2f}/ton compared to IBM ASP for the grade."
    ]
    return explanation, result

def export_to_excel(data_dict, filepath=EXPORT_PATH):
    df_new = pd.DataFrame([data_dict])
    if os.path.exists(filepath):
        df_old = pd.read_excel(filepath)
        df_combined = pd.concat([df_new, df_old], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_excel(filepath, index=False)
    print(f"\nExported summary to {filepath}")

def main():
    print("\nManganese Ore Calculator\n")
    print("1. Indian Origin")
    print("2. Foreign Origin")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        grade, premium_pct, use_moil, moil_base, moil_change_pct, distance, mode = get_user_input_indian()
        explanation, summary_data = calculate_price_indian(grade, premium_pct, use_moil, moil_base, moil_change_pct, distance, mode)

    elif choice == '2':
        country, base_price, customs, port_handling, inland_logistics, misc_costs, grade = get_user_input_foreign()
        explanation, summary_data = calculate_price_foreign(country, base_price, customs, port_handling, inland_logistics, misc_costs, grade)

    else:
        print("Invalid choice. Please restart.")
        return

    print("\n--- Summary ---")
    for line in explanation:
        print(line)
    print("\nNote: Prices exclude border/tax/custom clearance and are for indicative purposes only.")

    export_choice = input("\nDo you want to export this summary to Excel? (y/n): ").strip().lower()
    if export_choice == 'y':
        export_to_excel(summary_data)

if __name__ == "__main__":
    main()
