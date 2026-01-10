# Juno Authentication System

A Node.js + Express backend with SQLite database for user authentication.

## Setup Instructions

### 1. Install Dependencies

Navigate to the backend folder and install npm packages:

```bash
cd backend
npm install
```

### 2. Start the Server

Development mode (with auto-reload):
```bash
npm run dev
```

Production mode:
```bash
npm start
```

The server will run on `http://localhost:5000`

### 3. Test the API

#### Register a new user
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","password":"password123","confirmPassword":"password123"}'
```

#### Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"password123"}'
```

#### Check your profile (requires token)
```bash
curl -X GET http://localhost:5000/api/me \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## API Endpoints

### `POST /api/register`
Register a new user

**Request:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "confirmPassword": "password123"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### `POST /api/login`
Login an existing user

**Request:**
```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### `GET /api/me`
Get current user profile (requires authentication)

**Headers:**
```
Authorization: Bearer YOUR_TOKEN_HERE
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Frontend Integration

The login page (`login.html`) is already integrated with the backend. It:

1. Sends registration/login requests to the backend
2. Stores JWT token in localStorage
3. Shows success/error messages to users
4. Can redirect users after authentication

## Security Notes

- ⚠️ Change the `JWT_SECRET` in `.env` before deploying to production
- Passwords are hashed using bcryptjs
- JWT tokens expire after 7 days
- Use HTTPS in production
- Set up CORS properly for your domain

## Database

SQLite database file (`users.db`) is created automatically on first run. Users table structure:

```sql
id (INTEGER PRIMARY KEY)
name (TEXT)
email (TEXT UNIQUE)
password (TEXT hashed)
created_at (DATETIME)
```

## Troubleshooting

If the frontend can't connect to the backend:
- Make sure the backend server is running on port 5000
- Check CORS is enabled (should be by default)
- Open browser console (F12) to see network errors
- If you're running on a different port, update `API_URL` in `login.html`
