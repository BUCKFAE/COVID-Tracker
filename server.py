from data_handler import DataHandler


def main():
    print("Server has been started!")

    data_handler = DataHandler()
    data_handler.update_data()


if __name__ == "__main__":
    main()
