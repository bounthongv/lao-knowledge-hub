# 🚀 Render Deployment Checklist

**Quick checklist for deploying Lao Knowledge Hub API to Render**

---

## ✅ Pre-Deployment

- [ ] GitHub account created
- [ ] Code pushed to GitHub
- [ ] Render account created (via GitHub)
- [ ] Supabase credentials ready

---

## ✅ Deployment Steps

### Step 1: Push to GitHub
```bash
cd D:\lao-knowledge-hub
git add .
git commit -m "Ready for Render deployment"
git push origin main
```
- [ ] Code pushed successfully

### Step 2: Create Render Service
- [ ] Logged into https://render.com
- [ ] Clicked "New +" → "Web Service"
- [ ] Connected GitHub repository

### Step 3: Configure Service
- [ ] Name: `lao-knowledge-hub-api`
- [ ] Region: `Singapore`
- [ ] Branch: `main`
- [ ] Root Directory: `backend`
- [ ] Runtime: `Python 3`
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- [ ] Instance Type: `Free`

### Step 4: Environment Variables
Add these in Render (Advanced → Environment Variables):

- [ ] `SUPABASE_URL` = `https://nbvyybvgcdfeazcvecvy.supabase.co`
- [ ] `SUPABASE_ANON_KEY` = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (full key)
- [ ] `SUPABASE_SERVICE_KEY` = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (full key)
- [ ] `JWT_SECRET` = `HB+I1Mj8UNlSLQ5NKcLNzsQQ635XMDVsGbkoQDw6QvoSjHe8PUQFElec/ZPHaKEGjiUIgERvpRa8hFSgee7VKQ==`
- [ ] `JWT_ALGORITHM` = `HS256`
- [ ] `JWT_EXPIRATION_MINUTES` = `60`
- [ ] `DEBUG` = `true`
- [ ] `CORS_ORIGINS` = `http://localhost:3000,http://localhost:8080,https://*.renderapp.com`

- [ ] Clicked "Save"

### Step 5: Deploy
- [ ] Clicked "Create Web Service"
- [ ] Waiting for deployment (2-5 minutes)
- [ ] Copied deployment URL: `https://______________________.onrender.com`

---

## ✅ Post-Deployment Testing

### Test API
- [ ] Visit: `https://YOUR-URL.onrender.com/health`
- [ ] Visit: `https://YOUR-URL.onrender.com/docs`
- [ ] Test: `curl https://YOUR-URL.onrender.com/api/v1/books/popular`
- [ ] Test: `curl https://YOUR-URL.onrender.com/api/v1/books/recommended`

### Expected Results
- [ ] Health endpoint returns: `{"status":"healthy",...}`
- [ ] Swagger UI loads at `/docs`
- [ ] Books endpoints return JSON (empty array or books)

---

## ✅ Update Flutter App

### Update `lib/config/constants.dart`:
```dart
// Change this:
static const String apiUrl = 'http://localhost:8000/api/v1';

// To this:
static const String apiUrl = 'https://YOUR-URL.onrender.com/api/v1';
```

- [ ] Updated constants.dart
- [ ] Saved file

### Test Flutter App
```bash
cd flutter-app
flutter run -d chrome
```

- [ ] App starts
- [ ] Can login/register
- [ ] Home screen loads
- [ ] Books display (if sample data added)

---

## ✅ Add Sample Data (Recommended)

- [ ] Opened Supabase Dashboard
- [ ] Opened SQL Editor
- [ ] Ran `backend/seed_books_direct.sql`
- [ ] Verified 10 books added
- [ ] Refreshed Flutter app → Books appear!

---

## 🎉 Deployment Complete!

Your API is now:
- ✅ Live on the internet
- ✅ Accessible from any device
- ✅ Using HTTPS automatically
- ✅ Connected to Supabase

**Share your URL:**
- API: `https://YOUR-URL.onrender.com`
- Docs: `https://YOUR-URL.onrender.com/docs`

---

## 📝 Notes

- **First load after sleep**: ~30 seconds (free tier limitation)
- **Logs**: View in Render dashboard → Logs tab
- **Auto-deploy**: Push to GitHub → Render auto-deploys
- **Manual restart**: Render dashboard → Manual Deploy button

---

**Need help?** See `DEPLOY_TO_RENDER.md` for detailed instructions.

**Last Updated:** 2026-03-06
