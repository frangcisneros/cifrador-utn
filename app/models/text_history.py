from dataclasses import dataclass
from app import db  # Importa la instancia db desde el módulo app


@dataclass(init=False, repr=True, eq=True)
class TextHistory(db.Model):
    __tablename__ = "text_history"  # Nombre de la tabla en la base de datos
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entries: list[str] = db.Column(db.ARRAY(db.String(255)), nullable=False, default=[])

    # Definición de la relación inversa con la tabla 'texto' (texto)
    texts = db.relationship("Texto", back_populates="history")

    def add_entry(self, entry: str):
        """Add a new entry to the history."""
        self.entries.append(entry)

    def view_history(self):
        """View the entire history."""
        return self.entries
