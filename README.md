EcoTrack - Hyper-Local Carbon and E-Waste Ledger

Project Context and SDG Alignment

EcoTrack is a full-stack web application engineered to address UN Sustainable Development Goal 13 (Climate Action). While macro-level environmental policies are debated globally, individual tools for precise carbon tracking and electronic waste (e-waste) auditing remain heavily fragmented. Consumer electronics are replaced at an accelerated rate, creating an unmonitored stream of digital toxic waste.



EcoTrack bridges this gap by turning abstract climate goals into explicit, numerical feedback loops. It allows citizens to quantitatively track their physical commuting habits, audit household utility energy drawings, compete on a community leaderboard, and log structural electronic disposal slips to keep toxic materials out of traditional residential waste grids.



Key Architectural Features

Carbon Footprint Calculation Engine: A server-side algorithm built into Flask that processes routine daily metrics (transit parameters, utility asset uptimes) and translates them dynamically into exact kilogram CO2 emission values.



Dynamic Analytics Dashboard: Pulls historic time-series logging data asynchronously from MongoDB and leverages a client-side visualization engine (Chart.js) to plot interactive emission progression trends.



Gamified Reward Matrix: Implements an aggregate point-allocation layer that awards Eco-Points to users maintaining low-emission thresholds, sorting profiles into a live community leaderboard.



E-Waste Disposal Ledger: A transactional auditing directory where users schedule drop-off slots for obsolete hardware, mitigating the risk of toxic heavy metals (lead, mercury, cadmium) leaching into surrounding soil matrices.



Tech Stack and Dependencies

Frontend: HTML5, CSS3, JavaScript (Chart.js for visualizations, Bootstrap 5 for responsive mobile-first layouts, FontAwesome for iconography)



Backend Framework: Flask (Python 3.10) handling application routing, security context, and session states.



Database Layer: MongoDB NoSQL document store, optimized for flexible schemas, time-series metrics, and transactional log indices.



Security Middleware: Production-grade cryptographic password salting and hashing handled via werkzeug.security.



Directory Structure

ecotrack/

├── app.py                      # Main entry point and Flask routing configurations

├── config.py                   # Environment variable rules and database connection parameters

├── database/

│   └── db\_handler.py           # MongoDB collections, schema structures, and CRUD helper queries

├── static/

│   ├── css/

│   │   └── style.css           # Custom UI presentation branding, animations, and accents

│   └── js/

│       ├── dashboard.js        # Chart.js time-series dataset parsing and graph compilation

│       └── main.js             # Client-side form validations and UI behavior rules

├── templates/

│   ├── base.html               # Master layout containing shared navbar, flash messages, and CDN links

│   ├── index.html              # Landing homepage displaying SDG 13 project objectives

│   ├── login.html              # User session authentication gateway

│   ├── register.html           # cryptographically secured account creation form

│   ├── dashboard.html          # Interactive graph platform and live top-5 ranking board

│   ├── calculator.html         # Commuter and appliance logging interface

│   └── ewaste.html             # Electronics recycling hub asset reservation system

└── requirements.txt            # System dependency declarations



Installation and Local Setup

To deploy and test the system locally on your terminal, execute the following configuration steps:



Clone the Workspace:

git clone https://github.com/YOUR\_USERNAME/EcoTrack\_Project.git

cd EcoTrack\_Project



Install Required Packages:

pip install -r requirements.txt



Database Configuration:

Ensure a local instance of MongoDB is active on port 27017 or insert your production MongoDB Atlas cloud cluster connection string securely inside config.py.



Boot the Web Application:

python app.py



Navigate to http://127.0.0.1:5000 inside your web browser to interact with the platform.



Future Scope and Scalability

Automated Telemetry: Replacing manual entry forms with background GPS transit logging using mobile location tracking APIs.



Geospatial Mapping Layers: Swapping standard select boxes for an interactive map layout using Leaflet.js to pinpoint physical e-waste center coordinates instantly.



Role-Based Administrative Access: Integrating separate dashboard controls for verified municipal sanitation workers to review, manage, and mark submitted recycling appointments as Disposed.

