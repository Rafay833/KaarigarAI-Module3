🛠️ KaarigarAI - Module 3: Image Enhancement
This repository contains the backend logic for Module 3 of the KaarigarAI project. It focuses on preparing product images for marketplace listing by removing backgrounds and improving resolution.

Key Features
Background Removal: Uses the rembg library (U2Net model) to automatically isolate products.

Resolution Upscaling: Ensures all processed images meet a minimum requirement of 1000x1000 pixels.

FastAPI Integration: Provides a clean POST /image/enhance endpoint for the frontend to connect to.

How to Run Locally
Install dependencies:

pip install -r requirements.txt

Start the server:

python -m uvicorn main:app --reload

Access documentation:

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
