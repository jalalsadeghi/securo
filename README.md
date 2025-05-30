# Securo: Cloud-Based Cybersecurity Platform

Securo is a cloud-native cybersecurity platform designed to protect systems using real-time monitoring, agent-based logging, and automated alerting. The MVP includes core components for user registration, agent deployment, log collection (via Wazuh and Suricata), and automatic email alerts upon detecting security threats.

---

## 📌 Features (MVP Scope)

| Feature                              | Description                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| User Registration                    | Web-based form to create secure user accounts                              |
| Agent Installation & Reporting       | Lightweight agent scripts report system data to the platform               |
| Log Collection with Wazuh            | HIDS log collection for files, processes, and anomalies                    |
| Network Monitoring with Suricata     | IDS/IPS to detect network-based threats                                    |
| Alert Processing                     | Automatic threat level parsing and categorization                          |
| Email Notifications                  | Critical alerts sent via email to affected users                           |
| Web UI (Frontend)                    | React/Next.js interface to manage users and agents                         |
| API Server (Backend)                 | FastAPI service handling user, agent, and alert management                 |
| PostgreSQL Database                  | Relational store for users, agents, and alerts                             |
| Docker-Based Architecture            | Entire system orchestrated with Docker Compose                             |

---

## ⚙️ Technology Stack

- **Frontend:** React, Next.js, TypeScript
- **Backend:** FastAPI, Python 3.12
- **Database:** PostgreSQL 16
- **Security Tools:** Wazuh (HIDS), Suricata (IDS/IPS)
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Email Alerts:** aiosmtplib with SMTP configuration
- **Testing:** Pytest, pytest-asyncio, HTTPX

---

## 📦 Prerequisites

- Docker & Docker Compose installed
- Open SMTP credentials (for alert emails)

---

## 🚀 Installation & Running (via Docker)

1. **Clone the Repository:**
```bash
git clone https://github.com/jalalsadeghi/securo.git
cd securo
```

2. **Configure Environment Variables:**
```bash
cp .env.example .env
# Edit `.env` with your PostgreSQL and SMTP credentials
```

3. **Run the Entire Stack:**
```bash
docker compose up -d --build
```

4. **Access Services:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

---

## 📡 API Endpoints

| Endpoint                        | Method | Description                          |
|--------------------------------|--------|--------------------------------------|
| `/users/register`              | POST   | Register a new user                  |
| `/agents/{user_id}/create`     | POST   | Register a new agent for a user      |
| `/alerts/{user_id}`            | GET    | Fetch alerts for a given user        |

---

## 🧪 Testing

1. Enter backend container:
```bash
docker compose exec backend bash
```

2. Run tests:
```bash
pytest
```
Tests cover user registration, agent registration, and email alert delivery.

---

## 📁 Directory Structure

```
securo/
├── backend/
│   ├── src/
│   ├── tests/
│   └── Dockerfile
├── frontend/
│   ├── src/
│   └── Dockerfile
├── database/init.sql
├── security-config/ (Wazuh/Suricata)
├── docker-compose.yml
├── .env.example
└── .github/workflows/ci-cd.yml
```

---

## 🪪 License

This project is licensed under the **MIT License** — allowing personal, academic, and commercial use while maintaining open-source visibility.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request. Feedback, issues, and stars are appreciated!

---

**Author:** [Jalal Sadeghi](https://github.com/jalalsadeghi)  
**Project Repository:** [github.com/jalalsadeghi/securo](https://github.com/jalalsadeghi/securo)

