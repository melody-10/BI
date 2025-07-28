# 🧠 BI (Inteligencia de Negocios) <br> <br> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png" width=100> Academic Dataset Explorer

This Streamlit app was developed for a graduate-level Business Intelligence course. It provides interactive exploration and analysis of real-world business data, using the [Yelp Academic Dataset]

(https://business.yelp.com/data/resources/open-dataset/).

---

## 📚 Project Structure

- `/Data` – files containing Yelp academic dataset: https://business.yelp.com/data/resources/open-dataset/
- `/Modules` – Python scripts used for visualizations
- `/assets` – Images and logos used for visualizations
- `app.py` – Main Python Script to build the GUI Dashboard
- `requirements.txt` – Python dependencies


---

## 🧾 Dataset Description

The dataset was sourced from the **Yelp Open Dataset** and cleaned to focus on a balanced sample of business listings across **11 regions only**: AB, AZ, CA, FL, IN, LA, MO, NJ, NV, PA, TN


For each region, **5,000 businesses** were randomly sampled. The following columns were retained:

- `name`, `address`, `city`, `state`
- `latitude`, `longitude`
- `stars`, `review_count`, `is_open`
- `attributes`, `hours`

Additionally, business categories were one-hot encoded into **338 binary columns**, enabling flexible filtering and visualization.

---

## 📊 What You Can Do

✔️ Explore business distributions by category and state  
✔️ Analyze review trends and average ratings  
✔️ Filter by business type (e.g., Gyms, 'Real Estate', 'Candy Stores', 'Nutritionists', 'Tacos', etc.)  
✔️ Identify potential locations for new businesses  
✔️ Map businesses using geolocation data

---

## 🚀 Getting Started
streamlit APP

## 🧪 Technical Notes
Streamlit is used for the frontend UI and user interactions.

Core libraries include:

pandas for data handling

plotly and matplotlib for charts

folium for geospatial mapping

All reusable code modules live in the Modules/ directory (e.g., map_utils.py, category_charts.py).

## 🎓 Educational Use
This project is part of a graduate course in Business Intelligence and is designed to teach:

Real-world data wrangling and cleaning

Exploratory Data Analysis (EDA)

Interactive dashboards and filters

Geospatial decision support for business planning

Students are expected to build team projects that explore real opportunities for new businesses across regions.

## ⚠️ API Access Note
If you plan to use the Yelp Fusion API, you will need a work or institutional email address to request access. This requirement limits live data pulls during class. Instead, this project uses pre-downloaded and cleaned data for reliability.

## 📬 Contact
For questions, suggestions, or collaboration:

Edgar Avalos Gauna
✉️ edgaravalos@up.edu.mx

## 📘 License
This project is distributed for educational purposes and follows the licensing terms of the Yelp Academic Dataset.
