
from enum import Enum


class CatDimType(Enum):
    """尺寸标注类型"""
    # Distance.
    catDimDistance = 0

    # Distance offset.
    catDimDistanceOffset = 1

    # Length.
    catDimLength = 2

    # Curvilinear length.
    catDimLengthCurvilinear = 3

    # Angle.
    catDimAngle = 4

    # Radius.
    catDimRadius = 5

    # Tangent radius.
    catDimRadiusTangent = 6

    # Cylinder radius.
    catDimRadiusCylinder = 7

    # Edge radius.
    catDimRadiusEdge = 8

    # Diameter.
    catDimDiameter = 9

    # Tangent diameter.
    catDimDiameterTangent = 10

    # Cylinder diameter.
    catDimDiameterCylinder = 11

    # Edge diameter.
    catDimDiameterEdge = 12

    # Cone diameter.
    catDimDiameterCone = 13

    # Chamfer.
    catDimChamfer = 14

    # Slope.
    catDimSlope = 15

    # Circular length.
    catDimLengthCircular = 16

    # Fillet radius.
    catDimRadiusFillet = 17

    # Torus diamater.
    catDimDiameterTorus = 18

    # Torus radius.
    catDimRadiusTorus = 19

    # Minimum distance.
    catDimDistanceMin = 20


class CatTextFrameType(Enum):
    """文字边框类型"""
    # No frame is drawn
    catNone = 0

    # The frame is a rectangle
    catRectangle = 1

    # The frame is a square
    catSquare = 2

    # The frame is a circle
    catCircle = 3

    # The frame is a scored circle
    catScoredCircle = 4

    # The frame is a diamond
    catDiamond = 5

    # The frame is a triangle
    catTriangle = 6

    # The frame is a right flag
    catRightFlag = 7

    # The frame is a left flag
    catLeftFlag = 8

    # The frame is a left flag and a right flag
    catBothFlag = 9

    # The frame is oblong
    catOblong = 10

    # The frame is an ellipse
    catEllipse = 11

    # The frame is customized
    catCustom = 12


class ToleranceType(Enum):
    """ `DrawingGDT.GetToleranceType` 返回的GDT类型."""
    # 没有GDT符号，The specified row will be to remove
    NO_GDT = 0
    # 直线度
    Straightness = 1
    # 平面度
    Flatness = 2
    # 圆度
    Circularity = 3
    # 圆柱度
    Cylindricity = 4
    # 直线轮廓
    Line_profile = 5
    # 曲面轮廓
    Surface_profile = 6
    # 倾斜度
    Angularity = 7
    # 垂直度
    Perpendicularity = 8
    # 平行度
    Parallelism = 9
    # 位置度
    Position = 10
    # 同心度
    Concentricity = 11
    # 对称性
    Symmetry = 12
    # 圆跳动度
    Circular_runout = 13
    # 全跳动度
    Total_runout = 14
