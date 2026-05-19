# AJAI PRANAV TEX — Website

A full-featured Django website for AJAI PRANAV TEX, Tirupur's export surplus garment store.

---

## FEATURES

- Stunning animated homepage with export surplus explanation
- 5 product category pages (T-Shirts, Track Pants, Shorts, Hoodies, Baby Garments)
- Photo gallery with lightbox viewer per category
- Admin panel to upload/delete/feature product images
- Cloudinary cloud image storage (free)
- WhatsApp integration throughout
- Google Maps embed for both store locations
- Fully responsive mobile design
- Free hosting on Render.com with PostgreSQL

---

## TECH STACK

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11 + Django 4.2 |
| Database | SQLite (local) / PostgreSQL (Render) |
| Image Storage | Cloudinary (free tier) |
| Static Files | WhiteNoise |
| Hosting | Render.com (free) |

---

## STEP 1 — CLOUDINARY SETUP (FREE IMAGE STORAGE)

1. Go to **https://cloudinary.com** → Sign Up Free
2. After signup, go to **Dashboard**
3. Note down these 3 values:
   - Cloud Name
   - API Key
   - API Secret
4. Keep these ready for Step 3.

---

## STEP 2 — LOCAL SETUP & TESTING

```bash
# 1. Extract this ZIP and open the folder
cd ajai_pranav_tex

# 2. Create virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy .env.example to .env
cp .env.example .env

# 5. Edit .env — fill in your Cloudinary credentials:
#    CLOUDINARY_CLOUD_NAME=your_cloud_name
#    CLOUDINARY_API_KEY=your_api_key
#    CLOUDINARY_API_SECRET=your_api_secret

# 6. Run migrations
python manage.py migrate

# 7. Start server
python manage.py runserver

# 8. Open browser: http://127.0.0.1:8000
```

### Admin Panel (local):
- URL: http://127.0.0.1:8000/admin/login/
- Username: `ajai`
- Password: `ajai@1`

---

## STEP 3 — FREE HOSTING ON RENDER.COM

### A) Push to GitHub first

1. Create a free account at **https://github.com**
2. Create a new repository called `ajai-pranav-tex`
3. Run these commands inside your project folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ajai-pranav-tex.git
git push -u origin main
```

### B) Deploy on Render.com

1. Go to **https://render.com** → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo `ajai-pranav-tex`
4. Fill in the settings:
   - **Name:** ajai-pranav-tex
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn ajai_pranav_tex.wsgi:application`
   - **Plan:** Free

5. Scroll down to **Environment Variables** and add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Any random 50-character string (use https://djecrety.ir) |
| `DEBUG` | `False` |
| `CLOUDINARY_CLOUD_NAME` | From Cloudinary dashboard |
| `CLOUDINARY_API_KEY` | From Cloudinary dashboard |
| `CLOUDINARY_API_SECRET` | From Cloudinary dashboard |
| `ADMIN_USERNAME` | `ajai` |
| `ADMIN_PASSWORD` | `ajai@1` |

6. Click **"Create Web Service"**

### C) Add Free PostgreSQL Database on Render

1. In Render dashboard → **"New +"** → **"PostgreSQL"**
2. Name it `ajai-pranav-tex-db`
3. Select **Free** plan → Create
4. Once created, copy the **Internal Database URL**
5. Go back to your Web Service → Environment → Add:
   - Key: `DATABASE_URL`, Value: (paste the URL)
6. Redeploy the service

Your site will be live at: **https://ajai-pranav-tex.onrender.com**

---

## STEP 4 — GOOGLE MAPS API (for embedded maps)

The contact page has Google Maps embeds. To make them work:

1. Go to **https://console.cloud.google.com**
2. Create a project → Enable "Maps Embed API"
3. Create an API key (free tier gives $200/month credit)
4. In `store/templates/store/contact.html`, replace:
   ```
   AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY
   ```
   with your actual API key.

> **Note:** Alternatively, you can replace the `<iframe>` src with a simple Google Maps share link (no API key needed):
> Go to Google Maps → search your address → Share → Embed a map → Copy iframe src

---

## FREE HOSTING OPTIONS COMPARISON

| Platform | Free Tier | Database | Sleeps? | Custom Domain |
|----------|-----------|----------|---------|---------------|
| **Render.com** ⭐ | 750 hrs/month | PostgreSQL free | Yes (15 min) | Yes (free) |
| **Railway.app** | $5 credit/month | PostgreSQL | No | Yes |
| **PythonAnywhere** | 1 app, 512MB | MySQL | No | Paid only |
| **Fly.io** | 3 VMs free | Postgres | No | Yes |

**Recommended: Render.com** — easiest for Django, free PostgreSQL, no credit card needed.

### About "Sleeping":
Render free tier "sleeps" after 15 minutes of inactivity. The first visitor after sleep waits ~30 seconds. This is fine for a small business site. To avoid it, upgrade to Starter ($7/month) or use Railway.

---

## ADMIN PANEL USAGE

1. Go to `yoursite.com/admin/login/`
2. Login: username `ajai`, password `ajai@1`
3. **Upload images:**
   - Select category (T-Shirts, Track Pants, etc.)
   - Add optional title/description
   - Check "Feature on Homepage" to show on home page
   - Select one or multiple image files
   - Click Upload
4. **Delete images:** Click "Del" button on any image card
5. **Feature/Unfeature:** Click "★ Feature" / "☆ Unfeature" toggle
6. **Filter by category:** Use the tab buttons above the image grid

---

## FOLDER STRUCTURE

```
ajai_pranav_tex/
├── ajai_pranav_tex/
│   ├── settings.py       ← Django settings
│   ├── urls.py           ← Main URL routing
│   └── wsgi.py
├── store/
│   ├── models.py         ← ProductImage model
│   ├── views.py          ← All page views + admin logic
│   ├── urls.py           ← Store URL patterns
│   └── templates/store/
│       ├── base.html         ← Navbar + Footer
│       ├── home.html         ← Homepage
│       ├── category.html     ← Product gallery page
│       ├── contact.html      ← Contact + Maps
│       ├── about.html        ← About page
│       ├── admin_login.html  ← Admin login
│       └── admin_dashboard.html ← Admin panel
├── requirements.txt
├── manage.py
├── build.sh              ← Render build script
├── Procfile              ← Gunicorn start command
├── render.yaml           ← Render deployment config
└── .env.example          ← Environment variable template
```

---

## CUSTOMIZATION

### Change Admin Password
Edit `.env` file:
```
ADMIN_PASSWORD=your_new_password
```
On Render, update the `ADMIN_PASSWORD` environment variable.

### Add Google Maps API Key
Replace the placeholder key in `contact.html` (search for `AIzaSyD-9t`).

### Change Phone Number
Search for `8870165008` across all template files and replace.

### Change Colors
In `base.html`, find the `:root` CSS block:
```css
:root {
    --gold: #c8952a;        ← Main gold color
    --gold-light: #e8b84b;  ← Lighter gold
    --black: #0a0a0a;       ← Background
}
```

---

## SUPPORT

For any issues with deployment, contact your developer or refer to:
- Render docs: https://render.com/docs/deploy-django
- Cloudinary Django: https://cloudinary.com/documentation/django_integration
