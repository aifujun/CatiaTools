from typing import Iterator

from pycatia.drafting_interfaces.drawing_gdt import DrawingGDT
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class DrawingGDTs(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingGDT)
        self.com_object = com_object

    def add(self,
            i_position_leader_x: float,
            i_position_leader_y: float,
            i_position_x: float,
            i_position_y: float,
            i_gdt_symbol: int,
            i_text: str) -> DrawingGDT:
        """
        Creates a drawing GDT and adds it to the drawing GDTs collection. This drawing GDT becomes the active one.
        Parameters:
            iPositionLeaderX,
                iPositionLeaderY The drawing leader of the GDT x and y coordinates,
                expressed in millimeters, and expressed with respect to the view coordinate system
            iPositionX,
                iPositionY The drawing GDT x and y coordinates,
                expressed in millimeters, and expressed with respect to the view coordinate system
            iGDTSymbol
                The symbol to use in the first row.
        See also:
            CATIADrawingGDT::GetToleranceType
        Parameters:
            iText
                The text of the iGDTSymbol

        :param i_position_leader_x:
        :param i_position_leader_y:
        :param i_position_x:
        :param i_position_y:
        :param i_gdt_symbol:
        :param i_text:
        """
        return DrawingGDT(
            self.com_object.Add(
                i_position_leader_x,
                i_position_leader_y,
                i_position_x,
                i_position_y,
                i_gdt_symbol,
                i_text
            )
        )

    def item(self, i_index: cat_variant) -> DrawingGDT:
        """
        Returns a drawing GDT using its index from the drawing GDTs collection.
        Parameters:
            iIndex
                The index of the drawing GDT to retrieve from the collection of drawing GDTs. As a numerics,
                this index is the rank of the drawing GDT in the collection.
                The index of the first drawing GDT in the collection is 1,
                and the index of the last drawing GDT is Count.
        Returns:
            The retrieved drawing GDT
        Example:
            This example retrieves in ThisDrawingGDT the second drawing GDT,
            in the drawing GDT collection of the active view in the active sheet,
            in the active document supposed to be a drawing document.
                Dim MyView  As DrawingView
                Set MyView  = MySheet.Views.ActiveView
                Dim ThisDrawingGDT As DrawingGDT
                Set ThisDrawingGDT = MyView.GDTs.Item(2)

        :param i_index:
        :rtype: DrawingGDT
        """
        return DrawingGDT(self.com_object.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        Removes a drawing GDT from the drawing GDTs collection.
            Parameters:
                iIndex
                    The index of the drawing GDT to remove from the collection of drawing GDTs. As a numerics, this index is the rank of the drawing text in the collection. The index of the first drawing GDT in the collection is 1, and the index of the last drawing GDT is Count.
        Example:
            The following example removes the third drawing GDT from the drawing GDT collection of the active view of the active document, supposed to be a drawing document.
                Dim MyView As DrawingView
                Set MyView  = MySheet.Views.ActiveView
                MyView.GDTs.Remove(3)

        :param cat_variant i_index:
        :rtype: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingGDT:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingGDT(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingGDT]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingGDTs(name="{self.name}")'
