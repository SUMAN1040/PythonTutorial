# Write a program to generate multiplication tables for numbers from 2 to 20 and write it to different files; Place these files in a folder for a 13 years old

def generate_multiplication_tables(number):
    table = ""

    for i in range(1, 11):
        table += f"{number} x {i} = {number * i}\n"

    with open(f"tables/table_{number}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generate_multiplication_tables(i)