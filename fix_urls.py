import glob

target1 = 'const API_URL = "http://127.0.0.1:8000";'
target2 = 'const API_URL = "http://127.0.0.1:8000"'
replacement = 'const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";'

files = glob.glob('frontend/src/**/*.jsx', recursive=True)
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    if target1 in content or target2 in content:
        content = content.replace(target1, replacement)
        content = content.replace(target2, replacement)
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
