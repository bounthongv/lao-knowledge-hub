# 🔍 Troubleshooting Render Deployment

## Find Your Render API URL

### Where to Look in Render Dashboard:

1. Go to: https://dashboard.render.com
2. Click on your service: `lao-knowledge-hub-api`
3. **At the very top** you'll see:

```
┌─────────────────────────────────────────┐
│  ✅ lao-knowledge-hub-api               │
│  https://lao-knowledge-hub-api-abc123.onrender.com  ← COPY THIS
└─────────────────────────────────────────┘
```

4. If you don't see it there:
   - Click **"Logs"** tab
   - Look for: `Listening on port 8000` or the URL

---

## ❌ "Failed" - What Does It Say?

### Check the Logs Tab

1. In Render dashboard, click **"Logs"**
2. Look for these errors:

#### Error: "Build failed"
**Problem**: Code didn't compile  
**Solution**: Check build logs for Python errors

#### Error: "Crashed" or "Exited"
**Problem**: App started but crashed  
**Solution**: Look for Python traceback in logs

#### Error: "Health check failed"
**Problem**: Render can't reach your app  
**Solution**: Make sure uvicorn is running on port 8000

#### Error: "Environment variables missing"
**Problem**: SUPABASE_URL not set  
**Solution**: Add environment variables

---

## ✅ Quick Fix Checklist

### 1. Check Service Status

In Render dashboard:
- Is there a **green dot** ✅ next to your service name?
- Or **red dot** ❌ ?

**Green** = Running  
**Red** = Crashed/Failed

### 2. Check Logs

Click **"Logs"** tab and look for:

✅ **Good signs:**
```
Build succeeded
Listening on port 8000
INFO:     Application startup complete.
```

❌ **Bad signs:**
```
Build failed
Error: ModuleNotFoundError
Error: KeyError: 'SUPABASE_URL'
Crashed
```

### 3. Check Environment Variables

Click **"Environment"** tab:

**Must have these:**
- [ ] `SUPABASE_URL`
- [ ] `SUPABASE_ANON_KEY`
- [ ] `SUPABASE_SERVICE_KEY`
- [ ] `JWT_SECRET`

**If missing:**
1. Click **"Add Environment Variable"**
2. Add each one from your `.env` file
3. Click **"Save Changes"**
4. Service will auto-redeploy

### 4. Test the URL

Once you find your URL (e.g., `https://lao-knowledge-hub-api-abc123.onrender.com`):

**Test in browser:**
```
https://lao-knowledge-hub-api-abc123.onrender.com/health
```

**Expected:**
```json
{"status":"healthy","message":"Lao Knowledge Hub API is running"}
```

**If you see:**
- **"Application not found"** → Service not running
- **"502 Bad Gateway"** → Service crashed, check logs
- **Loading forever** → Service stuck, restart it
- **JSON response** → ✅ Working! Copy this URL

---

## 🔧 How to Fix Common Issues

### Issue 1: Build Failed

**Check logs for:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solution:**
- Make sure `requirements.txt` is in the `backend/` folder
- Check Build Command is: `pip install -r requirements.txt`

### Issue 2: Environment Variables Missing

**Error in logs:**
```
KeyError: 'SUPABASE_URL'
```

**Solution:**
1. Go to **"Environment"** tab
2. Add all required variables (see above)
3. Service will redeploy automatically

### Issue 3: Service Crashes

**Logs show:**
```
Crashed with exit code 1
```

**Solution:**
1. Check logs for the error before crash
2. Usually missing environment variables
3. Or Supabase connection error

### Issue 4: CORS Error (in Flutter)

**Browser console shows:**
```
Access to fetch at '...' from origin '...' has been blocked by CORS policy
```

**Solution:**
1. In Render → Environment tab
2. Add or update: `CORS_ORIGINS`
3. Value: `http://localhost:3000,http://localhost:8080,https://*.web.app,https://*.renderapp.com`
4. Redeploy

---

## 📝 What to Share for Help

If you need help, share:

1. **Your Render URL** (the `.onrender.com` one)
2. **Screenshot of Logs tab** (last 20 lines)
3. **Screenshot of Environment tab** (hide the actual keys, just show variable names)
4. **What error you see** in Flutter app

---

## 🚀 Quick Restart

If service is stuck:

1. Go to Render dashboard
2. Click your service
3. Click **"Manual Deploy"** button
4. Select branch: `main`
5. Click **"Deploy"**

This forces a fresh deployment.

---

**Next Step:** 
1. Find your `.onrender.com` URL
2. Test it in browser: `https://YOUR-URL.onrender.com/health`
3. Share the URL so I can update your Flutter app!
