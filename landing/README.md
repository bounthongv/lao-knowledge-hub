# Lao Knowledge Hub - Landing Page

## 🎯 Architecture

```
Landing Page (HTML/CSS - SEO optimized)
    ↓
[Get Started Button]
    ↓
Flutter App (Login/Register → Dashboard)
```

## 📁 File Structure

```
lao-knowledge-hub/
├── landing/
│   └── index.html          ← Beautiful SEO-optimized landing page
├── flutter-app/
│   └── build/web/          ← Flutter app (accessed via landing page)
└── backend/
    └── app/                ← FastAPI backend
```

## 🚀 How to Use

### 1. View Landing Page
Open `landing/index.html` in your browser:
```bash
# Option 1: Direct file open
start landing\index.html

# Option 2: Using Python HTTP server
cd landing
python -m http.server 8080
# Then visit: http://localhost:8080
```

### 2. Navigate to App
Click **"Get Started"** button on landing page → Takes you to Flutter app

### 3. User Flow
1. **Landing Page** (`/landing/index.html`)
   - SEO-optimized content
   - Features showcase
   - Stats and social proof
   - "Get Started" button

2. **Login/Register** (`flutter-app/build/web/#/login`)
   - User authentication
   - Email verification

3. **Dashboard** (`flutter-app/build/web/#/home`)
   - Main app with books
   - User profile in AppBar

## 🎨 Landing Page Features

- ✅ **SEO Optimized**: Meta tags, keywords, Open Graph
- ✅ **Responsive**: Works on desktop, tablet, mobile
- ✅ **Bilingual**: Lao + English text
- ✅ **Modern Design**: Gradient backgrounds, smooth animations
- ✅ **Clear CTAs**: Multiple "Get Started" buttons
- ✅ **Social Proof**: Stats section (10,000+ books, 5,000+ students)

## 🔧 Customization

### Update Stats
Edit the numbers in `landing/index.html`:
```html
<div class="stat-item">
    <h3>10,000+</h3>
    <p>Books & Resources</p>
</div>
```

### Update Links
All links point to `flutter-app/build/web/` - update if you deploy elsewhere.

### Colors
Change CSS variables at top of `<style>` section:
```css
:root {
    --primary: #1E3A8A;      /* Deep Blue */
    --lao-red: #DC2626;      /* Lao Red */
    --gold: #F59E0B;         /* Gold */
}
```

## 📊 SEO Keywords Included

- Lao books
- Laos education
- Digital library
- NUOL (National University of Laos)
- Textbooks
- Lao language
- Academic books
- E-books Laos

## 🌐 Deployment

### Option 1: Firebase Hosting
```bash
# Copy landing page to public folder
cp landing/index.html public/

# Deploy
firebase deploy
```

### Option 2: Netlify
Drag and drop the `landing` folder to Netlify

### Option 3: GitHub Pages
Push to GitHub and enable Pages

## ✅ Next Steps

1. ✅ Landing page created
2. ✅ Flutter app builds successfully
3. ⏳ Connect FastAPI backend for books
4. ⏳ Deploy to production

---

**Ready for Step 2: Connect to FastAPI Backend** to display real books!