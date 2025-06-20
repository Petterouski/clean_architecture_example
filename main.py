from core.use_cases import UseCases
from adapters.repository import Repository
from adapters.ui import UI

def main():
    repository = Repository()
    use_cases = UseCases(repository)
    ui = UI()

    use_cases.add_item("Data 1")
    use_cases.add_item("Data 2")

    items = use_cases.get_items()
    ui.display_items(items)

if __name__ == "__main__":
    main()