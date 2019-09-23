from a.a import A

class B(A):
    def method(self, i: int) -> float:
        return float(i)

if __name__ == "__main__":
    print(B().method(10))