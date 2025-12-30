**UNNES Smart Drink Sales Predictor**
The UNNES Smart Drink Sales Predictor is a data engineering solution designed to optimize beverage inventory management through weather-based demand forecasting. Developed as a strategic asset for the Entrepreneurship course at Universitas Negeri Semarang (UNNES), this project integrates real-time environmental data with business logic to drive smarter retail operations.

**Project Overview**
This project is a weather-aware predictive system that automates the collection and analysis of meteorological data to forecast beverage sales. It utilizes a Modern Data Stack (MDS) to create a seamless flow from raw API data to actionable business insights. The system is fully containerized using Docker and orchestrated by Apache Airflow, ensuring that the sales predictions are updated automatically based on the latest local weather conditions around the UNNES campus.

**Problem Statement**
Vending machine and beverage stall operators at UNNES frequently face two critical operational challenges:

- Inventory Waste Perishable supplies, particularly ice cubes and fresh ingredients, are often overstocked during rainy or cool days, leading to direct financial loss.

- Missed Revenue Opportunities During unexpected heatwaves or high-temperature days, stock levels for cold refreshments often fail to meet the sudden surge in demand, resulting in lost sales.

The lack of a scientific method to correlate weather patterns with inventory levels prevents student entrepreneurs from maximizing their profit margins.

**Goals and Benefits**
The primary objective is to transform weather data into a strategic business advantage.

- Precision Inventory Planning The system enables owners to adjust their stock levels for cold versus warm beverages based on 24-hour weather forecasts.

- Waste Reduction By predicting days with high rainfall or lower temperatures, the system helps minimize the over-purchase of perishable cooling agents like ice.

- Automated Business Intelligence The implementation of Apache Airflow removes the need for manual data checking, providing a consistent and reliable recommendation engine for the business owner.

- Data-Driven Decision Making Owners move away from "gut-feeling" estimations toward a model supported by historical weather trends and predicted sales volume.

**#Technical Results and Outputs**
The project successfully delivers a complete ELT (Extract, Load, Transform) pipeline with the following outputs.

**Automated Data Pipeline**
The system utilizes Python to extract data from the OpenWeatherMap API. These records are loaded into a BigQuery Raw Layer. Apache Airflow manages the entire workflow, ensuring data arrives on schedule without manual intervention.

**Transformed Sales Mart**
Using dbt (data build tool), the raw weather data is transformed into a Sales Mart. This layer calculates the "Predictive Demand Index," which categorizes upcoming days into "High Cold-Drink Demand" or "High Warm-Drink Demand" scenarios.

**Looker Studio Dashboard**
The final output is an interactive Looker Studio Dashboard. This visual interface provides the business owner with a 7-day outlook of predicted sales trends, current temperature alerts, and specific inventory recommendations for the UNNES campus area.

**Conclusion**
The UNNES Smart Drink Sales Predictor demonstrates that technical data engineering frameworks can be directly applied to solve fundamental entrepreneurial problems. By bridging the gap between environmental data and retail logistics, the project provides a scalable model for reducing operational waste and increasing profitability. This system serves as a foundation for more advanced machine learning models that could eventually incorporate university event calendars and student schedules to further refine sales accuracy.