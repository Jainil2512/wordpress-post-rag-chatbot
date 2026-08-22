from app.vector_store import get_vector_store


def main():

    vector_store = get_vector_store()

    collection = vector_store._collection

    count = collection.count()

    print("Vectors stored:", count)


if __name__ == "__main__":
    main()