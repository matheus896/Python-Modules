import alchemy.transmutation.recipes


def main() -> None:
    """Reach a recipe inside a subpackage with an absolute import."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    recipe = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {recipe}")


if __name__ == "__main__":
    main()
