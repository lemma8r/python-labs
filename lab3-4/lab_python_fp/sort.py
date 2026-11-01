def main():
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

    # 1. С использованием lambda
    result_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_lambda)

    # 2. Без использования lambda (используем встроенную функцию abs)
    result_func = sorted(data, key=abs, reverse=True)
    print(result_func)

if __name__ == '__main__':
    main()
