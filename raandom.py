import csv
import random
import faker

# Create a Faker instance
fake = faker.Faker()

# Define the headers
headers = ['Name', 'Age', 'City', 'Country', 'Salary']

# Open the file in write mode
with open('random_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    # Write the headers
    writer.writeheader()

    # Generate 100 rows of random data
    for _ in range(100):
        writer.writerow({
            'Name': fake.name(),
            'Age': random.randint(20, 60),
            'City': fake.city(),
            'Country': fake.country(),
            'Salary': random.randint(30000, 80000)
        })