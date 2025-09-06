[README.md](https://github.com/user-attachments/files/22185222/README.md)
# Club Reservation v3 (Render Ready)

## Features
- Customer reservation form (dark neon theme)
- Special requests with conditional photo uploads (up to 3, JPG/PNG ≤ 2MB)
- Admin dashboard (dark neon theme) with:
  - Search bar (simple text)
  - WhatsApp quick links
  - Thumbnails for uploaded photos
  - Confirm / Cancel / Delete reservations
  - Export to Excel (with date-time filename + clickable photo links)
- Table management (Add / Edit / View tables)
- Fresh empty database
- Demo admin account: `admin / admin123`
- Replaceable logo placeholder (`static/logo.png`)

## Requirements
- Python 3.10+

## Run Locally
```bash
cd club-reservation-v3-render
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run
```

## Deploy to Render
1. Push this project to GitHub.
2. In Render → New → Web Service.
3. Build Command:
   pip install -r requirements.txt
4. Start Command:
   gunicorn app:app
5. Done! Your app is live on https://<your-app-name>.onrender.com

## Notes
- Replace `static/logo.png` with your own logo.
- Uploaded photos go to `/uploads/`.
