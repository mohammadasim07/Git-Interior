# ⚡ StormAPI — Full-Stack API Performance & Load Testing Platform

![Spring Boot](https://img.shields.io/badge/Spring_Boot_3.4-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Java 21](https://img.shields.io/badge/Java_21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=springsecurity&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket_STOMP-010101?style=for-the-badge&logo=socketdotio&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

StormAPI is an enterprise-grade, full-stack HTTP API performance testing platform engineered with **Java 21** and **Spring Boot 3.4**. It empowers developers and QA engineers to simulate realistic traffic loads, pinpoint bottlenecks, and validate system elasticity under extreme stress conditions.

---

## ✨ Key Features

- **6 Rigorous Testing Profiles**:
  - 📈 **Load Testing**: Assess system behavior under anticipated standard workloads.
  - 🔥 **Stress Testing**: Push APIs past peak operational thresholds to determine breaking points.
  - ⚡ **Spike Testing**: Simulate abrupt bursts of concurrent requests.
  - ⏳ **Soak Testing**: Continuous sustained load over time to diagnose memory leaks and resource exhaustion.
  - 💥 **Breakpoint Testing**: Incrementally scale concurrency until system failure to identify ceiling metrics.
  - 🔄 **Scalability Testing**: Verify system responsiveness as computational resources scale.
- **Real-Time Telemetry & Monitoring**:
  - Real-time latency, error-rate, and throughput analytics streamed via **WebSocket / STOMP**.
- **Automated Multi-Format Reporting**:
  - Automated report generation in **JSON, CSV, HTML, and PDF** formats with visual latency distribution curves.
- **Enterprise Security**:
  - Stateful & Stateless security with **Spring Security**, **JWT (JSON Web Tokens)**, and **OAuth2**.

---

## 🏗️ Architecture Overview

```
[ Client / Web UI ]
       │
       ▼ (HTTP / WebSocket STOMP)
[ Spring Boot 3.4 Controller Layer ]
       │
       ├──► [ Security & JWT Filter ]
       ├──► [ Test Execution Engine (Async / Virtual Threads) ]
       │         └── Worker Pool -> Target HTTP APIs
       │
       ├──► [ Real-Time Metrics Aggregator ] -> [ WebSocket Publisher ]
       └──► [ Report Generation Engine ] -> PDF / HTML / CSV / JSON
```

---

## 🚀 Getting Started

### Prerequisites
- **JDK 21** or higher
- **Maven 3.8+**
- **MySQL 8.0+**

### Installation & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mohammadasim07/StormAPI.git
   cd StormAPI
   ```

2. Configure MySQL database in `src/main/resources/application.properties`:
   ```properties
   spring.datasource.url=jdbc:mysql://localhost:3306/stormapi_db
   spring.datasource.username=root
   spring.datasource.password=yourpassword
   spring.jpa.hibernate.ddl-auto=update
   ```

3. Build and execute:
   ```bash
   mvn clean install
   mvn spring-boot:run
   ```

---

## 👨‍💻 Author
- **Mohammad Asim** — [GitHub](https://github.com/mohammadasim07) | [LinkedIn](https://www.linkedin.com/in/mohammadasim07)
