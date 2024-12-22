import os
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcodes(names, output_folder="barcodes"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for name in names:
        # Membuat barcode dengan Code128
        barcode = Code128(name, writer=ImageWriter())
        file_path = os.path.join(output_folder, f"{name}.png")
        barcode.save(file_path)
        print(f"Barcode untuk '{name}' telah disimpan di: {file_path}")

if __name__ == "__main__":
    names_list = [
        "Yudan_Maulana", "John_Doe", "Jane_Doe", 
        "Product_123", "Item_456", "Sample_789"
    ]
    generate_barcodes(names_list)
