from src.data_loader import get_project_root, get_data_directory


def main():
    print("Job Market Skill Tracker")
    print(f"Project root: {get_project_root()}")
    print(f"Data directory: {get_data_directory()}")


if __name__ == "__main__":
    main()