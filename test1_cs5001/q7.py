def main():
    msg = "*"
    i = -5

    while True:
        msg = msg + "hello"
        i = i + 1

        if i < 0:
            continue
        else:
            break

    msg = msg + "*"
    print(msg)

if __name__ == "__main__":
    main()