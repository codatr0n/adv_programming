import mvc_model as model
import mvc_view as view


def start():
    data = model.load_file('mvc_data.csv')
    view.start_view(data)


if __name__ == "__main__":
    start()