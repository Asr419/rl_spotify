from dataclasses import dataclass

import numpy as np
import numpy.typing as npt
import pandas as pd


@dataclass
class DocCatalogue:
    """A class to store the documents in a catalogue."""

    def __init__(self, doc_df: pd.DataFrame, doc_id_column: str) -> None:
        """
        Args:
            doc_df (pd.DataFrame): dataframe containing idx and features of documents
            doc_id_column (str): column name of the document id
        """
        self.doc_df = doc_df
        self.doc_id_column = doc_id_column

        self.doc_df.set_index(self.doc_id_column, inplace=True)
        # sorting doc df by doc_id
        self.doc_df = self.doc_df.sort_index()

    def get_doc_features(self, doc_id: int) -> npt.NDArray[np.float64]:
        """Get the features of a document given its id."""
        return self.doc_df.loc[doc_id, :].values

    def get_docs_features(
        self, doc_ids: npt.NDArray[np.int_]
    ) -> npt.NDArray[np.float_]:
        """Get the features of documentß given list of ids."""
        item_features = self.doc_df.loc[doc_ids, :].values
        return item_features

    def get_all_item_features(self) -> npt.NDArray[np.float_]:
        """Get the features of all documents."""
        return self.doc_df.values


class SpotifyDocCatalogue(DocCatalogue):
    def __init__(self, doc_df: pd.DataFrame, doc_id_column: str) -> None:
        super().__init__(doc_df, doc_id_column)

        # create a dictionary of song_id to duration
        self.duration = self.doc_df["duration_ms"].values

    def get_song_duration(song_id: int) -> int:
        """Get the duration of a song given its id."""
        return self.doc_df.loc[doc_id, :].values