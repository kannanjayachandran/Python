import matplotlib.pyplot as plt


def main():

    sentence = """
                Python is a high-level, general-purpose programming language. Its design philosophy emphasizes 
                code readability with the use of significant indentation. Python is dynamically typed and 
                garbage-collected. It supports multiple programming paradigms, including structured, object-oriented 
                and functional programming
                """
    counter = {}
    for letter in sentence:
        counter[letter.lower()] = counter.get(letter, 0) + 1

    x_value, y_value = zip(*counter.items())
    plt.bar(x_value, y_value)
    plt.show()

    counter_clean = {}
    for key, value in counter.items():
        if key.isalpha():
            counter_clean[key] = value

    x_value, y_value = zip(*counter_clean.items())

    plt.plot(x_value, y_value, color='blue', marker='o', linestyle='dotted',
        linewidth=2, markersize=8)
    plt.show()


if __name__ == '__main__':
    main()
