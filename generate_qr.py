import os
import qrcode

def generate_qrcodes(data_list, output_folder="qrcodes"):
    # Membuat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for data in data_list:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,  
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        file_path = os.path.join(output_folder, f"{data}.png")
        img.save(file_path)
        print(f"QR code untuk '{data}' telah disimpan di: {file_path}")

if __name__ == "__main__":
    data_list = [f"Item_{i:03}" for i in range(1, 101)]
    generate_qrcodes(data_list)
