from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Load environment variables
load_dotenv()

# Set Kaggle credentials from .env
os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")
os.environ['KAGGLE_CONFIG_DIR'] = os.path.abspath('') 

# Authenticate Kaggle API
api = KaggleApi()
api.authenticate()

# Prepare data folder
os.makedirs('data/raw', exist_ok=True)

# Download dataset
dataset = 'leandrenash/enhanced-health-insurance-claims-dataset'
api.dataset_download_files(dataset, path='data/raw', unzip=True)

print("Dataset downloaded and extracted to 'data/raw' directory.")