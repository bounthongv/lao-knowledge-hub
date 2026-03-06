# Deploy Backend to Render

**Quick deployment guide for Lao Knowledge Hub API**

---

## 🎯 What We're Doing

Deploy your FastAPI backend to Render.com so:
- ✅ Accessible from anywhere (not just localhost)
- ✅ Flutter app can connect from any device
- ✅ Free tier available
- ✅ Automatic HTTPS

---

## 📋 Prerequisites

- [ ] GitHub account (free)
- [ ] Render account (free - sign up with GitHub)
- [ ] Supabase project (already have: `nbvyybvgcdfeazcvecvy`)

---

## 🚀 Step-by-Step Deployment

### Step 1: Push Code to GitHub

```bash
# Navigate to project
cd D:\lao-knowledge-hub

# Check git status
git status

# Add all files
git add .

# Commit
git commit -m "Deploy backend to Render"

# Push to GitHub
git push origin main
```

**If you don't have a GitHub repo yet:**

```bash
# Create new repo on GitHub.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/lao-knowledge-hub.git
git branch -M main
git push -u origin main
```

---

### Step 2: Create Render Web Service

1. **Go to Render**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect your repository**:
   - Choose: `lao-knowledge-hub`
   - Click **"Connect"**

---

### Step 3: Configure Web Service

Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `lao-knowledge-hub-api` |
| **Region** | `Singapore` (closest to Laos) |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port 8000` |
| **Instance Type** | `Free` |

---

### Step 4: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"** → Add these:

```
SUPABASE_URL=https://nbvyybvgcdfeazcvecvy.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5idnl5YnZnY2RmZWF6Y3ZlY3Z5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIwMDE1NjMsImV4cCI6MjA4NzU3NzU2M30.uHbR33t8PuF92uUQFDIUX2Z93MlaNCQ8JZT5BrHQEds
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5idnl5YnZnY2RmZWF6Y3ZlY3Z5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MjAwMTU2MywiZXhwIjoyMDg3NTc3NTYzfQ.OW2R2YevOnrsX04uPPkCYDKiCcmjRoD9L6ejLyy8LNo

JWT_SECRET=HB+I1Mj8UNlSLQ5NKcLNzsQQ635XMDVsGbkoQDw6QvoSjHe8PUQFElec/ZPHaKEGjiUIgERvpRa8hFSgee7VKQ==
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=60

DEBUG=true
CORS_ORIGINS=http://localhost:3000,http://localhost:8080,https://*.renderapp.com
```

Click **"Save"**

---

### Step 5: Deploy!

1. **Click "Create Web Service"**
2. **Wait for deployment** (2-5 minutes)
3. **Copy your URL** (looks like: `https://lao-knowledge-hub-api-xyz.onrender.com`)

---

## ✅ Test Your Deployed API

### 1. Test Health Endpoint

```bash
curl https://YOUR-RENDER-URL.onrender.com/health
```

Expected: `{"status":"healthy","message":"Lao Knowledge Hub API is running"}`

### 2. Test Books Endpoint

```bash
curl https://YOUR-RENDER-URL.onrender.com/api/v1/books/popular
curl https://YOUR-RENDER-URL.onrender.com/api/v1/books/recommended
```

### 3. Test in Browser

Visit:
- `https://YOUR-RENDER-URL.onrender.com/health`
- `https://YOUR-RENDER-URL.onrender.com/docs` (Swagger UI)

---

## 🔧 Update Flutter App Configuration

After deployment, update your Flutter app to use the new backend URL:

### Edit `flutter-app/lib/config/constants.dart`:

```dart
class Constants {
  // OLD (localhost):
  // static const String apiUrl = 'http://localhost:8000';
  
  // NEW (Render):
  static const String apiUrl = 'https://YOUR-RENDER-URL.onrender.com';
  
  // Supabase config
  static const String supabaseUrl = 'https://nbvyybvgcdfeazcvecvy.supabase.co';
  static const String supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
}
```

---

## 📊 Add Sample Data (Optional but Recommended)

To see books in your app, run the SQL script:

1. **Open Supabase Dashboard**: https://app.supabase.com
2. **SQL Editor** → **New Query**
3. **Copy & Run**: `backend/seed_books_direct.sql`
4. **Done!** Books will appear in your app

---

## 🔍 Troubleshooting

### Deployment Failed

**Check logs in Render:**
1. Go to your service dashboard
2. Click **"Logs"** tab
3. Look for errors

**Common issues:**
- ❌ Missing `requirements.txt` → Make sure it's in `backend/` folder
- ❌ Wrong build command → Should be `pip install -r requirements.txt`
- ❌ Wrong start command → Should be `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### API Returns 500 Error

**Check environment variables:**
1. In Render dashboard, click **"Environment"**
2. Verify all Supabase keys are correct
3. Redeploy after changes (automatic)

### CORS Error from Flutter

**Update CORS_ORIGINS in Render:**
```
CORS_ORIGINS=http://localhost:3000,http://localhost:8080,https://*.renderapp.com,https://your-app.web.app
```

---

## 💰 Render Free Tier Limits

| Resource | Limit |
|----------|-------|
| **Monthly Usage** | 750 hours (enough for 1 instance running 24/7) |
| **RAM** | 512 MB |
| **CPU** | Shared |
| **Bandwidth** | 100 GB/month |
| **Sleep Mode** | Spins down after 15 min inactivity (wakes on next request) |

**Note:** Free tier instances sleep after 15 minutes of inactivity. First request after sleep takes ~30 seconds to wake up.

---

## 🎯 Next Steps After Deployment

1. ✅ **Test API endpoints** from your computer
2. ✅ **Update Flutter app** with Render URL
3. ✅ **Add sample data** to Supabase
4. ✅ **Run Flutter app** and see books display!
5. ✅ **Share URL** with team for testing

---

## 📁 Files Reference

```
backend/
├── Procfile              # ✅ Already configured
├── requirements.txt      # ✅ Already configured
├── app/
│   └── main.py          # ✅ API routes
└── .env.example         # Reference for env vars
```

---

## 🆘 Need Help?

- **Render Docs**: https://render.com/docs
- **FastAPI on Render**: https://render.com/docs/deploy-fastapi
- **Status Page**: https://status.render.com

---

**Ready to deploy?** Start with Step 1 (push to GitHub)! 🚀

**Last Updated:** 2026-03-06
