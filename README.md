# E‑Commerce (Django)

A simple yet production-ready **e‑commerce website** built with Django. Features product listings, categories, authentication, a shopping cart (add/update/delete), and static file handling optimized for deployment.

---

## 📉 Live Demo

* **Site:** [Live Demo](https://djangocart.onrender.com/)
* **Admin:** [Admin Page](https://djangocart.onrender.com/admin)
* Example Credentials (demo): `user@example.com / password123`

---

## 🔍 About This Project

This project was built to practice and demonstrate:

* Django ORM for product & category management
* User authentication and session handling
* Cart functionality with add/update/delete
* Serving and optimizing static assets with **WhiteNoise**
* Deploying a Django app to **Render** with a production-ready configuration

---

## 💡 Features

* Product catalog and categories
* User authentication (register, login, logout)
* Shopping cart with quantity update and item removal
* Responsive Bootstrap UI
* Static asset pipeline via WhiteNoise
* SQLite (dev) / `DATABASE_URL` (prod)

---

## 🛠️ Tech Stack

* **Backend:** Django 5
* **Database:** SQLite (dev), PostgreSQL (prod via `DATABASE_URL`)
* **Static Files:** WhiteNoise
* **Production Server:** Gunicorn

---

## 📂 Project Structure

```
ecom/
  cart/                    # cart logic, views, urls, templates
  store/                   # products, categories, auth, templates
  static/                  # css, js, images (product images live here)
  media/                   # reserved for uploads
  ecom/                    # project settings, urls, wsgi
  manage.py
  requirements.txt
  Procfile
  build.sh
  runtime.txt
```

---

## 📸 Static & Media

* Static collected to `staticfiles/` in production.
* Product images in `static/images/products/`.
* Template tag `store/templatetags/product_images.py` maps product names to filenames.

Example mappings:

* "Atomic Habits" → `images/products/Atomic_Habits.jpg`
* "iPhone" → `images/products/iphone.jpg`

---

## 🚀 Quickstart (Local)

**Prerequisites:** Python 3.11+

```bash
# 1. Clone repository
git clone https://github.com/shivamr021/e-commerce.git
cd e-commerce

# 2. Create virtual environment (Windows)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# or macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Collect static files (optional for dev)
python manage.py collectstatic --no-input

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

Visit:

* Site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔐 Environment Variables

* `SECRET_KEY` (required in prod)
* `DEBUG` (`True`/`False`)
* `ALLOWED_HOSTS` (comma-separated)
* `DATABASE_URL` (optional)

---

## 🔧 Settings Highlights

* `STATIC_URL = '/static/'`
* `STATIC_ROOT = BASE_DIR / 'staticfiles'`
* `STATICFILES_DIRS = [ BASE_DIR / 'static' ]`
* `MEDIA_URL = '/media/'`
* `MEDIA_ROOT = BASE_DIR / 'media'`
* WhiteNoise Middleware & Storage for production

---

## 📦 Deployment (Render)

1. Connect repo to Render and create a Web Service
2. Build Command: `./build.sh`
3. Start Command: `gunicorn ecom.wsgi:application`
4. Set environment variables:

   * `SECRET_KEY`
   * `DEBUG=False`
   * `ALLOWED_HOSTS=.render.com,<your-service>.onrender.com`

**Notes:**

* Free tier sleeps after inactivity
* Ephemeral DB unless using a managed database

---

## 🛒 Cart Behavior

* Session-based cart
* Add/update/delete items
* Quantity updates on cart page

---

## 🛡️ Troubleshooting

* **400 Bad Request:** Check `ALLOWED_HOSTS`
* **Static files 404:** Run `collectstatic` & verify WhiteNoise settings
* **Images missing:** Check file naming and `product_images.py`
* **Invalid credentials in prod:** SQLite resets on deployment; recreate superuser or use managed DB

---

## 📋 License

No license specified.

---

## 📚 Repository

[GitHub Repo](https://github.com/shivamr021/e-commerce)
