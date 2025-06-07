# 📬 Cloud Run Email Notifier

This Python-based service allows you to securely send email alerts using Gmail SMTP through a deployed [Google Cloud Run](https://cloud.google.com/run) service. It authenticates using a service account and sends authorized POST requests to your Cloud Run endpoint.

---

## 🧰 Features

- Sends emails via Cloud Run with Google Identity Token authentication
- Uses Gmail SMTP under the hood
- Securely authenticated using service account credentials
- Supports local testing via authenticated HTTP request
- app directory contains the service to be deployed to google cloud

---

## 📁 File Structure

