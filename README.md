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



## SUPPORT

For any issues with deployment, contact your developer or refer to:
- Render docs: https://render.com/docs/deploy-django
- Cloudinary Django: https://cloudinary.com/documentation/django_integration
