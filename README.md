\# EcoTrack 🌱



\### Hyper-Local Carbon Footprint \& E-Waste Management Platform



<p align="center">

&#x20; <img src="https://img.shields.io/badge/SDG-13%20Climate%20Action-success" />

&#x20; <img src="https://img.shields.io/badge/Python-3.10-blue" />

&#x20; <img src="https://img.shields.io/badge/Flask-Web%20Framework-black" />

&#x20; <img src="https://img.shields.io/badge/MongoDB-NoSQL-green" />

&#x20; <img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</p>



\---



\## Project Overview



EcoTrack is a full-stack web application developed to support \*\*United Nations Sustainable Development Goal (SDG) 13 – Climate Action\*\*.



The platform empowers users to monitor their environmental impact through carbon footprint tracking, utility consumption analysis, sustainability scoring, and responsible electronic waste management.



By transforming daily activities into measurable environmental metrics, EcoTrack helps users make informed decisions toward a greener and more sustainable future.



\---



\## Problem Statement



Environmental awareness often remains theoretical because individuals lack practical tools to measure their personal impact.



Key challenges include:



\* Limited visibility into individual carbon emissions

\* Lack of community engagement in sustainable practices

\* Improper disposal of electronic waste

\* Absence of simple environmental tracking systems



EcoTrack addresses these issues through data-driven monitoring and user engagement mechanisms.



\---



\## Key Features



\### Carbon Footprint Calculator



Calculate estimated CO₂ emissions based on:



\* Daily commuting activities

\* Vehicle usage

\* Energy consumption patterns

\* Appliance utilization



\### Analytics Dashboard



Interactive dashboard providing:



\* Emission trend visualization

\* Historical carbon records

\* Sustainability analytics

\* User performance tracking



\### EcoPoints Reward System



Gamified sustainability model featuring:



\* EcoPoint accumulation

\* Community leaderboard

\* Environmental achievement tracking



\### E-Waste Disposal Ledger



Digital e-waste management system allowing users to:



\* Record electronic waste entries

\* Track disposal activities

\* Promote responsible recycling practices



\### Secure User Authentication



\* User Registration

\* Login System

\* Password Hashing

\* Session Management



\---



\## Technology Stack



| Layer              | Technologies            |

| ------------------ | ----------------------- |

| Frontend           | HTML5, CSS3, JavaScript |

| UI Framework       | Bootstrap 5             |

| Data Visualization | Chart.js                |

| Backend            | Flask (Python)          |

| Database           | MongoDB                 |

| Authentication     | Werkzeug Security       |

| Version Control    | Git \& GitHub            |



\---



\## System Architecture



```text

User Interface

&#x20;      │

&#x20;      ▼

HTML + CSS + JavaScript

&#x20;      │

&#x20;      ▼

Flask Backend

&#x20;      │

&#x20;┌─────┴─────┐

&#x20;▼           ▼

MongoDB   Authentication

Database   \& Sessions

```



\---



\## Project Structure



```text

EcoTrack\_Project/

│

├── app.py

├── config.py

├── requirements.txt

│

├── database/

│   └── db\_handler.py

│

├── static/

│   ├── css/

│   │   └── style.css

│   │

│   └── js/

│       ├── dashboard.js

│       └── main.js

│

└── templates/

&#x20;   ├── base.html

&#x20;   ├── index.html

&#x20;   ├── login.html

&#x20;   ├── register.html

&#x20;   ├── dashboard.html

&#x20;   ├── calculator.html

&#x20;   └── ewaste.html

```



\---



\## Installation



\### Clone Repository



```bash

git clone https://github.com/PryxIntel/EcoTrack\_Project.git

cd EcoTrack\_Project

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Configure Database



Ensure MongoDB is running locally or update your MongoDB Atlas connection string inside:



```python

config.py

```



\### Run Application



```bash

python app.py

```



Open:



```text

http://127.0.0.1:5000

```



\---



\## SDG Alignment



\### SDG 13 – Climate Action



EcoTrack contributes to climate action by:



\* Raising environmental awareness

\* Monitoring carbon emissions

\* Encouraging sustainable behavior

\* Supporting responsible e-waste disposal



\---



\## Future Enhancements



\* GPS-based automatic travel tracking

\* AI-powered sustainability recommendations

\* Recycling center location mapping

\* Mobile application support

\* Administrative dashboard for municipal authorities



\---



\## Developer



\*\*Priyanshu Chauhan\*\*

B.Tech – Computer Science \& Engineering

Madan Mohan Malaviya University of Technology (MMMUT)



GitHub: https://github.com/PryxIntel



\---



\## License



This project is developed for academic and educational purposes under a university capstone project initiative.



\---



<p align="center">

&#x20; Built with ❤️ for SDG 13 – Climate Action

</p>



