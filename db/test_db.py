if __name__ == "__main__":
    from compound_db import Compound, CompoundLibrary, parse_compound_file

    library = CompoundLibrary()
    compounds = parse_compound_file("compounds.txt")

    for c in compounds:
        library.add_to_db(c)
    
    print("Current DB Contents:")
    library.list_from_db()
    library.close
