from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from config import Config

# Initialize MongoDB Client using configurations from config.py
client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

# Define your collection handles (MongoDB creates these automatically on first write)
users_col = db['users']
carbon_logs_col = db['carbon_logs']
ewaste_logs_col = db['ewaste_logs']

# ==========================================
# 1. USERS COLLECTION HANDLERS
# ==========================================
def create_user(username, email, password_hash):
    """
    Structure and insert a new user document.
    """
    user_document = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "total_eco_points": 0,          # Starts at zero
        "created_at": datetime.utcnow()
    }
    return users_col.insert_one(user_document).inserted_id

def find_user_by_email(email):
    return users_col.find_one({"email": email})


# ==========================================
# 2. CARBON LOGS COLLECTION HANDLERS
# ==========================================
def add_carbon_log(user_id, transport_type, distance_km, appliance_hours, emissions_kg, points):
    """
    Structure and insert a daily carbon tracking document.
    """
    log_document = {
        "user_id": ObjectId(user_id),   # Link log to a specific user
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "transport_type": transport_type,
        "distance_km": float(distance_km),
        "appliance_hours": float(appliance_hours),
        "calculated_emissions_kg": float(emissions_kg),
        "points_earned": int(points)
    }
    
    # 1. Insert the log
    result = carbon_logs_col.insert_one(log_document)
    
    # 2. Update the user's total Eco-Points in the users collection
    users_col.update_one(
        {"_id": ObjectId(user_id)},
        {"$inc": {"total_eco_points": int(points)}}
    )
    return result.inserted_id


# ==========================================
# 3. E-WASTE LOGS COLLECTION HANDLERS
# ==========================================
def schedule_ewaste_dropoff(user_id, device_type, quantity, center_name, scheduled_date):
    """
    Structure and insert an e-waste recycling appointment.
    """
    ewaste_document = {
        "user_id": ObjectId(user_id),
        "device_type": device_type,
        "quantity": int(quantity),
        "center_name": center_name,
        "status": "Pending",            # Default status
        "scheduled_date": scheduled_date,
        "created_at": datetime.utcnow()
    }
    return ewaste_logs_col.insert_one(ewaste_document).inserted_id