import pytest
import sys

if __name__ == "__main__":
    print("Running tests via pytest.main()...")
    ret = pytest.main(["tests/"])
    print(f"Pytest return code: {ret}")
