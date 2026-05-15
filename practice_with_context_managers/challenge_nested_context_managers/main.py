from contextlib import contextmanager

class DummyResource:
    def __init__(self):
        self.active = False

    def __enter__(self):
        self.active = True
        print("DummyResource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active = False
        print("DummyResource released")

@contextmanager
def temporary_flag():
    print("Flag set")
    try:
        yield
    finally:
        print("Flag cleared")

def use_resources():
    # 両方のコンテキストマネージャを同時に使う
    with DummyResource() as resource, temporary_flag():
        print("Inside nested context managers")
        # ここで例外を発生させても両方のクリーンアップ処理が実行される
        # raise RuntimeError("テスト例外")

use_resources()