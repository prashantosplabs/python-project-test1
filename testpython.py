# test_build.py
import time

def ain():
    print("=== Jenkins Build Test ===")
    print("Step 1: Starting build process...")
    time.sleep(1)

    print("Step 2: Simulating work...")
    for i in range(3):
        print(f"  -> Working... {i+100}")
        time.sleep(1)

    print("Step 3: Build completed successfully.")
    return 0

if __name__ == "__main__":
    exit(main())
