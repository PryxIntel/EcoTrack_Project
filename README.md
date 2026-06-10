<div align="center">



\# 🌱 EcoTrack



\### Hyper-Local Carbon Footprint \& E-Waste Management Platform



\[!\[SDG 13](https://img.shields.io/badge/SDG-13%20Climate%20Action-success?style=for-the-badge)](https://sdgs.un.org/goals/goal13)

\[!\[Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org)

\[!\[Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com)

\[!\[MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-green?style=for-the-badge\&logo=mongodb\&logoColor=white)](https://www.mongodb.com)

\[!\[Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](#)



A full-stack sustainability platform designed to help users calculate carbon emissions, monitor energy consumption, earn eco-rewards, and manage electronic waste responsibly.



</div>



\---



\## 📖 Project Overview



\*\*EcoTrack\*\* is a full-stack web application developed to support the \*\*United Nations Sustainable Development Goal 13 (Climate Action)\*\*. 



While environmental sustainability can feel abstract and difficult to measure at an individual level, EcoTrack bridges this gap. The platform equips users with practical tools to calculate personal CO₂ emissions, visualize their environmental footprint through dynamic analytics, engage in community-driven leaderboards, and maintain a secure digital ledger for e-waste disposal. 



By transforming awareness into measurable, gamified data, EcoTrack empowers individuals to take direct responsibility for their ecological footprint.



\---



\## 🎯 Problem Statement



Most individuals want to live more sustainably but lack the structural tools to measure or mitigate their daily impact. Current challenges include:



\* \*\*Blind Spots in Carbon Data:\*\* Limited awareness of how everyday commuting and appliance choices translate into raw carbon numbers.

\* \*\*Lack of Tracking Mechanisms:\*\* No unified historical view to check if personal sustainability habits are actually improving over time.

\* \*\*The E-Waste Crisis:\*\* Improper disposal of household electronics due to a lack of organized documentation and tracking systems.

\* \*\*Isolated Efforts:\*\* Minimal community interaction or gamified incentives to drive long-term, climate-conscious behavioral changes.



EcoTrack provides a centralized, data-driven ecosystem to tackle these challenges effectively.



\---



\## ✨ Key Features



\### 🌍 Carbon Footprint Calculator

\* Estimates precise carbon emissions based on daily transport modes and vehicle details.

\* Quantifies household energy footprints by tracking domestic utility data and appliance runtimes.



\### 📊 Analytics Dashboard

\* Powered by \*\*Chart.js\*\* to render real-time, interactive performance metrics.

\* Displays historical tracking, monthly emission trends, and category breakdown charts.



\### 🏆 EcoPoints \& Leaderboard System

\* Incentivizes eco-friendly choices with standard \*\*EcoPoint\*\* rewards.

\* Features a community-wide leaderboard to foster healthy competition and continuous engagement.



\### ♻️ E-Waste Management Ledger

\* Logs electronic items heading for disposal to support responsible recycling practices.

\* Tracks structural lifecycle metrics to minimize hazardous trace metals in municipal waste streams.



\### 🔐 Secure Authentication \& Security

\* Built-in user signup, login workflows, and active session states.

\* Utilizes \*\*Werkzeug\*\* security protocols for industry-standard password hashing and data safety.



\---



\## 🛠️ Technology Stack



| Layer | Technology | Purpose |

| :--- | :--- | :--- |

| \*\*Frontend\*\* | HTML5, CSS3, JavaScript | Core structure, styling, and interactive client logic |

| \*\*UI Framework\*\* | Bootstrap 5 | Fully responsive grid system and reusable components |

| \*\*Data Visualization\*\* | Chart.js | Renders responsive data trends and footprint tracking |

| \*\*Backend Framework\*\* | Flask (Python) | Robust server routing, API handling, and request logic |

| \*\*Database\*\* | MongoDB | Flexible, document-oriented NoSQL storage for high scalability |

| \*\*Security Layer\*\* | Werkzeug Security | Secure credential hashing and cryptographic helpers |

| \*\*Version Control\*\* | Git \& GitHub | Code management, review pipelines, and deployment |



\---



\## 🏗️ System Architecture



```text

&#x20;      ┌─────────────────────────────────────────┐

&#x20;      │             User Interface              │

&#x20;      │       (HTML5 • CSS3 • JavaScript)       │

&#x20;      └────────────────────┬────────────────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;      ┌─────────────────────────────────────────┐

&#x20;      │              Flask Backend              │

&#x20;      │            (Python Routing)             │

&#x20;      └──────────────┬─────────────┬────────────┘

&#x20;                     │             │

&#x20;        ┌────────────┴──┐       ┌──┴────────────┐

&#x20;        ▼               ▼       ▼               ▼

&#x20;  ┌───────────┐   ┌───────────────────────────────────┐

&#x20;  │  MongoDB  │   │      Session Management \&         │

&#x20;  │ Database  │   │   Authentication (Werkzeug)       │

&#x20;  └───────────┘   └───────────────────────────────────┘

