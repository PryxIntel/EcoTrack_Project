from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from database.db_handler import (
    create_user, find_user_by_email, add_carbon_log, schedule_ewaste_dropoff,
    users_col, carbon_logs_col, ewaste_logs_col
)
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object(Config)

# ==========================================
# AUTHENTICATION ROUTES
# ==========================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        if find_user_by_email(email):
            flash('Email address already exists!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        create_user(username, email, hashed_password)
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        user = find_user_by_email(email)
        if not user or not check_password_hash(user['password_hash'], password):
            flash('Invalid email or password!', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = str(user['_id'])
        session['username'] = user['username']
        flash(f"Welcome back, {user['username']}!", 'success')
        return redirect(url_for('dashboard'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# ==========================================
# CORE CORE FUNCTIONAL ROUTES
# ==========================================

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    # Fetch user data for points display
    user_data = users_col.find_one({"_id": ObjectId(session['user_id'])})
    
    # Fetch user's recent carbon logs for data visualization mapping
    logs = list(carbon_logs_col.find({"user_id": ObjectId(session['user_id'])}).sort("date", -1).limit(7))
    
    # Global leaderboard logic (Top 5 users by points)
    leaderboard = list(users_col.find({}, {"username": 1, "total_eco_points": 1}).sort("total_eco_points", -1).limit(5))
    
    return render_template('dashboard.html', user=user_data, logs=logs, leaderboard=leaderboard)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        transport = request.form.get('transport_type')
        distance = float(request.form.get('distance_km', 0))
        appliances = float(request.form.get('appliance_hours', 0))
        
        # Simple Carbon Footprint Engine Logic:
        # Standard constants: ~0.12kg CO2 per km for average transport, ~0.5kg CO2 per hour of high-draw appliances
        transport_emissions = distance * 0.12
        appliance_emissions = appliances * 0.5
        total_emissions = round(transport_emissions + appliance_emissions, 2)
        
        # Calculate Reward Points (Lower emissions = baseline points + bonus)
        base_points = 10
        bonus_points = max(0, int(30 - total_emissions))
        earned_points = base_points + bonus_points
        
        # Save log entry
        add_carbon_log(session['user_id'], transport, distance, appliances, total_emissions, earned_points)
        flash(f'Daily metrics logged! You earned {earned_points} Eco-Points.', 'success')
        return redirect(url_for('dashboard'))
        
    return render_template('calculator.html')

@app.route('/ewaste', methods=['GET', 'POST'])
def ewaste():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        device = request.form.get('device_type')
        qty = int(request.form.get('quantity', 1))
        center = request.form.get('center_name')
        date = request.form.get('scheduled_date')
        
        schedule_ewaste_dropoff(session['user_id'], device, qty, center, date)
        flash('Recycling request submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
        
    # Get user's previous drop-off logs
    appointments = list(ewaste_logs_col.find({"user_id": ObjectId(session['user_id'])}).sort("scheduled_date", 1))
    return render_template('ewaste.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)