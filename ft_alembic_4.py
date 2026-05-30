import alchemy

def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    main()