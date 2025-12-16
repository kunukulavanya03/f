# f

Backend API for f

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
f/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration
- User login
- Password reset
- User profile management
- User listing

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to an existing user account.
- `POST /api/password_reset` - Reset the password for a user account.
- `GET /api/profile` - Retrieve the profile information for the currently logged in user.
- `PUT /api/profile` - Update the profile information for the currently logged in user.
- `GET /api/users` - Retrieve a list of all users.
- `GET /api/users/{user_id}` - Retrieve the profile information for a specific user.

## License

MIT
