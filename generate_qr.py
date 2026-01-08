import qrcode
import os

# Folder to save QR code images
qr_folder = "qr_codes"
os.makedirs(qr_folder, exist_ok=True)

# List of songs with download links
songs = [
    {
        "name": "Bad Habits",
        "cover": "images/Bad Habits Cover (1).jpg",
        "link": "https://drive.google.com/uc?export=download&id=1mXo30T5K_l9wZw7NPvXw68paeZmpnfZ0"
    },
    {
        "name": "Song 2",
        "cover": "images/Song2.jpg",
        "link": "https://drive.google.com/uc?export=download&id=XXXX"
    },
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
