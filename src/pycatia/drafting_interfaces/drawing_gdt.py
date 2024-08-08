
from pycatia.drafting_interfaces.drawing_leaders import DrawingLeaders
from pycatia.drafting_interfaces.drawing_text_properties import DrawingTextProperties
from pycatia.drafting_interfaces.drawing_text_range import DrawingTextRange
from pycatia.system_interfaces.any_object import AnyObject


class DrawingGDT(AnyObject):

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> float:
        """
        Returns or sets the angle of the drawing GDT.
        The angle is measured between the axis system of the drawing view and the local axis system of the drawing GDT.
        The angle is measured in radians and is counted counterclockwise.
        Example:
        This example sets the angle of the MyGDT drawing GDT to 90 degrees clockwise.
        You first need to compute the angle in degrees and set the minus sign to indicate the rotation is clockwise.
            Angle90Clockwise = -90
            MyGDT.Angle = Angle90Clockwise

        :return:
        """
        return self.com_object.Angle

    @angle.setter
    def angle(self, angle_value: float):
        """sets the angle of the drawing GDT."""
        self.com_object.Angle = angle_value

    @property
    def leaders(self) -> DrawingLeaders:
        """
        Returns the drawing leader collection of the drawing GDT.
        Example:
            This example retrieves in LeaderCollection the collection of leaders of the MyGDT drawing GDT.
                Dim LeaderCollection As DrawingLeaders
                Set LeaderCollection = MyGDT.Leaders
        :return:
        """
        return self.com_object.Leaders

    @property
    def row_number(self) -> int:
        """
        Returns the number of lines in the GDT
        Example:
            This example retrieves in rowNumber the row number of the MyGDT drawing GDT
                rowNumber = MyGDT.RowNumber

        :return:
        """
        return self.com_object.RowNumber

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        Returns the text properties of the drawing GDT.
        Example:
            This example retrieves in TextProperties the text properties of the MyGDT drawing GDT..
                Dim TextProperties As DrawingTextProperties
                Set TextProperties = MyGDT.TextProperties

        :return:
        """
        return self.com_object.TextProperties

    @property
    def x(self) -> float:
        """
        Returns or sets the x coordinate of the drawing GDT.
        It is expressed with respect to the current view coordinate system. This coordinate,
        like any length, is measured in millimeters.
        Example:
            This example retrieves in X the x coordinate of the MyGDT drawing GDT.
                X = MyGDT.x

        :return:
        """
        return self.com_object.x

    @x.setter
    def x(self, x_val: float):
        """
        Sets the x coordinate of the drawing GDT.
        :param x_val:
        :return:
        """
        self.com_object.x = x_val

    @property
    def y(self) -> float:
        """
        Returns or sets the y coordinate of the drawing GDT.
        It is expressed with respect to the current view coordinate system.
        This coordinate, like any length, is measured in millimeters.
        Example:
            This example sets the y coordinate of the MyGDT drawing GDT to 5 inches.
            You need first to convert the 5 inches into millimeters.
                NewYCoordinate = 5*25.4/1000
                MyGDT.y = NewYCoordinate

        :return:
        """
        return self.com_object.y

    @y.setter
    def y(self, y_val: float):
        """
        Sets the y coordinate of the drawing GDT.
        :param y_val:
        :return:
        """
        self.com_object.y = y_val

    def get_reference_number(self, i_row_number: int) -> int:
        """
        Returns the number of references in a row of the GDT.
        Parameters:
            iRowNumber
                The number of the row to analyse.
        Returns:
            The number of references in this row.
        Example:
            This example gets the reference number of the MyGDT drawing GDT
                MyGDT.GetReferenceNumber(iRowNumber, oRefNumber)

        :param i_row_number:
        :return:
        """
        return self.com_object.GetReferenceNumber(i_row_number)

    def get_text_range(self, i_row_number: int, i_number) -> DrawingTextRange:
        """
        Returns the CATIADrawingTextRange of tolerance value and reference value.
        Parameters:
            iRowNumber
                The number of the row to analyse If iRowNumber equals 0 to analyse upper text or lower text.
                If iRowNumber is greater than 0 analyse tolerance value or reference value.
            iNumber
                The modifier to analyse in this row:
                    If iRowNumber equals 0 and iNumber = 0 represent upper text
                    If iRowNumber equals 0 and iNumber = 1 represent lower text
                    If iRowNumber is greater than 0 and iNumber equals 0 to analyse tolerance value
                    If iRowNumber is greater than 0 and iNumber is greater than 0 to analyse reference value.
        Returns:
            The CATIADrawingTextRange which is specified.
            If there is no text range which is corresponded above, then NULL is given back.
        Example:
            This example gets the TextRange on the specified line and modifier of the MyGDT drawing GDT
                MyGDT.GetTextRange(iRowNumber, iNumber, oTextRange)

        :param i_row_number:
        :param i_number:
        :return:
        """
        return self.com_object.GetTextRange(i_row_number, i_number)

    def get_tolerance_type(self, i_row_number) -> int:
        """
        Returns the symbol used in the row of the GDT.
        Parameters:
            iRowNumber
                The number of the row to analyze.
        Returns:
            The symbol in this row.
                0 : No GDT symbol. The specified row will be remove
                1 : Straightness GDT symbol
                2 : Flatness GDT symbol
                3 : Circularity GDT symbol
                4 : Cilindricity GDT symbol
                5 : Line profile GDT symbol
                6 : Surface profile GDT symbol
                7 : Angularity GDT symbol
                8 : Perpendicularity GDT symbol
                9 : Parallelism GDT symbol
                10 : Position GDT symbol
                11 : Concentricity GDT symbol
                12 : Symmetry
                13 : Circular runout GDT symbol
                14 : Total runout GDT symbol
        Example:
            This example gets the symbol on the specified line of the MyGDT drawing GDT
                MyGDT.GetToleranceType(iRowNumber, oGDTSymbol)

        :param i_row_number:
        :return:
        """
        return self.com_object.GetToleranceType(i_row_number)

    def set_tolerance_type(self, i_row_number: int, i_gdt_symbol: int) -> None:
        """
        Sets the symbol used in the row of the GDT.
        Parameters:
            iRowNumber
                The number of the row analyse. If the row doesn't exist, it will be created
            iGDTSymbol
                The symbol to use in this row.
        See also:
            CATIADrawingGDT::GetToleranceType
        Example:
            This example sets a symbol on a specified line of the MyGDT drawing GDT
                MyGDT.SetToleranceType(iRowNumber, iGDTSymbol)

        :param i_row_number:
        :param i_gdt_symbol:
        :return:
        """
        self.com_object.SetToleranceType(i_row_number, i_gdt_symbol)
