import time
import json

class Timer:
    def __init__(self):
        self.tasks = {}

    def start(self, name):
        self.tasks[name] = {"start": time.time()}

    def stop(self, name):
        if name in self.tasks:
            self.tasks[name]["duration"] = time.time() - self.tasks[name]["start"]

    def report(self):
        print(json.dumps(self.tasks, indent=2, default=str))

if __name__ == "__main__":
    t = Timer()
    t.start("demo")
    time.sleep(0.5)
    t.stop("demo")
    t.report()
