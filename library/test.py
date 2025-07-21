from compound_library import CompoundLibrary, Compound, parse_compound_file

if __name__ == "__main__":
    library = CompoundLibrary()
    compounds = parse_compound_file("compounds.txt")
    for c in compounds:
        library.add_compounds(c)

    library.list_compounds()

    print("------------------------------------------------------------------------------------------------------------------------------------------")

    library.remove_compounds("Water")

    library.list_compounds()

    print("------------------------------------------------------------------------------------------------------------------------------------------")

    library.search_compounds("Acetone")

    print("------------------------------------------------------------------------------------------------------------------------------------------")

    for c in compounds:
        library.add_compounds(c)

    library.list_compounds()