# pubchem_api.py

class PubChemClient:
    def search_by_name(self, name: str) -> dict:
        """Search PubChem by common name. Return full compound data."""
    
    def search_by_cid(self, cid: str) -> dict:
        """Search by PubChem CID."""
    
    def search_by_smiles(self, smiles: str) -> dict:
        """Search PubChem by SMILES string."""
    
    def get_structure_url(self, cid: str) -> str:
        """Return a URL to the compound structure image."""

    def fetch_properties(self, cid: str) -> dict:
        """Pull detailed properties (MP, BP, density, hazards, etc)."""

    def get_candidate_names(self, name: str) -> list:
        """Return a list of possible matching CIDs for ambiguous names."""

    def validate_fields(self, raw: dict) -> dict:
        """Normalize missing/null fields and map to internal schema."""
