# 🐾 Raster to Vector Converter for Coloring Books

This script helps automatically convert raster images (PNG/JPG) to vector SVG files with minimal setup — perfect for children's coloring books.

## ✨ Features

- Processes all images from the `input_images/` folder
- Converts them to SVG using `potrace`
- Generates an HTML file for easy side-by-side comparison
- Automatically deletes temporary `.pbm` files

## 🚀 How to Use

### 1. Install Dependencies

```bash
sudo apt install imagemagick potrace
```

### 2. Prepare Project Structure

```bash
.
├── convert_to_svg.py
├── input_images/      # Place PNG and JPG files here
└── output_svg/        # SVGs and HTML will be saved here
```

### 3. Run the Script

```bash
python3 convert_to_svg.py
```

### 4. Open the Result

The file `output_svg/index.html` will show original images and their vector versions side-by-side.

## 📎 Sample Output

![Sample](preview.png)

## 📜 License

MIT — use and adapt freely. If you improve it, consider a pull request 🙌
