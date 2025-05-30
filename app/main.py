from app.fetcher import fetch_jobs
import json

def main():
    try:
        data = fetch_jobs()
        print("Jobs fetched successfully:")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# This code serves as the entry point for the application.
# It imports the fetch_jobs function from the fetcher module and calls it,
# printing the fetched jobs or an error message if an exception occurs.