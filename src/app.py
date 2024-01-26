import json
import os

# Path to the appsettings.json file
appsettings_path = "./src/appsettings.json"

# Path to the .env file
env_path = "./src/.env"

# Read the appsettings.json file
with open(appsettings_path, "r") as file:
    appsettings = json.load(file)

# Extract the values and write them to the .env file
with open(env_path, "w") as file:
    for setting in appsettings:
        name = setting["name"]
        value = setting["value"]
        file.write(f"{name}={value}\n")
