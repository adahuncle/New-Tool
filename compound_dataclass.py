from dataclasses import dataclass

@dataclass
class CompoundData:
    name: str
    formula: str
    mw: float
    mp: float | None
    bp: float | None
    density: float | None
    hazards: list[str] | None
    smiles: str
    inchi: str
    cid: int
    structure_url: str
