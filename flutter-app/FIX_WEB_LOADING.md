# 🚨 Flutter Web Loading Issue - FIXED

## Problem
Flutter web app stuck loading infinitely because it was trying to connect to `http://localhost:8000` which doesn't work when deployed.

## ✅ Solution Applied

### 1. Updated API Service
Changed `lib/services/api_service.dart` to use centralized constants instead of hardcoded localhost.

### 2. Updated Constants
Changed `lib/config/constants.dart` to use Render URL instead of localhost.

## 🔧 What You Need to Do

### Step 1: Get Your Render URL

1. Go to your **Render Dashboard**: https://dashboard.render.com
2. Click on your service: `lao-knowledge-hub-api`
3. Copy the URL at the top (looks like):
   ```
   https://lao-knowledge-hub-api-abc123.onrender.com
   ```

### Step 2: Update Flutter Constants

Open: `flutter-app/lib/config/constants.dart`

Replace this line:
```dart
static const String apiUrl = 'https://lao-knowledge-hub-api.onrender.com/api/v1';
```

With your actual URL:
```dart
static const String apiUrl = 'https://YOUR-ACTUAL-URL.onrender.com/api/v1';
```

Also update:
```dart
static const String healthUrl = 'https://YOUR-ACTUAL-URL.onrender.com/health';
```

### Step 3: Rebuild & Deploy Flutter Web

```bash
cd flutter-app

# Clean build
flutter clean

# Get dependencies
flutter pub get

# Build for web
flutter build web

# Deploy (choose your hosting)
# Option A: Firebase Hosting
firebase deploy --only hosting

# Option B: Render (upload web folder)
# Option C: Test locally first
flutter run -d chrome
```

## ✅ Test It Works

### 1. Test API Directly
Visit in browser:
```
https://YOUR-URL.onrender.com/health
https://YOUR-URL.onrender.com/api/v1/books/popular
```

Should return JSON, not error.

### 2. Test Flutter Web Locally
```bash
cd flutter-app
flutter run -d chrome
```

Should load without infinite spinner.

### 3. Check Console Logs

Press **F12** in Chrome → Console tab

Look for:
- ✅ `Health check passed`
- ✅ `Loaded X books`
- ❌ Any red errors (connection refused, timeout, etc.)

## 🐛 Still Not Working?

### Check 1: Render Service Status

Go to Render dashboard:
- Is service **Running** (green dot)?
- Check **Logs** tab for errors
- Look for "Listening on port 8000"

### Check 2: Environment Variables

In Render → Environment:
- ✅ `SUPABASE_URL` set
- ✅ `SUPABASE_ANON_KEY` set
- ✅ `SUPABASE_SERVICE_KEY` set
- ✅ `JWT_SECRET` set

### Check 3: CORS

If you see CORS error in browser console:

Update `CORS_ORIGINS` in Render environment:
```
CORS_ORIGINS=http://localhost:3000,http://localhost:8080,https://*.renderapp.com,https://your-app.web.app
```

Redeploy after changing.

## 📝 Common Issues

### Issue: "Connection refused" or "Failed to connect"
**Cause**: API URL is still localhost  
**Fix**: Update constants.dart with Render URL

### Issue: "CORS policy"
**Cause**: Render not allowing your domain  
**Fix**: Update CORS_ORIGINS environment variable

### Issue: "502 Bad Gateway"
**Cause**: Render service crashed  
**Fix**: Check Render logs, restart service

### Issue: Infinite loading spinner
**Cause**: API returning error or timeout  
**Fix**: 
1. Check API health endpoint works
2. Check browser console for errors
3. Verify Render service is running

## 🎯 Quick Fix Checklist

- [ ] Copied Render URL from dashboard
- [ ] Updated `constants.dart` with actual URL
- [ ] Ran `flutter clean`
- [ ] Ran `flutter pub get`
- [ ] Tested API health endpoint in browser
- [ ] Rebuilt Flutter web: `flutter build web`
- [ ] Checked browser console (F12) for errors
- [ ] Verified Render service is running (green dot)

## 💡 Pro Tip

Add this to your `main.dart` for debugging:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Debug: Print API URL
  print('🔗 API URL: ${AppConstants.apiUrl}');
  print('🔗 Supabase URL: ${AppConstants.supabaseUrl}');
  
  // Test API connection
  try {
    final health = await ApiService.healthCheck();
    print('✅ API Health: ${health ? "OK" : "FAILED"}');
  } catch (e) {
    print('❌ API Connection Failed: $e');
  }
  
  await Supabase.initialize(
    url: AppConstants.supabaseUrl,
    anonKey: AppConstants.supabaseAnonKey,
  );

  runApp(const MyApp());
}
```

This will show in console if the API is reachable!

---

**What's your Render URL?** I can update the files for you if you share it.

**Last Updated:** 2026-03-06
