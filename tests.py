from timer import Timer
import time

def test_basic():
    t = Timer()
    t.start("x")
    time.sleep(0.1)
    t.stop("x")
    assert "duration" in t.tasks["x"]

if __name__ == "__main__":
    test_basic()
    print("OK")
