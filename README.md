# IngufuPay - Smart Prepaid Electricity Payment System

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Designs & Documentation](#designs--documentation)
- [API Documentation](#api-documentation)
- [Deployment Plan](#deployment-plan)
- [Contributing](#contributing)
- [License](#license)

## Description

**IngufuPay** is a comprehensive digital platform for managing prepaid electricity payments and monitoring power consumption. The system enables both household and institutional users to:

- Register and manage multiple electricity meters
- Check real-time meter balances and consumption
- Purchase electricity units through mobile money providers (MTN, Airtel)
- Generate and redeem token-based purchases
- Track payment history and transaction records
- Receive low-balance alerts and consumption notifications
- Generate detailed consumption reports

The platform features a **Django REST Framework backend** providing RESTful APIs and a **responsive vanilla JavaScript frontend** for seamless user experience across devices.

### Target Users
- **Household Users**: Individual customers managing residential meters
- **Institution Users**: Organizations managing multiple meters across different locations, departments, and buildings

---

## Features

### Core Functionality
✅ **User Authentication & Authorization**
- Secure login/registration with JWT tokens
- Role-based access control (household vs. institution)
- Profile management

✅ **Meter Management**
- Register multiple meters
- Monitor real-time balance and consumption
- Meter status tracking (Active, Inactive, Suspended)
- Building and department categorization for institutions

✅ **Payment Processing**
- Multiple payment provider integration (MTN Mobile Money, Airtel Money)
- Real-time unit conversion and pricing
- Transaction status tracking (Pending, Success, Failed)
- Automatic balance updates

✅ **Token System**
- Generate prepaid tokens for offline distribution
- Manual token redemption
- Token expiry management
- Redeemed token tracking

✅ **Transaction History & Reporting**
- Comprehensive transaction logging
- Filterable transaction history by date, type, status
- Transaction receipt generation
- Monthly consumption reports
