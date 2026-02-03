import qrcode
import os

# Folder to save QR code images
qr_folder = "qr_codes"
os.makedirs(qr_folder, exist_ok=True)

# List of songs with download links
songs = [
    {
        "name": "Friends",
        "cover": "images/friends_cover.png",
        "link": "https://drive.google.com/file/d/1sfSz327KOy-jkGbvx9f6BMg_F_PJ_75T/view?usp=drive_link"
    }
]

# Generate QR codes
for song in songs:
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(song["link"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    filename = f"{song['name'].replace(' ', '_')}_QR.png"
    filepath = os.path.join(qr_folder, filename)
    img.save(filepath)
    print(f"Saved QR code for {song['name']} → {filepath}")
