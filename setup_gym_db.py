import sqlite3
import pandas as pd
import os

# STEP 1: Setup file paths and table name

# Path to the SQLite database file (will be created if it doesn't exist)
db_file_name = 'data/processed/gym_data.db'

# Path to the raw CSV data
csv_file_path = 'data/raw/gym_members_exercise_tracking.csv'

# Table name to be created in the database
table_name = 'gym_members'

# STEP 2: Validate CSV file path
# If the CSV file doesn't exist, exit the program with an error message
if not os.path.exists(csv_file_path):
    print(f"Error: The CSV file '{csv_file_path}' was not found.")
    exit()

# STEP 3: Start SQLite operations (connect and initialize)
try:
    # Establish connection to the database
    conn = sqlite3.connect(db_file_name)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    print(f"Successfully connected to SQLite database: {db_file_name}")

    # STEP 4: Create table if it doesn't exist
    # Define table schema and data types for each column
    # Double quotes around column names are used to support spaces and special characters
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS "{table_name}" (
        Age INTEGER,
        Gender TEXT,
        "Weight (kg)" REAL,
        "Height (cm)" REAL,
        Max_BPM INTEGER,
        Avg_BPM REAL,
        Resting_BPM INTEGER,
        "Session_Duration (hours)" REAL,
        Calories_burned REAL,
        Workout_Type TEXT,
        Fat_Percentage REAL,
        "Water_Intake (liters)" REAL,
        "Workout_Frequency (days/week)" INTEGER,
        Experience_Level INTEGER,
        BMI REAL
    );
    """

    # Execute the SQL query to create the table
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Table '{table_name}' has been created successfully.")

    # STEP 5: Load CSV into DataFrame
    try:
        # Read CSV into a pandas DataFrame
        df = pd.read_csv(csv_file_path)
        print(f"Successfully loaded data from '{csv_file_path}' into pandas DataFrame.")

        # Display first 5 rows of the DataFrame
        print("DataFrame head (first 5 rows):")
        print(df.head())

        # Display DataFrame metadata (columns, types, non-null counts)
        print("\nDataFrame info (data types and non-nulls):")
        df.info()

        # STEP 6: Import DataFrame into SQLite table
        # 'if_exists="replace"' ensures any existing table data is cleared
        # 'index=False' prevents pandas from writing the DataFrame index as a column
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.commit()
        print(f"\nData from '{csv_file_path}' successfully imported into '{table_name}' table.")

    # STEP 7: Handle CSV loading-related errors
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file '{csv_file_path}' is empty.")
        conn.rollback()  # Roll back table creation if data is invalid
    except FileNotFoundError:
        print(f"Error: The CSV file '{csv_file_path}' was not found.")
        conn.close()
        exit()
    except Exception as e:
        print(f"Unexpected error while loading CSV: {e}")
        conn.close()
        exit()

    # STEP 8: Verify data insertion by selecting first 5 rows from the table
    try:
        select_query = f"""SELECT * FROM "{table_name}" LIMIT 5;"""
        cursor.execute(select_query)

        # Fetch all returned rows
        rows = cursor.fetchall()

        if rows:
            # Get column names from cursor metadata
            column_names = [description[0] for description in cursor.description]
            print("\nColumn names:")
            print(column_names)

            print("\nSample rows:")
            for row in rows:
                print(row)
        else:
            print("No data found in the table. Data import might have failed.")

    except sqlite3.Error as e:
        print(f"Error executing verification query: {e}")

# Handle SQLite connection or query execution errors
except sqlite3.Error as e:
    print(f"A database error occurred: {e}")
# Handle any unexpected errors during the main DB operations
except Exception as e:
    print(f"An unexpected error occurred during database operations: {e}")

# STEP 9: Always close the database connection
finally:
    if conn:  # Only close if connection was established
        conn.close()
        print("\nDatabase connection closed.")
    else:
        print("\nNo database connection was established to close.")

print(f"\nProcess completed. Your SQLite database file is located at: {db_file_name}")
