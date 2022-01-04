#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    a = dir(hidden_4)
    for cnt in range(len(a)):
        if a[cnt][:2] != "__":
            print(a[cnt])
