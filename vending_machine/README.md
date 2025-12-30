**Vending Machine Real-Time Data Pipeline**
The project implements a streaming data architecture that captures transaction logs from vending machines as they occur. By replacing traditional batch-reporting methods with a live data stream, providers can monitor their machines across the campus from a single centralized interface.

**System Functionality**
The core of this system is a distributed message broker that handles incoming data from various machines. The architecture is divided into three functional segments.

- Data Production Layer A Python script acts as the data source by simulating the activity of a vending machine. It generates JSON packets containing the machine ID, product name, price, and precise transaction timestamp.

- Message Brokerage Layer The system uses Apache Kafka configured in KRaft mode. This layer acts as a buffer and distributor for the data. It ensures that no transaction is lost even during high-traffic periods such as class breaks at UNNES.

- Monitoring Layer A Streamlit-based dashboard serves as the user interface. It consumes data directly from the Kafka stream and updates a visual table in real-time without requiring manual page refreshes.

**Operational Benefits for UNNES Providers**
Implementing this pipeline offers significant advantages for managing vending machines in a university environment.

- Elimination of Stock-Outs Providers can monitor inventory levels in real-time. This allows them to restock popular beverages or snacks immediately after they are sold out rather than waiting for a scheduled visit.

- Real-Time Revenue Tracking The dashboard displays a continuous feed of successful transactions. Owners can verify their total sales at any moment, providing full transparency into the financial performance of each machine location.

- Identification of Peak Demand By analyzing the timestamps of the transactions, providers can identify peak usage hours across different faculties at UNNES. This data helps in optimizing restocking schedules to avoid disrupting students during busy periods.

- Automated Data History All incoming transactions are formatted for storage in a PostgreSQL database. This allows for long-term statistical analysis to determine which products are most popular among students and staff.

**Deployment and Execution**
Technical Requirements
The infrastructure requires Docker Desktop for orchestration and Python 3.12 for local script execution.

**Building the Services**
Execute the following command in the root directory to initialize the Kafka broker, the PostgreSQL database, and the Monitoring Dashboard.

Bash:
docker compose up --build

Starting the Live Stream
Open a new terminal window to start the data simulation.

Bash:
python app/factory_sim.py

Viewing the Dashboard
Access the live sales monitoring interface via a web browser at the following address.

Browser:
http://localhost:8501