# Life Expectancy Analyzer
# Creative Extension: Added country-based analysis where users can enter a country name to see its min, max, and average life expectancy.

filename = "life-expectancy.csv"

# Overall min/max trackers
overall_min = float('inf')
overall_max = float('-inf')
min_country = ""
min_year = ""
max_country = ""
max_year = ""

# Load data
data = []
with open(filename) as file:
    next(file)  # Skip header
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        year = int(parts[2])
        life_exp = float(parts[3])
        data.append((country, year, life_exp))

        # Track overall min/max
        if life_exp < overall_min:
            overall_min = life_exp
            min_country = country
            min_year = year
        if life_exp > overall_max:
            overall_max = life_exp
            max_country = country
            max_year = year

# Display overall results
print(f"\nThe overall max life expectancy is: {overall_max:.3f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min:.2f} from {min_country} in {min_year}")

# Year-specific analysis
year_of_interest = int(input("\nEnter the year of interest: "))
year_data = [entry for entry in data if entry[1] == year_of_interest]

if year_data:
    total = sum(entry[2] for entry in year_data)
    avg = total / len(year_data)
    max_entry = max(year_data, key=lambda x: x[2])
    min_entry = min(year_data, key=lambda x: x[2])

    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg:.2f}")
    print(f"The max life expectancy was in {max_entry[0]} with {max_entry[2]:.2f}")
    print(f"The min life expectancy was in {min_entry[0]} with {min_entry[2]:.3f}")
else:
    print("No data found for that year.")

# Country-specific analysis (Creative Feature)
country_of_interest = input("\nEnter a country to analyze: ").strip()
country_data = [entry for entry in data if entry[0].lower() == country_of_interest.lower()]

if country_data:
    total = sum(entry[2] for entry in country_data)
    avg = total / len(country_data)
    max_entry = max(country_data, key=lambda x: x[2])
    min_entry = min(country_data, key=lambda x: x[2])

    print(f"\nFor {country_of_interest.title()}:")
    print(f"The average life expectancy was {avg:.2f}")
    print(f"The max life expectancy was {max_entry[2]:.2f} in {max_entry[1]}")
    print(f"The min life expectancy was {min_entry[2]:.2f} in {min_entry[1]}")
else:
    print("No data found for that country.")