# Deployment Guide - Railway

## Step 1: Create a Railway Account
1. Go to https://railway.app
2. Sign up with GitHub account (easiest)
3. Connect your GitHub account

## Step 2: Prepare Your Code for Deployment
✅ Already done! Your code is ready.

## Step 3: Deploy on Railway

### Option A: Deploy from GitHub (Recommended)
1. **Push your code to GitHub**
   - Create a GitHub repository
   - Push the `junoweb` folder to GitHub
   - Make sure the `backend` folder is included

2. **On Railway.app:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect it's a Node.js project
   - Click "Deploy"

### Option B: Deploy using Railway CLI
1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **From your backend folder, login:**
   ```bash
   cd backend
   railway login
   ```

3. **Initialize and deploy:**
   ```bash
   railway init
   railway up
   ```

## Step 4: Set Environment Variables on Railway

1. Go to your Railway project dashboard
2. Click on the service/app
3. Go to "Variables" tab
4. Add these variables:
   - `JWT_SECRET` = (change to a strong random string, e.g., `juno-secret-key-2026-random123`)
   - `PORT` = Leave blank (Railway sets this automatically)

## Step 5: Get Your Deployment URL

1. In Railway dashboard, click your service
2. Go to "Settings" tab
3. Copy the **Domain URL** (looks like `https://your-app-name.railway.app`)
4. This is your live backend URL!

## Step 6: Update Your Frontend

Update `login.html` to use your live server:

Change this line:
```javascript
const API_URL = 'http://localhost:5000/api';
```

To:
```javascript
const API_URL = 'https://your-app-name.railway.app/api';
```

(Replace `your-app-name` with your actual Railway app URL)

## Step 7: Test It!

1. Open your login.html in a browser
2. Try registering a new account
3. Check that it works!

---

## Alternative Hosting Options

### Render.com
- Similar to Railway
- Free tier available
- Visit: https://render.com

### Fly.io
- Good for global deployment
- Free tier available
- Visit: https://fly.io

### Heroku (Deprecated Free Tier)
- Was free, now requires paid plan
- Not recommended for new projects

---

## Troubleshooting

**Database Error on Deployment:**
- SQLite works but is local to each dyno
- For production, you should upgrade to PostgreSQL
- Railway offers free PostgreSQL databases - let me know if you need help!

**CORS Error:**
- Make sure your frontend URL is accessible
- CORS is already enabled in your server.js

**Connection Refused:**
- Verify the API_URL in login.html matches your Railway domain
- Remove `http://` if the URL is `https://`

---

## Next Steps for Production

When your site grows, consider:
1. **Use PostgreSQL instead of SQLite** (better for production)
2. **Add email verification** for sign-ups
3. **Add password reset functionality**
4. **Use HTTPS everywhere** (already handled by Railway)
5. **Rate limiting** to prevent brute force attacks
6. **Email notifications** on registration

Let me know if you need help with any of these!
