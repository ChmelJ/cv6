import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    with open(path, mode="r") as file:
        signal = file.readlines()
    return [float(value.strip()) for value in signal]


def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values):
    plt.plot(values)
    plt.show()


if __name__ == "__main__":
    my_signal = load_signal_from_txt("ekg_signal.txt")
    print(my_signal)
    print(signal_min(my_signal))
    print(signal_max(my_signal))
    print(signal_avg(my_signal))
    plot_signal(my_signal)
