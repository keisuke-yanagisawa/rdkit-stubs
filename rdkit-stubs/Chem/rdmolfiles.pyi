from typing import Any, ClassVar, Optional, overload, IO
from types import TracebackType

from rdkit.Chem import Mol

class CXSmilesFields:
    CX_ALL: ClassVar[CXSmilesFields] = ...
    CX_ATOM_LABELS: ClassVar[CXSmilesFields] = ...
    CX_ATOM_PROPS: ClassVar[CXSmilesFields] = ...
    CX_COORDS: ClassVar[CXSmilesFields] = ...
    CX_ENHANCEDSTEREO: ClassVar[CXSmilesFields] = ...
    CX_LINKNODES: ClassVar[CXSmilesFields] = ...
    CX_MOLFILE_VALUES: ClassVar[CXSmilesFields] = ...
    CX_NONE: ClassVar[CXSmilesFields] = ...
    CX_POLYMER: ClassVar[CXSmilesFields] = ...
    CX_RADICALS: ClassVar[CXSmilesFields] = ...
    CX_SGROUPS: ClassVar[CXSmilesFields] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class ForwardSDMolSupplier:
    @overload
    def __init__(
        self,
        fileobj: IO,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    @overload
    def __init__(
        self,
        filename: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    def GetEOFHitOnRead(self) -> bool: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetProcessPropertyLists(self, arg2: bool): ...
    def atEnd(self) -> bool: ...
    def __enter__(self): ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MaeMolSupplier:
    @overload
    def __init__(self, fileobj: IO, sanitize: bool = ..., removeHs: bool = ...): ...
    @overload
    def __init__(self, filename: str, sanitize: bool = ..., removeHs: bool = ...): ...
    def atEnd(self) -> bool: ...
    def __enter__(self): ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MultithreadedSDMolSupplier:
    __instance_size__: ClassVar[int] = ...
    def __init__(
        self,
        fileName: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = True,
        numWriterThreads: int = ...,
        sizeInputQueue: int = ...,
        sizeOutputQueue: int = ...,
    ): ...
    def GetLastItemText(self) -> str: ...
    def GetLastRecordId(self) -> int: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetProcessPropertyLists(self, arg2: bool): ...
    def atEnd(self) -> bool: ...
    def __enter__(self): ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MultithreadedSmilesMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetLastItemText(cls, RDKit) -> Any: ...
    @classmethod
    def GetLastRecordId(cls, RDKit) -> Any: ...
    @classmethod
    def atEnd(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class PDBWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SDMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetItemText(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetProcessPropertyLists(cls, RDKit) -> Any: ...
    @classmethod
    def SetData(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetProcessPropertyLists(cls, RDKit, bool) -> Any: ...
    @classmethod
    def _SetStreamIndices(cls, RDKit, boost) -> Any: ...
    @classmethod
    def atEnd(cls, RDKit) -> Any: ...
    @classmethod
    def reset(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SDWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetForceV3000(cls, RDKit) -> Any: ...
    @classmethod
    def GetKekulize(cls, RDKit) -> Any: ...
    def GetText(self, *args, **kwargs) -> Any: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def SetForceV3000(cls, RDKit, bool) -> Any: ...
    @classmethod
    def SetKekulize(cls, RDKit, bool) -> Any: ...
    @classmethod
    def SetProps(cls, RDKit, boost) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmartsParserParams:
    __instance_size__: ClassVar[int] = ...
    allowCXSMILES: Any
    debugParse: Any
    mergeHs: Any
    parseName: Any
    strictCXSMILES: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetItemText(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetData(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def reset(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesParserParams:
    __instance_size__: ClassVar[int] = ...
    allowCXSMILES: Any
    debugParse: Any
    parseName: Any
    removeHs: Any
    sanitize: Any
    strictCXSMILES: Any
    useLegacyStereo: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesWriteParams:
    __instance_size__: ClassVar[int] = ...
    allBondsExplicit: Any
    allHsExplicit: Any
    canonical: Any
    doIsomericSmiles: Any
    doKekule: Any
    doRandom: Any
    rootedAtAtom: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def SetProps(cls, RDKit, boost) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class TDTMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetItemText(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetData(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def reset(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class TDTWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetNumDigits(cls, RDKit) -> Any: ...
    @classmethod
    def GetWrite2D(cls, RDKit) -> Any: ...
    @classmethod
    def GetWriteNames(cls, RDKit) -> Any: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def SetNumDigits(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetProps(cls, RDKit, boost) -> Any: ...
    @classmethod
    def SetWrite2D(cls, RDKit) -> Any: ...
    @classmethod
    def SetWriteNames(cls, RDKit) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def AddMetadataToPNGFile(*args, **kwargs) -> Any: ...
def AddMetadataToPNGString(*args, **kwargs) -> Any: ...
def AtomFromSmarts(*args, **kwargs) -> Any: ...
def AtomFromSmiles(*args, **kwargs) -> Any: ...
def BondFromSmarts(*args, **kwargs) -> Any: ...
def BondFromSmiles(*args, **kwargs) -> Any: ...
@overload
def CanonicalRankAtoms(mol, breakTies=...) -> Any: ...
@overload
def CanonicalRankAtoms(RDKit) -> Any: ...
@overload
def CanonicalRankAtomsInFragment(mol, atomsToUse=..., breakTies=...) -> Any: ...
@overload
def CanonicalRankAtomsInFragment(RDKit, boost) -> Any: ...
def CreateAtomBoolPropertyList(*args, **kwargs) -> Any: ...
def CreateAtomDoublePropertyList(*args, **kwargs) -> Any: ...
def CreateAtomIntPropertyList(*args, **kwargs) -> Any: ...
def CreateAtomStringPropertyList(*args, **kwargs) -> Any: ...
def MetadataFromPNGFile(boost) -> Any: ...
def MetadataFromPNGString(boost) -> Any: ...
def MolFragmentToCXSmarts(RDKit, boost) -> Any: ...
def MolFragmentToCXSmiles(RDKit, boost) -> Any: ...
def MolFragmentToSmarts(RDKit, boost) -> Any: ...
def MolFragmentToSmiles(RDKit, boost) -> Any: ...
def MolFromFASTA(*args, **kwargs) -> Any: ...
def MolFromHELM(boost) -> Any: ...
def MolFromMol2Block(*args, **kwargs) -> Any: ...
def MolFromMol2File(*args, **kwargs) -> Any: ...
def MolFromMolBlock(boost) -> Any: ...
def MolFromMolFile(*args, **kwargs) -> Any: ...
def MolFromPDBBlock(boost) -> Any: ...
def MolFromPDBFile(*args, **kwargs) -> Any: ...
def MolFromPNGFile(*args, **kwargs) -> Any: ...
def MolFromPNGString(boost) -> Any: ...
def MolFromRDKitSVG(boost) -> Any: ...
def MolFromSequence(boost) -> Any: ...
@overload
def MolFromSmarts(boost) -> Any: ...
@overload
def MolFromSmarts(boost, RDKit) -> Any: ...
def MolFromSmiles(*args, **kwargs) -> Mol: ...
def MolFromTPLBlock(boost) -> Any: ...
def MolFromTPLFile(*args, **kwargs) -> Any: ...
def MolMetadataToPNGFile(RDKit, boost) -> Any: ...
def MolMetadataToPNGString(RDKit, boost) -> Any: ...
def MolToCMLBlock(RDKit) -> Any: ...
def MolToCMLFile(*args, **kwargs) -> Any: ...
def MolToCXSmarts(RDKit) -> Any: ...
def MolToCXSmiles(RDKit) -> Any: ...
def MolToFASTA(RDKit) -> Any: ...
def MolToHELM(RDKit) -> Any: ...
def MolToMolBlock(RDKit) -> Any: ...
def MolToMolFile(*args, **kwargs) -> Any: ...
def MolToPDBBlock(RDKit) -> Any: ...
def MolToPDBFile(*args, **kwargs) -> Any: ...
def MolToRandomSmilesVect(*args, **kwargs) -> Any: ...
def MolToSequence(RDKit) -> Any: ...
def MolToSmarts(RDKit) -> Any: ...
def MolToSmiles(RDKit) -> Any: ...
def MolToTPLBlock(RDKit) -> Any: ...
def MolToTPLFile(*args, **kwargs) -> Any: ...
def MolToV3KMolBlock(RDKit) -> Any: ...
def MolToV3KMolFile(*args, **kwargs) -> Any: ...
def MolToXYZBlock(RDKit) -> Any: ...
def MolToXYZFile(*args, **kwargs) -> Any: ...
def MolsFromPNGFile(*args, **kwargs) -> Any: ...
def MolsFromPNGString(boost) -> Any: ...
def SmilesMolSupplierFromText(*args, **kwargs) -> Any: ...
