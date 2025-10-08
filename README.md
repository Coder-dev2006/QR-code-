#  QR Code Generator (Python)
A simple Python project that generates **QR codes** from any text or URL using the `pyqrcode` library.  
You can save the QR code as both **SVG** and **PNG** files.

---

##  Features
-  Generate QR codes from any text or link  
-  Save as both `.svg` and `.png` formats  
-  Lightweight and fast  
-  Built using pure Python  

---

##  Requirements
Install the required libraries:

```bash
pip install pyqrcode pypng
🧠 Usage
Run the script in your terminal:

bash
Copy code
python qr_generator.py
Example:

python
Copy code
# Matn yoki link
s = "www.geeksforgeeks.org"

# QR code yaratish
url = pyqrcode.create(s)

# SVG fayl sifatida saqlash
url.svg("myqr.svg", scale=8)

# PNG fayl sifatida saqlash
url.png("myqr.png", scale=6)
 Output Files
After running the script, two files will be created in the same directory:

Copy code
myqr.svg
myqr.png
You can open these files to view or share your QR code.

 Project Structure
css
Copy code
qr-code-generator/
│
├── qr_generator.py
├── myqr.png
├── myqr.svg
└── README.md
 How It Works
The script takes any string (text or link).

It creates a QR code object using pyqrcode.create().

The QR code is saved as both SVG and PNG formats with customizable scale.

 Author
Developed by Coder-dev2006
 Simple and useful QR code generation example in Python.

 License
This project is licensed under the MIT License — free to use, modify, and share.
