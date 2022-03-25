# Create your models here. (Each model represents a table)

from django.db.models import (
    CASCADE,
    SET_NULL,
    CharField,
    DateField,
    FloatField,
    ForeignKey,
    IntegerField,
    Model,
    TextChoices,
)


class Classes(TextChoices):
    CLASS_A = "Class A (Rhodopsin)"
    CLASS_B1 = "Class B1 (Secretin)"
    CLASS_B2 = "Class B2 (Adhesion)"
    CLASS_C = "Class C (Glutamate)"
    CLASS_D1 = "Class D1 (Ste2-like fungal pheromone)"
    CLASS_F = "Class F (Frizzled)"


class Methods(TextChoices):
    XRAY = "X-ray Diffraction"
    ELECTRON_CRYS = "Electron crystallography"
    ELECTRON_MICRO = "Electron microscopy"


class Protein(Model):
    uniprot_id = CharField(max_length=200, unique=True)
    accession = CharField(max_length=50)  # might not be unique due to different species
    iuphar_name = CharField(max_length=50)
    receptor_class = CharField(max_length=40, choices=Classes.choices)
    family = CharField(max_length=250)
    subfamily = CharField(max_length=250)
    species = CharField(max_length=250)


class Structure(Model):
    pdb_id = CharField(max_length=4, unique=True)
    method = CharField(max_length=25, choices=Methods.choices)
    resolution = FloatField(null=True, blank=True)
    deposition_date = DateField()
    # From PDB
    publication = CharField(max_length=250, null=True, blank=True)
    protein = ForeignKey(
        Protein, related_name="gpcrs", on_delete=CASCADE, null=True, blank=True
    )
    chain = CharField(max_length=1)  # chain used for mapping


class AlloStructure(Model):
    ligand_id = CharField(max_length=3)
    structure = ForeignKey(Structure, on_delete=SET_NULL, null=True)


class Similarities(Model):
    allo_structure = ForeignKey(
        AlloStructure, on_delete=CASCADE, related_name="AlloStructure"
    )
    structure = ForeignKey(Structure, on_delete=CASCADE, related_name="Structure")
    rmsd = FloatField(null=True, blank=True)  # structure based RMSD
    probe_overlap = IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("allo_structure", "structure")
